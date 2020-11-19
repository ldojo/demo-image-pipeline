import logging
from proto.v1beta1.vulnerability_pb2 import Severity
from proto.v1beta1.grafeas_pb2 import Note as GrafeasNote
from proto.v1beta1.common_pb2 import VULNERABILITY as VULNERABILITY_KIND


class Note():
  def __init__(self, name: str, short_desc: str, long_desc: str):
    self.name = name
    self.short_desc = short_desc
    self.long_desc = long_desc
    self.note = GrafeasNote()

class VulnerabilityNote(Note):
  def __init__(self, name: str, short_desc: str, long_desc: str, severity: Severity, vul_details: list):
    super().__init__(name, short_desc, long_desc)
    self.severity = severity

    self.note.short_description = self.short_desc
    self.note.long_description = self.long_desc
    self.note.kind = VULNERABILITY_KIND

    self.note.vulnerability.severity = self.severity
    for vul_detail in vul_details:
      details = self.note.vulnerability.details.add()
      details.CopyFrom(vul_detail)

    logging.debug('Note: %s', self.note)

  def __str__(self):
    packages = list()
    for detail in self.note.vulnerability.details:
      packages.append((detail.package, detail.min_affected_version.name))

    return "[name={},packages={}]".format(self.name, packages)
