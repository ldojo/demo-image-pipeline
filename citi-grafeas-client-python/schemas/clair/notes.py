"""Clair-specific creation of Notes for Grafeas"""
import logging
from proto.v1beta1.vulnerability_pb2 import Severity, Vulnerability, MINIMAL, SEVERITY_UNSPECIFIED
from proto.v1beta1.package_pb2 import Version
from schemas.notes import Note, VulnerabilityNote

class ClairVulnerabilityNote(Note):
  """Derives from Note parent to create Notes specific to Clair results"""
  @staticmethod
  def create_vulnerability_note(cve_details: list):
    """Static method to create a ClairVulnerabilityNote from a list of Clair JSON vulnerabilities"""
    logging.debug('CVE Details: %s', cve_details)
    vul_details = list()

    for cve_detail in cve_details:
      the_details = Vulnerability.Detail()
      if 'Description' not in cve_details:
        the_details.description = 'N/A'
      else:
        the_details.description = cve_detail['Description']
      the_details.package = cve_detail['FeatureName']
      the_details.package_type = 'native'
      if cve_detail['Severity'].upper() == 'NEGLIGIBLE':
        severity = MINIMAL
      elif cve_detail['Severity'].upper() == 'UNKNOWN':
        severity = SEVERITY_UNSPECIFIED
      else:
        severity = Severity.Value(cve_detail['Severity'].upper())
      the_details.severity_name = Severity.Name(severity)
      the_details.cpe_uri = cve_detail['NamespaceName']

      version = the_details.min_affected_version
      version.name = cve_detail['FeatureVersion']
      version.revision = '1'
      version.kind = Version.VersionKind.Value('NORMAL')

      vul_details.append(the_details)

    short_desc = cve_details[0]['Name']
    name = cve_details[0]['Name']
    if 'Description' not in cve_details[0]:
      long_desc = 'N/A'
    else:
      long_desc = cve_details[0]['Description']
    if cve_details[0]['Severity'].upper() == 'NEGLIGIBLE':
      severity = MINIMAL
    elif cve_details[0]['Severity'].upper() == 'UNKNOWN':
      severity = SEVERITY_UNSPECIFIED
    else:
      severity = Severity.Value(cve_details[0]['Severity'].upper())

    return VulnerabilityNote(name, short_desc, long_desc, severity, vul_details)
