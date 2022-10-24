# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ostorlab/agent/message/proto/v3/scan/file/android.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='ostorlab/agent/message/proto/v3/scan/file/android.proto',
  package='ostorlab.agent.message.proto.v3.scan.file',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n7ostorlab/agent/message/proto/v3/scan/file/android.proto\x12)ostorlab.agent.message.proto.v3.scan.file\"Q\n\x07\x61ndroid\x12\x0f\n\x07scan_id\x18\x01 \x01(\x05\x12\x0c\n\x04\x66ile\x18\x02 \x01(\x0c\x12\x0c\n\x04hash\x18\x03 \x01(\t\x12\x19\n\x08platform\x18\x04 \x01(\t:\x07\x61ndroid'
)




_ANDROID = _descriptor.Descriptor(
  name='android',
  full_name='ostorlab.agent.message.proto.v3.scan.file.android',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='scan_id', full_name='ostorlab.agent.message.proto.v3.scan.file.android.scan_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='file', full_name='ostorlab.agent.message.proto.v3.scan.file.android.file', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='hash', full_name='ostorlab.agent.message.proto.v3.scan.file.android.hash', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='platform', full_name='ostorlab.agent.message.proto.v3.scan.file.android.platform', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=b"android".decode('utf-8'),
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=102,
  serialized_end=183,
)

DESCRIPTOR.message_types_by_name['android'] = _ANDROID
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

android = _reflection.GeneratedProtocolMessageType('android', (_message.Message,), {
  'DESCRIPTOR' : _ANDROID,
  '__module__' : 'ostorlab.agent.message.proto.v3.scan.file.android_pb2'
  # @@protoc_insertion_point(class_scope:ostorlab.agent.message.proto.v3.scan.file.android)
  })
_sym_db.RegisterMessage(android)


# @@protoc_insertion_point(module_scope)
