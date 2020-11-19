"""Provides utility classes for managing Occurrences to submit to Grafeas"""

import logging
from proto.v1beta1.vulnerability_pb2 import Severity
from proto.v1beta1.grafeas_pb2 import Occurrence as GrafeasOccurrence
from schemas.notes import Note, VulnerabilityNote


class Occurrence():
  """Base class to manage and wrap Occurrence types for Grafeas"""
  def __init__(self, resource: str, note: Note, name: str = None):
    self.name = name
    self.resource = resource
    self.note = note
    self.occurrence = GrafeasOccurrence()

class VulnerabilityOccurrence(Occurrence):
  RESOURCE_URI = 'uri'
  RESOURCE_OPERATOR_DETAILS = 'operator_details'
  """Derived class to manage Vulnerability-specific Occurrences for Grafeas"""
  def __init__(self, resource: dict, note: VulnerabilityNote):
    """
    Constructor

    :param resource: dict with 'uri' (str) and 'operator_details' (list)
    :param note: Note that is linked to this Occurrence
    """
    super().__init__(resource, note)
    logging.debug('Note name: %s', note.note.name)
    self.occurrence.note_name = note.note.name
    self.occurrence.kind = note.note.kind
    logging.debug(type(note.note.vulnerability.details))
    details = note.note.vulnerability.details[0]
    logging.debug('Details: %s', type(details))
    # CopyFrom(note.note.vulnerability.details) doesn't work for some reason
    # details class shows up as google.protobuf.pyext._message.RepeatedCompositeContainer instead of Details
    # Error below
    # TypeError: Parameter to CopyFrom() must be instance of same class:
    # expected grafeas.v1beta1.vulnerability.Details got google.protobuf.pyext._message.RepeatedCompositeContainer.

    #self.occurrence.vulnerability.CopyFrom(note.note.vulnerability.details)
    self.occurrence.vulnerability.type = details.package_type
    self.occurrence.vulnerability.severity = Severity.Value(details.severity_name)
    self.occurrence.vulnerability.effective_severity = Severity.Value(details.severity_name)
    self.occurrence.resource.uri = resource[VulnerabilityOccurrence.RESOURCE_URI]

    # If it's None, then this may not be an operator image so skip this.
    if resource[VulnerabilityOccurrence.RESOURCE_OPERATOR_DETAILS] is not None:
      for operator_detail in resource[VulnerabilityOccurrence.RESOURCE_OPERATOR_DETAILS]:
        operator_details = self.occurrence.resource.operator_details.operators.add()
        operator_details.name = operator_detail['operatorName']
        operator_details.version = operator_detail['version']
    package_issue = self.occurrence.vulnerability.package_issue.add()
    package_issue.affected_location.cpe_uri = details.cpe_uri
    package_issue.affected_location.package = details.package
    package_issue.affected_location.version.CopyFrom(details.min_affected_version)


  @staticmethod
  def create_vulnerability_occurrence(resource: dict, vul_note: VulnerabilityNote):
    """
    Static method used to generate a vulnerability occurrence

    :param resource: dict with 'uri' (str) and 'operator_details' (list)
    :param note: Note that is linked to this Occurrence

    :returns: a new VulnerabilityOccurrence
    """
    return VulnerabilityOccurrence(resource, vul_note)
