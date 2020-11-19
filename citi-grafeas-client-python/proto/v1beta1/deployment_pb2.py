# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/v1beta1/deployment.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/v1beta1/deployment.proto',
  package='grafeas.v1beta1.deployment',
  syntax='proto3',
  serialized_options=b'\n\035io.grafeas.v1beta1.deploymentP\001Z<github.com/grafeas/grafeas/proto/v1beta1/deployment_go_proto\242\002\003GRA',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1eproto/v1beta1/deployment.proto\x12\x1agrafeas.v1beta1.deployment\x1a\x1fgoogle/protobuf/timestamp.proto\"\"\n\nDeployable\x12\x14\n\x0cresource_uri\x18\x01 \x03(\t\"E\n\x07\x44\x65tails\x12:\n\ndeployment\x18\x01 \x01(\x0b\x32&.grafeas.v1beta1.deployment.Deployment\"\xc3\x02\n\nDeployment\x12\x12\n\nuser_email\x18\x01 \x01(\t\x12/\n\x0b\x64\x65ploy_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x31\n\rundeploy_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0e\n\x06\x63onfig\x18\x04 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x05 \x01(\t\x12\x14\n\x0cresource_uri\x18\x06 \x03(\t\x12\x41\n\x08platform\x18\x07 \x01(\x0e\x32/.grafeas.v1beta1.deployment.Deployment.Platform\"C\n\x08Platform\x12\x18\n\x14PLATFORM_UNSPECIFIED\x10\x00\x12\x07\n\x03GKE\x10\x01\x12\x08\n\x04\x46LEX\x10\x02\x12\n\n\x06\x43USTOM\x10\x03\x42\x65\n\x1dio.grafeas.v1beta1.deploymentP\x01Z<github.com/grafeas/grafeas/proto/v1beta1/deployment_go_proto\xa2\x02\x03GRAb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])



_DEPLOYMENT_PLATFORM = _descriptor.EnumDescriptor(
  name='Platform',
  full_name='grafeas.v1beta1.deployment.Deployment.Platform',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PLATFORM_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GKE', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FLEX', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CUSTOM', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=459,
  serialized_end=526,
)
_sym_db.RegisterEnumDescriptor(_DEPLOYMENT_PLATFORM)


_DEPLOYABLE = _descriptor.Descriptor(
  name='Deployable',
  full_name='grafeas.v1beta1.deployment.Deployable',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_uri', full_name='grafeas.v1beta1.deployment.Deployable.resource_uri', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=95,
  serialized_end=129,
)


_DETAILS = _descriptor.Descriptor(
  name='Details',
  full_name='grafeas.v1beta1.deployment.Details',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='deployment', full_name='grafeas.v1beta1.deployment.Details.deployment', index=0,
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
  serialized_start=131,
  serialized_end=200,
)


_DEPLOYMENT = _descriptor.Descriptor(
  name='Deployment',
  full_name='grafeas.v1beta1.deployment.Deployment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_email', full_name='grafeas.v1beta1.deployment.Deployment.user_email', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='deploy_time', full_name='grafeas.v1beta1.deployment.Deployment.deploy_time', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='undeploy_time', full_name='grafeas.v1beta1.deployment.Deployment.undeploy_time', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='config', full_name='grafeas.v1beta1.deployment.Deployment.config', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='address', full_name='grafeas.v1beta1.deployment.Deployment.address', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='resource_uri', full_name='grafeas.v1beta1.deployment.Deployment.resource_uri', index=5,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='platform', full_name='grafeas.v1beta1.deployment.Deployment.platform', index=6,
      number=7, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _DEPLOYMENT_PLATFORM,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=203,
  serialized_end=526,
)

_DETAILS.fields_by_name['deployment'].message_type = _DEPLOYMENT
_DEPLOYMENT.fields_by_name['deploy_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_DEPLOYMENT.fields_by_name['undeploy_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_DEPLOYMENT.fields_by_name['platform'].enum_type = _DEPLOYMENT_PLATFORM
_DEPLOYMENT_PLATFORM.containing_type = _DEPLOYMENT
DESCRIPTOR.message_types_by_name['Deployable'] = _DEPLOYABLE
DESCRIPTOR.message_types_by_name['Details'] = _DETAILS
DESCRIPTOR.message_types_by_name['Deployment'] = _DEPLOYMENT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Deployable = _reflection.GeneratedProtocolMessageType('Deployable', (_message.Message,), {
  'DESCRIPTOR' : _DEPLOYABLE,
  '__module__' : 'proto.v1beta1.deployment_pb2'
  # @@protoc_insertion_point(class_scope:grafeas.v1beta1.deployment.Deployable)
  })
_sym_db.RegisterMessage(Deployable)

Details = _reflection.GeneratedProtocolMessageType('Details', (_message.Message,), {
  'DESCRIPTOR' : _DETAILS,
  '__module__' : 'proto.v1beta1.deployment_pb2'
  # @@protoc_insertion_point(class_scope:grafeas.v1beta1.deployment.Details)
  })
_sym_db.RegisterMessage(Details)

Deployment = _reflection.GeneratedProtocolMessageType('Deployment', (_message.Message,), {
  'DESCRIPTOR' : _DEPLOYMENT,
  '__module__' : 'proto.v1beta1.deployment_pb2'
  # @@protoc_insertion_point(class_scope:grafeas.v1beta1.deployment.Deployment)
  })
_sym_db.RegisterMessage(Deployment)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
