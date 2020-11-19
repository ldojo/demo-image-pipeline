# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/v1beta1/image.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/v1beta1/image.proto',
  package='grafeas.v1beta1.image',
  syntax='proto3',
  serialized_options=b'\n\030io.grafeas.v1beta1.imageP\001Z7github.com/grafeas/grafeas/proto/v1beta1/image_go_proto\242\002\003GRA',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x19proto/v1beta1/image.proto\x12\x15grafeas.v1beta1.image\"\xc8\x02\n\x05Layer\x12\x39\n\tdirective\x18\x01 \x01(\x0e\x32&.grafeas.v1beta1.image.Layer.Directive\x12\x11\n\targuments\x18\x02 \x01(\t\"\xf0\x01\n\tDirective\x12\x19\n\x15\x44IRECTIVE_UNSPECIFIED\x10\x00\x12\x0e\n\nMAINTAINER\x10\x01\x12\x07\n\x03RUN\x10\x02\x12\x07\n\x03\x43MD\x10\x03\x12\t\n\x05LABEL\x10\x04\x12\n\n\x06\x45XPOSE\x10\x05\x12\x07\n\x03\x45NV\x10\x06\x12\x07\n\x03\x41\x44\x44\x10\x07\x12\x08\n\x04\x43OPY\x10\x08\x12\x0e\n\nENTRYPOINT\x10\t\x12\n\n\x06VOLUME\x10\n\x12\x08\n\x04USER\x10\x0b\x12\x0b\n\x07WORKDIR\x10\x0c\x12\x07\n\x03\x41RG\x10\r\x12\x0b\n\x07ONBUILD\x10\x0e\x12\x0e\n\nSTOPSIGNAL\x10\x0f\x12\x0f\n\x0bHEALTHCHECK\x10\x10\x12\t\n\x05SHELL\x10\x11\"@\n\x0b\x46ingerprint\x12\x0f\n\x07v1_name\x18\x01 \x01(\t\x12\x0f\n\x07v2_blob\x18\x02 \x03(\t\x12\x0f\n\x07v2_name\x18\x03 \x01(\t\"V\n\x05\x42\x61sis\x12\x14\n\x0cresource_url\x18\x01 \x01(\t\x12\x37\n\x0b\x66ingerprint\x18\x02 \x01(\x0b\x32\".grafeas.v1beta1.image.Fingerprint\"@\n\x07\x44\x65tails\x12\x35\n\rderived_image\x18\x01 \x01(\x0b\x32\x1e.grafeas.v1beta1.image.Derived\"\xa1\x01\n\x07\x44\x65rived\x12\x37\n\x0b\x66ingerprint\x18\x01 \x01(\x0b\x32\".grafeas.v1beta1.image.Fingerprint\x12\x10\n\x08\x64istance\x18\x02 \x01(\x05\x12\x30\n\nlayer_info\x18\x03 \x03(\x0b\x32\x1c.grafeas.v1beta1.image.Layer\x12\x19\n\x11\x62\x61se_resource_url\x18\x04 \x01(\tB[\n\x18io.grafeas.v1beta1.imageP\x01Z7github.com/grafeas/grafeas/proto/v1beta1/image_go_proto\xa2\x02\x03GRAb\x06proto3'
)



_LAYER_DIRECTIVE = _descriptor.EnumDescriptor(
  name='Directive',
  full_name='grafeas.v1beta1.image.Layer.Directive',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DIRECTIVE_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MAINTAINER', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RUN', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CMD', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LABEL', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='EXPOSE', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ENV', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ADD', index=7, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='COPY', index=8, number=8,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ENTRYPOINT', index=9, number=9,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='VOLUME', index=10, number=10,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='USER', index=11, number=11,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='WORKDIR', index=12, number=12,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ARG', index=13, number=13,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ONBUILD', index=14, number=14,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='STOPSIGNAL', index=15, number=15,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='HEALTHCHECK', index=16, number=16,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SHELL', index=17, number=17,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=141,
  serialized_end=381,
)
_sym_db.RegisterEnumDescriptor(_LAYER_DIRECTIVE)


_LAYER = _descriptor.Descriptor(
  name='Layer',
  full_name='grafeas.v1beta1.image.Layer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='directive', full_name='grafeas.v1beta1.image.Layer.directive', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='arguments', full_name='grafeas.v1beta1.image.Layer.arguments', index=1,
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
    _LAYER_DIRECTIVE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=53,
  serialized_end=381,
)


