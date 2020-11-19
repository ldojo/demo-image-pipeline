# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/v1beta1/attestation.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from proto.v1beta1 import common_pb2 as proto_dot_v1beta1_dot_common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/v1beta1/attestation.proto',
  package='grafeas.v1beta1.attestation',
  syntax='proto3',
  serialized_options=b'\n\036io.grafeas.v1beta1.attestationP\001Z=github.com/grafeas/grafeas/proto/v1beta1/attestation_go_proto\242\002\003GRA',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1fproto/v1beta1/attestation.proto\x12\x1bgrafeas.v1beta1.attestation\x1a\x1aproto/v1beta1/common.proto\"\xe4\x01\n\x14PgpSignedAttestation\x12\x11\n\tsignature\x18\x01 \x01(\t\x12S\n\x0c\x63ontent_type\x18\x03 \x01(\x0e\x32=.grafeas.v1beta1.attestation.PgpSignedAttestation.ContentType\x12\x14\n\npgp_key_id\x18\x02 \x01(\tH\x00\"D\n\x0b\x43ontentType\x12\x1c\n\x18\x43ONTENT_TYPE_UNSPECIFIED\x10\x00\x12\x17\n\x13SIMPLE_SIGNING_JSON\x10\x01\x42\x08\n\x06key_id\"\x85\x02\n\x18GenericSignedAttestation\x12W\n\x0c\x63ontent_type\x18\x01 \x01(\x0e\x32\x41.grafeas.v1beta1.attestation.GenericSignedAttestation.ContentType\x12\x1a\n\x12serialized_payload\x18\x02 \x01(\x0c\x12.\n\nsignatures\x18\x03 \x03(\x0b\x32\x1a.grafeas.v1beta1.Signature\"D\n\x0b\x43ontentType\x12\x1c\n\x18\x43ONTENT_TYPE_UNSPECIFIED\x10\x00\x12\x17\n\x13SIMPLE_SIGNING_JSON\x10\x01\"k\n\tAuthority\x12\x39\n\x04hint\x18\x01 \x01(\x0b\x32+.grafeas.v1beta1.attestation.Authority.Hint\x1a#\n\x04Hint\x12\x1b\n\x13human_readable_name\x18\x01 \x01(\t\"H\n\x07\x44\x65tails\x12=\n\x0b\x61ttestation\x18\x01 \x01(\x0b\x32(.grafeas.v1beta1.attestation.Attestation\"\xcc\x01\n\x0b\x41ttestation\x12S\n\x16pgp_signed_attestation\x18\x01 \x01(\x0b\x32\x31.grafeas.v1beta1.attestation.PgpSignedAttestationH\x00\x12[\n\x1ageneric_signed_attestation\x18\x02 \x01(\x0b\x32\x35.grafeas.v1beta1.attestation.GenericSignedAttestationH\x00\x42\x0b\n\tsignatureBg\n\x1eio.grafeas.v1beta1.attestationP\x01Z=github.com/grafeas/grafeas/proto/v1beta1/attestation_go_proto\xa2\x02\x03GRAb\x06proto3'
  ,
  dependencies=[proto_dot_v1beta1_dot_common__pb2.DESCRIPTOR,])



_PGPSIGNEDATTESTATION_CONTENTTYPE = _descriptor.EnumDescriptor(
  name='ContentType',
  full_name='grafeas.v1beta1.attestation.PgpSignedAttestation.ContentType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CONTENT_TYPE_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SIMPLE_SIGNING_JSON', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=243,
  serialized_end=311,
)
_sym_db.RegisterEnumDescriptor(_PGPSIGNEDATTESTATION_CONTENTTYPE)

_GENERICSIGNEDATTESTATION_CONTENTTYPE = _descriptor.EnumDescriptor(
  name='ContentType',
  full_name='grafeas.v1beta1.attestation.GenericSignedAttestation.ContentType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CONTENT_TYPE_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SIMPLE_SIGNING_JSON', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=243,
  serialized_end=311,
)
_sym_db.RegisterEnumDescriptor(_GENERICSIGNEDATTESTATION_CONTENTTYPE)


