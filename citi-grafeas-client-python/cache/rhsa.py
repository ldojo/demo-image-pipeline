"""Provides RhsaToCveCache class"""

from io import StringIO
from csv import reader
import requests

class RhsaToCveCache():
  """Creates and stores a mapping of Red Hat Security Advisories (RHSA) to CVEs from Red Hat public info"""
  def __init__(self, url='https://www.redhat.com/security/data/metrics/rhsamapcpe.txt'):
    self.rhsa_to_cve_cache = dict()
    if url is None:
      return
    req = requests.get(url)
    data_as_file = StringIO(req.text)
    self.__load_rhsa_to_cve__(data_as_file)

  def __str__(self):
    return str(self.rhsa_to_cve_cache)

  def get_cves(self, key: str):
    """Returns list of CVEs mapping to specific RHSA"""
    return self.rhsa_to_cve_cache[key]

  def __load_rhsa_to_cve__(self, file):
    rhsa_to_cve_reader = reader(file, delimiter=' ')

    # Create a dictionary of all the RHSA with their corresponding list of CVEs
    for row in rhsa_to_cve_reader:
      self.rhsa_to_cve_cache[row[0]] = row[1].split(',')
