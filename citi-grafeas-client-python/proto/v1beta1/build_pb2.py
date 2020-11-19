# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/v1beta1/build.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from proto.v1beta1 import provenance_pb2 as proto_dot_v1beta1_dot_provenance__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/v1beta1/build.proto',
  package='grafeas.v1beta1.build',
  syntax='proto3',
  serialized_options=b'\n\030io.grafeas.v1beta1.buildP\001Z7github.com/grafeas/grafeas/proto/v1beta1/build_go_proto\242\002\003GRA',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x19proto/v1beta1/build.proto\x12\x15grafeas.v1beta1.build\x1a\x1eproto/v1beta1/provenance.proto\"Z\n\x05\x42uild\x12\x17\n\x0f\x62uilder_version\x18\x01 \x01(\t\x12\x38\n\tsignature\x18\x02 \x01(\x0b\x32%.grafeas.v1beta1.build.BuildSignature\"\xd2\x01\n\x0e\x42uildSignature\x12\x12\n\npublic_key\x18\x01 \x01(\t\x12\x11\n\tsignature\x18\x02 \x01(\x0c\x12\x0e\n\x06key_id\x18\x03 \x01(\t\x12?\n\x08key_type\x18\x04 \x01(\x0e\x32-.grafeas.v1beta1.build.BuildSignature.KeyType\"H\n\x07KeyType\x12\x18\n\x14KEY_TYPE_UNSPECIFIED\x10\x00\x12\x15\n\x11PGP_ASCII_ARMORED\x10\x01\x12\x0c\n\x08PKIX_PEM\x10\x02\"d\n\x07\x44\x65tails\x12?\n\nprovenance\x18\x01 \x01(\x0b\x32+.grafeas.v1beta1.provenance.BuildProvenance\x12\x18\n\x10provenance_bytes\x18\x02 \x01(\tB[\n\x18io.grafeas.v1beta1.buildP\x01Z7github.com/grafeas/grafeas/proto/v1beta1/build_go_proto\xa2\x02\x03GRAb\x06proto3'
  ,
  dependencies=[proto_dot_v1beta1_dot_provenance__pb2.DESCRIPTOR,])



_BUILDSIGNATURE_KEYTYPE = _descriptor.EnumDescriptor(
  name='KeyType',
  full_name='grafeas.v1beta1.build.BuildSignature.KeyType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='KEY_TYPE_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PGP_ASCII_ARMORED', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PKIX_PEM', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=315,
  serialized_end=387,
)
_sym_db.RegisterEnumDescriptor(_BUILDSIGNATURE_KEYTYPE)


_BUILD = _descriptor.Descriptor(
  name='Build',
  full_name='grafeas.v1beta1.build.Build',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='builder_version', full_name='grafeas.v1beta1.build.Build.builder_version', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='signature', full_name='grafeas.v1beta1.build.Build.signature', index=1,
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
  ],
  serialized_start=84,
  serialized_end=174,
)


_BUILDSIGNATURE = _descriptor.Descriptor(
  name='BuildSignature',
  full_name='grafeas.v1beta1.build.BuildSignature',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='public_key', full_name='grafeas.v1beta1.build.BuildSignature.public_key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='signature', full_name='grafeas.v1beta1.build.BuildSignature.signature', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='key_id', full_name='grafeas.v1beta1.build.BuildSignature.key_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='key_type', full_name='grafeas.v1beta1.build.BuildSignature.key_type', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _BUILDSIGNATURE_KEYTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=177,
  serialized_end=387,
)


_DETAILS = _descriptor.Descriptor(
  name='Details',
  full_name='grafeas.v1beta1.build.Details',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='provenance', full_name='grafeas.v1beta1.build.Details.provenance', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='provenance_bytes', full_name='grafeas.v1beta1.build.Details.provenance_bytes', index=1,
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
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=389,
  serialized_end=489,
)

_BUILD.fields_by_name['signature'].message_type = _BUILDSIGNATURE
_BUILDSIGNATURE.fields_by_name['key_type'].enum_type = _BUILDSIGNATURE_KEYTYPE
_BUILDSIGNATURE_KEYTYPE.containing_type = _BUILDSIGNATURE
_DETAILS.fields_by_name['provenance'].message_type = proto_dot_v1beta1_dot_provenance__pb2._BUILDPROVENANCE
DESCRIPTOR.message_types_by_name['Build'] = _BUILD
DESCRIPTOR.message_types_by_name['BuildSignature'] = _BUILDSIGNATURE
DESCRIPTOR.message_types_by_name['Details'] = _DETAILS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Build = _reflection.GeneratedProtocolMessageType('Build', (_message.Message,), {
  'DESCRIPTOR' : _BUILD,
  '__module__' : 'proto.v1beta1.build_pb2'
  # @@protoc_insertion_point(class_scope:grafeas.v1beta1.build.Build)
  })
_sym_db.RegisterMessage(Build)

BuildSignature = _reflection.GeneratedProtocolMessageType('BuildSignature', (_message.Message,), {
  'DESCRIPTOR' : _BUILDSIGNATURE,
  '__module__' : 'proto.v1beta1.build_pb2'
  # @@protoc_insertion_point(class_scope:grafeas.v1beta1.build.BuildSignature)
  })
_sym_db.RegisterMessage(BuildSignature)

Details = _reflection.GeneratedProtocolMessageType('Details', (_message.Message,), {
  'DESCRIPTOR' : _DETAILS,
  '__module__' : 'proto.v1beta1.build_pb2'
  # @@protoc_insertion_point(class_scope:grafeas.v1beta1.build.Details)
  })
_sym_db.RegisterMessage(Details)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
