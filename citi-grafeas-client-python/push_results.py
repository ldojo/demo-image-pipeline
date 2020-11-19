""" Pushes the results of an image scan with Clair. Accepts a file or STDIN"""
import json
import sys
import argparse
import logging
import pprint
import grpc
from proto.v1beta1 import grafeas_pb2_grpc, grafeas_pb2
from proto.v1beta1 import project_pb2_grpc, project_pb2
from proto.v1beta1.vulnerability_pb2 import Severity
from schemas.clair.notes import ClairVulnerabilityNote
from schemas.occurrences import VulnerabilityOccurrence
from cache.vulnerabilities import VulnerabilityCache
from operators.metadata import OperatorMetadata


def parse_arguments():
  """Builds the argument parser"""
  parser = argparse.ArgumentParser()
  parser.add_argument('project', help='Project name associated with this image scan.')
  parser.add_argument('--host', default='localhost:8080', help='Grafeas host in <hostname>:<port> format')
  parser.add_argument('-i', '--image', help='Override the URI of the image to which the scan results belong.')
  parser.add_argument(
    '-f',
    '--file',
    required=False,
    help="File container scan results in JSON format (use '-' for STDIN)")
  parser.add_argument(
    '-o',
    '--operator-catalog-host',
    help='Host for the Operator Catalog API service in <hostname>:<port> format',
    default='http://localhost:8081')
  parser.add_argument('-v', '--verbose', help='Increase log output.', action='store_true')
  return parser.parse_args()

def push_clair_results(target_vul_project, target_project, input_file, image_override, operator_catalog_host):
  """Creates vulnerabilities from the given Clair file and pushes to Grafeas"""
  occurrence_count = dict()

  if input_file == '-':
    the_file = sys.stdin
  else:
    the_file = open(input_file)

  with the_file as results_file:
    logging.debug('Loading scan results...')
    results_data = json.load(results_file)
    logging.debug('Scan results loaded!')

  cache = VulnerabilityCache(results_data['Vulnerabilities'])
  logging.debug(cache.get_vulnerabilities())

  if image_override is None:
    image_name = results_data['ImageName']
  else:
    image_name = image_override

  operator_metadata = OperatorMetadata(operator_catalog_host)
  operators = operator_metadata.get_image_operators([image_name])
  if image_name in operators:
    resource_details = {'uri': image_name, 'operator_details': operators[image_name]}
  else:
    resource_details = {'uri': image_name, 'operator_details': list()}


  for vul_list in cache.get_vulnerabilities().values():
    vul_note = ClairVulnerabilityNote.create_vulnerability_note(vul_list)

    grafeas_stub = grafeas_pb2_grpc.GrafeasV1Beta1Stub(channel)
    try:
      logging.debug('Creating note: %s', vul_note)
      note = grafeas_stub.CreateNote(
        grafeas_pb2.CreateNoteRequest(
          parent=target_vul_project,
          note_id=vul_note.name,
          note=vul_note.note))
      vul_note.note = note
      logging.debug('Created note: %s', vul_note)
    except grpc.RpcError as error:
      logging.debug('Error code: %s', error.code())
      if error.code() == grpc.StatusCode.ALREADY_EXISTS:
        logging.warning('Note already exists, retrieving existing note...')
        logging.debug(
          'Searching for note with location %s/notes/%s: %s',
          target_vul_project,
          vul_note.name,
          vul_note)

        note = grafeas_stub.GetNote(
          grafeas_pb2.GetNoteRequest(
            name="{}/notes/{}".format(target_vul_project, vul_note.name)))
        vul_note.note = note
        logging.debug('Existing note: %s', note)
      else:
        raise

    try:
      logging.debug('Creating occurrence...')
      vul_occur = VulnerabilityOccurrence.create_vulnerability_occurrence(resource_details, vul_note)

      grafeas_stub.CreateOccurrence(
        grafeas_pb2.CreateOccurrenceRequest(
          parent=target_project.name,
          occurrence=vul_occur.occurrence))
      if vul_note.severity in occurrence_count:
        occurrence_count[Severity.Name(vul_note.severity)] += 1
      else:
        occurrence_count[Severity.Name(vul_note.severity)] = 1
    except grpc.RpcError as error:
      logging.fatal('Error creating occurrence: %s', error)
      raise

  total_occurrences = sum(occurrence_count.values())
  logging.info('Created %d occurrences', total_occurrences)
  logging.info('Severities: ' + pprint.pprint(occurrence_count))


if __name__ == '__main__':
  args = parse_arguments()
  if args.verbose:
    logging.basicConfig(level=logging.DEBUG)
  else:
    logging.basicConfig(level=logging.INFO)

  # Look for existing project, otherwise create it
  logging.debug('Searching for project %s', args.project)

  channel = grpc.insecure_channel(args.host)
  project_stub = project_pb2_grpc.ProjectsStub(channel)
  parent_project = 'projects/' + args.project
  vul_project = 'projects/vulnerabilities'

  # Get the main CVE project to add notes as needed
  try:
    cve_project = project_stub.GetProject(project_pb2.GetProjectRequest(name='projects/vulnerabilities'))
  except grpc.RpcError as error:
    logging.debug('Error code: %s', error.code())
    if error.code() == grpc.StatusCode.NOT_FOUND:
      cve_project = project_stub.CreateProject(
        project_pb2.CreateProjectRequest(
          project=project_pb2.Project(name='projects/vulnerabilities')))
    else:
      raise

  app_project = None
  try:
    app_project = project_stub.GetProject(project_pb2.GetProjectRequest(name=parent_project))
    logging.debug('Found project: %s', app_project)
  except grpc.RpcError as error:
    logging.debug('Error code: %s', error.code())
    if error.code() == grpc.StatusCode.NOT_FOUND:
      logging.debug('Failed to find project: %s', args.project)

      logging.debug('Creating missing project...')
      app_project = project_stub.CreateProject(
        project_pb2.CreateProjectRequest(
          project=project_pb2.Project(name=parent_project)))
      logging.info('Created project: %s', app_project)

  push_clair_results(vul_project, app_project, args.file, args.image, args.operator_catalog_host)
