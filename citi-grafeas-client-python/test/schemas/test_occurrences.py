import unittest
from schemas.occurrences import VulnerabilityOccurrence
from schemas.notes import VulnerabilityNote
from proto.v1beta1.package_pb2 import Version
from proto.v1beta1.vulnerability_pb2 import MEDIUM, Severity, Vulnerability

class VulnerabilityOccurrenceTest(unittest.TestCase):
  def setUp(self):
    vul_details = list()
    the_details = Vulnerability.Detail()
    the_details.description = 'N/A'
    the_details.package = 'dbus'
    the_details.package_type = 'native'
    severity = MEDIUM
    severity = Severity.Value('MEDIUM')
    the_details.severity_name = Severity.Name(severity)
    the_details.cpe_uri = 'cpe:rhel8'

    version = the_details.min_affected_version
    version.name = '1.0.0'
    version.revision = '1'
    version.kind = Version.VersionKind.Value('NORMAL')

    vul_details.append(the_details)
    self.note = VulnerabilityNote('test-cve', 'test-cve-short-desc', 'test-cve-long-desc', MEDIUM, vul_details)

  def test_vulnerability_occurrence(self):
    resource = {
      VulnerabilityOccurrence.RESOURCE_URI: 'docker.io/library/httpd:latest',
      VulnerabilityOccurrence.RESOURCE_OPERATOR_DETAILS: [{'operatorName':'fake-operator', 'version': '0.0.1'}]
    }

    occurrence = VulnerabilityOccurrence.create_vulnerability_occurrence(resource, self.note)
    self.assertEqual(occurrence.occurrence.note_name, self.note.note.name)
