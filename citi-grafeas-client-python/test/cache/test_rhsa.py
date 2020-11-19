import unittest
from io import StringIO
from cache.rhsa import RhsaToCveCache

class RhsaToCveCacheTest(unittest.TestCase):
  def test_load_rhsa_to_cve(self):
    test_data = '''RHSA-2020:3389 CVE-2020-12653,CVE-2020-12654 cpe:/a:redhat:enterprise_mrg:2:server:el6/kernel-rt
RHSA-2020:3388 CVE-2019-17639,CVE-2020-2590,CVE-2020-2601,CVE-2020-14577,CVE-2020-14578,CVE-2020-14579,CVE-2020-14583,CVE-2020-14593,CVE-2020-14621 cpe:/a:redhat:rhel_extras:7/java-1.7.1-ibm
'''
    data_as_file = StringIO(test_data)
    cache = RhsaToCveCache(None)
    cache.__load_rhsa_to_cve__(data_as_file)

    self.assertEqual(len(cache.get_cves('RHSA-2020:3389')), 2)
    self.assertEqual(len(cache.get_cves('RHSA-2020:3388')), 9)