_PGPSIGNEDATTESTATION = _descriptor.Descriptor(
  name='PgpSignedAttestation',
  full_name='grafeas.v1beta1.attestation.PgpSignedAttestation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='signature', full_name='grafeas.v1beta1.attestation.PgpSignedAttestation.signature', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='content_type', full_name='grafeas.v1beta1.attestation.PgpSignedAttestation.content_type', index=1,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pgp_key_id', full_name='grafeas.v1beta1.attestation.PgpSignedAttestation.pgp_key_id', index=2,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PGPSIGNEDATTESTATION_CONTENTTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='key_id', full_name='grafeas.v1beta1.attestation.PgpSignedAttestation.key_id',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=93,
  serialized_end=321,
)


_GENERICSIGNEDATTESTATION = _descriptor.Descriptor(
  name='GenericSignedAttestation',
  full_name='grafeas.v1beta1.attestation.GenericSignedAttestation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='content_type', full_name='grafeas.v1beta1.attestation.GenericSignedAttestation.content_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='serialized_payload', full_name='grafeas.v1beta1.attestation.GenericSignedAttestation.serialized_payload', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='signatures', full_name='grafeas.v1beta1.attestation.GenericSignedAttestation.signatures', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _GENERICSIGNEDATTESTATION_CONTENTTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=324,
  serialized_end=585,
)


_AUTHORITY_HINT = _descriptor.Descriptor(
  name='Hint',
  full_name='grafeas.v1beta1.attestation.Authority.Hint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='human_readable_name', full_name='grafeas.v1beta1.attestation.Authority.Hint.human_readable_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=659,
  serialized_end=694,
)

_AUTHORITY = _descriptor.Descriptor(
  name='Authority',
  full_name='grafeas.v1beta1.attestation.Authority',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='hint', full_name='grafeas.v1beta1.attestation.Authority.hint', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_AUTHORITY_HINT, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=587,
  serialized_end=694,
)


_DETAILS = _descriptor.Descriptor(
  name='Details',
  full_name='grafeas.v1beta1.attestation.Details',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='attestation', full_name='grafeas.v1beta1.attestation.Details.attestation', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=696,
  serialized_end=768,
)


_ATTESTATION = _descriptor.Descriptor(
  name='Attestation',
  full_name='grafeas.v1beta1.attestation.Attestation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='pgp_signed_attestation', full_name='grafeas.v1beta1.attestation.Attestation.pgp_signed_attestation', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='generic_signed_attestation', full_name='grafeas.v1beta1.attestation.Attestation.generic_signed_attestation', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='signature', full_name='grafeas.v1beta1.attestation.Attestation.signature',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=771,
  serialized_end=975,
)

_PGPSIGNEDATTESTATION.fields_by_name['content_type'].enum_type = _PGPSIGNEDATTESTATION_CONTENTTYPE
_PGPSIGNEDATTESTATION_CONTENTTYPE.containing_type = _PGPSIGNEDATTESTATION
_PGPSIGNEDATTESTATION.oneofs_by_name['key_id'].fields.append(
  _PGPSIGNEDATTESTATION.fields_by_name['pgp_key_id'])
_PGPSIGNEDATTESTATION.fields_by_name['pgp_key_id'].containing_oneof = _PGPSIGNEDATTESTATION.oneofs_by_name['key_id']
_GENERICSIGNEDATTESTATION.fields_by_name['content_type'].enum_type = _GENERICSIGNEDATTESTATION_CONTENTTYPE
_GENERICSIGNEDATTESTATION.fields_by_name['signatures'].message_type = proto_dot_v1beta1_dot_common__pb2._SIGNATURE
_GENERICSIGNEDATTESTATION_CONTENTTYPE.containing_type = _GENERICSIGNEDATTESTATION
_AUTHORITY_HINT.containing_type = _AUTHORITY
_AUTHORITY.fields_by_name['hint'].message_type = _AUTHORITY_HINT
_DETAILS.fields_by_name['attestation'].message_type = _ATTESTATION
_ATTESTATION.fields_by_name['pgp_signed_attestation'].message_type = _PGPSIGNEDATTESTATION
_ATTESTATION.fields_by_name['generic_signed_attestation'].message_type = _GENERICSIGNEDATTESTATION
_ATTESTATION.oneofs_by_name['signature'].fields.append(
  _ATTESTATION.fields_by_name['pgp_signed_attestation'])
