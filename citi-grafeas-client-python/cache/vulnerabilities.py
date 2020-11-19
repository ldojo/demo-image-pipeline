"""Provides a cache for vulnerabilities provided by Red Hat Security Advisories"""

from cache.rhsa import RhsaToCveCache

class VulnerabilityCache():
  """Wrapper around dictionary that provides the vulnerability cache"""
  def __init__(self, vulnerabilities: list = None):
    self.vulnerabilities = dict()
    self.rhsa_to_cve_cache = dict()
    if vulnerabilities:
      for vulnerability in vulnerabilities:
        self.add_vulnerability(vulnerability)

  def add_vulnerability(self, vulnerability: dict):
    """Add vulnerabilities to the cache"""
    key = vulnerability['Name']
    if key.startswith('RHSA'):
      cves = self.__rhsa_to_cve_cache__().get_cves(key)
      for cve in cves:
        filtered_cve = vulnerability.copy()
        filtered_cve['Name'] = cve
        self.add_vulnerability(filtered_cve)
      return
    if key in self.vulnerabilities:
      self.vulnerabilities[key].append(vulnerability)
    else:
      self.vulnerabilities[key] = list()
      self.vulnerabilities[key].append(vulnerability)

  def get_vulnerabilities(self):
    """Return all the vulnerabilities"""
    return self.vulnerabilities

  def __rhsa_to_cve_cache__(self):
    if not self.rhsa_to_cve_cache:
      self.rhsa_to_cve_cache = RhsaToCveCache()

    return self.rhsa_to_cve_cache