_FINGERPRINT = _descriptor.Descriptor(
  name='Fingerprint',
  full_name='grafeas.v1beta1.image.Fingerprint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='v1_name', full_name='grafeas.v1beta1.image.Fingerprint.v1_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='v2_blob', full_name='grafeas.v1beta1.image.Fingerprint.v2_blob', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='v2_name', full_name='grafeas.v1beta1.image.Fingerprint.v2_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=383,
  serialized_end=447,
)


_BASIS = _descriptor.Descriptor(
  name='Basis',
  full_name='grafeas.v1beta1.image.Basis',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_url', full_name='grafeas.v1beta1.image.Basis.resource_url', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='fingerprint', full_name='grafeas.v1beta1.image.Basis.fingerprint', index=1,
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
  serialized_start=449,
  serialized_end=535,
)


_DETAILS = _descriptor.Descriptor(
  name='Details',
  full_name='grafeas.v1beta1.image.Details',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='derived_image', full_name='grafeas.v1beta1.image.Details.derived_image', index=0,
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
  serialized_start=537,
  serialized_end=601,
)


_DERIVED = _descriptor.Descriptor(
  name='Derived',
  full_name='grafeas.v1beta1.image.Derived',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='fingerprint', full_name='grafeas.v1beta1.image.Derived.fingerprint', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='distance', full_name='grafeas.v1beta1.image.Derived.distance', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='layer_info', full_name='grafeas.v1beta1.image.Derived.layer_info', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='base_resource_url', full_name='grafeas.v1beta1.image.Derived.base_resource_url', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=604,
  serialized_end=765,
)

_LAYER.fields_by_name['directive'].enum_type = _LAYER_DIRECTIVE
_LAYER_DIRECTIVE.containing_type = _LAYER
_BASIS.fields_by_name['fingerprint'].message_type = _FINGERPRINT
_DETAILS.fields_by_name['derived_image'].message_type = _DERIVED
_DERIVED.fields_by_name['fingerprint'].message_type = _FINGERPRINT
_DERIVED.fields_by_name['layer_info'].message_type = _LAYER
DESCRIPTOR.message_types_by_name['Layer'] = _LAYER
DESCRIPTOR.message_types_by_name['Fingerprint'] = _FINGERPRINT
DESCRIPTOR.message_types_by_name['Basis'] = _BASIS
DESCRIPTOR.message_types_by_name['Details'] = _DETAILS
DESCRIPTOR.message_types_by_name['Derived'] = _DERIVED
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Layer = _reflection.GeneratedProtocolMessageType('Layer', (_message.Message,), {
  'DESCRIPTOR' : _LAYER,
  '__module__' : 'proto.v1beta1.image_pb2'
  # @@protoc_insertion_point(class_scope:grafeas.v1beta1.image.Layer)
  })
_sym_db.RegisterMessage(Layer)

Fingerprint = _reflection.GeneratedProtocolMessageType('Fingerprint', (_message.Message,), {
  'DESCRIPTOR' : _FINGERPRINT,
  '__module__' : 'proto.v1beta1.image_pb2'
  # @@protoc_insertion_point(class_scope:grafeas.v1beta1.image.Fingerprint)
  })
_sym_db.RegisterMessage(Fingerprint)

Basis = _reflection.GeneratedProtocolMessageType('Basis', (_message.Message,), {
  'DESCRIPTOR' : _BASIS,
  '__module__' : 'proto.v1beta1.image_pb2'
  # @@protoc_insertion_point(class_scope:grafeas.v1beta1.image.Basis)
  })
_sym_db.RegisterMessage(Basis)

Details = _reflection.GeneratedProtocolMessageType('Details', (_message.Message,), {
  'DESCRIPTOR' : _DETAILS,
  '__module__' : 'proto.v1beta1.image_pb2'
  # @@protoc_insertion_point(class_scope:grafeas.v1beta1.image.Details)
  })
_sym_db.RegisterMessage(Details)

Derived = _reflection.GeneratedProtocolMessageType('Derived', (_message.Message,), {
  'DESCRIPTOR' : _DERIVED,
  '__module__' : 'proto.v1beta1.image_pb2'
  # @@protoc_insertion_point(class_scope:grafeas.v1beta1.image.Derived)
  })
_sym_db.RegisterMessage(Derived)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
