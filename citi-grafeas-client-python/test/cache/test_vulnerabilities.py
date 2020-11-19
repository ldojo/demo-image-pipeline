import json
import unittest
from test.cache.utils import JSON_CLAIR_OUTPUT
from cache.vulnerabilities import VulnerabilityCache

class VulnerabilityCacheTest(unittest.TestCase):
  def test_add_single_vulnerability(self):
    self.cache.add_vulnerability(self.parsed_json['Vulnerabilities'][0])
    for key in self.cache.get_vulnerabilities():
      self.assertNotRegex(key, 'RHSA.*')

  def test_add_all_vulnerabilities(self):
    for vulnerability in self.parsed_json['Vulnerabilities']:
      self.cache.add_vulnerability(vulnerability)

    # Make sure we don't have any RHSA keys
    self.assertNotIn('RHSA-2019:3575', self.cache.get_vulnerabilities())

    cves = ['CVE-2019-7146', 'CVE-2019-7149', 'CVE-2019-7150', 'CVE-2019-7664', 'CVE-2019-7665']
    for cve in cves:
      # Make sure the above RHSA was properly translated to CVEs
      self.assertIn(cve, self.cache.get_vulnerabilities())
      # RHSA-2019:3575 has 3 packages associated with it, make sure we have 3 packages associated with the CVE
      self.assertEqual(len(self.cache.get_vulnerabilities()[cve]), 3)


  def setUp(self):
    self.parsed_json = json.loads(JSON_CLAIR_OUTPUT)
    self.cache = VulnerabilityCache()