_ATTESTATION.fields_by_name['pgp_signed_attestation'].containing_oneof = _ATTESTATION.oneofs_by_name['signature']
_ATTESTATION.oneofs_by_name['signature'].fields.append(
  _ATTESTATION.fields_by_name['generic_signed_attestation'])
_ATTESTATION.fields_by_name['generic_signed_attestation'].containing_oneof = _ATTESTATION.oneofs_by_name['signature']
DESCRIPTOR.message_types_by_name['PgpSignedAttestation'] = _PGPSIGNEDATTESTATION
DESCRIPTOR.message_types_by_name['GenericSignedAttestation'] = _GENERICSIGNEDATTESTATION
DESCRIPTOR.message_types_by_name['Authority'] = _AUTHORITY
DESCRIPTOR.message_types_by_name['Details'] = _DETAILS
DESCRIPTOR.message_types_by_name['Attestation'] = _ATTESTATION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PgpSignedAttestation = _reflection.GeneratedProtocolMessageType('PgpSignedAttestation', (_message.Message,), {
  'DESCRIPTOR' : _PGPSIGNEDATTESTATION,
  '__module__' : 'proto.v1beta1.attestation_pb2'
  # @@protoc_insertion_point(class_scope:grafeas.v1beta1.attestation.PgpSignedAttestation)
  })
_sym_db.RegisterMessage(PgpSignedAttestation)

GenericSignedAttestation = _reflection.GeneratedProtocolMessageType('GenericSignedAttestation', (_message.Message,), {
  'DESCRIPTOR' : _GENERICSIGNEDATTESTATION,
  '__module__' : 'proto.v1beta1.attestation_pb2'
  # @@protoc_insertion_point(class_scope:grafeas.v1beta1.attestation.GenericSignedAttestation)
  })
_sym_db.RegisterMessage(GenericSignedAttestation)

Authority = _reflection.GeneratedProtocolMessageType('Authority', (_message.Message,), {

  'Hint' : _reflection.GeneratedProtocolMessageType('Hint', (_message.Message,), {
    'DESCRIPTOR' : _AUTHORITY_HINT,
    '__module__' : 'proto.v1beta1.attestation_pb2'
    # @@protoc_insertion_point(class_scope:grafeas.v1beta1.attestation.Authority.Hint)
    })
  ,
  'DESCRIPTOR' : _AUTHORITY,
  '__module__' : 'proto.v1beta1.attestation_pb2'
  # @@protoc_insertion_point(class_scope:grafeas.v1beta1.attestation.Authority)
  })
_sym_db.RegisterMessage(Authority)
_sym_db.RegisterMessage(Authority.Hint)

Details = _reflection.GeneratedProtocolMessageType('Details', (_message.Message,), {
  'DESCRIPTOR' : _DETAILS,
  '__module__' : 'proto.v1beta1.attestation_pb2'
  # @@protoc_insertion_point(class_scope:grafeas.v1beta1.attestation.Details)
  })
_sym_db.RegisterMessage(Details)

Attestation = _reflection.GeneratedProtocolMessageType('Attestation', (_message.Message,), {
  'DESCRIPTOR' : _ATTESTATION,
  '__module__' : 'proto.v1beta1.attestation_pb2'
  # @@protoc_insertion_point(class_scope:grafeas.v1beta1.attestation.Attestation)
  })
_sym_db.RegisterMessage(Attestation)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)