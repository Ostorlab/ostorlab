# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v3/asset/file/android/apk/apk.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='v3/asset/file/android/apk/apk.proto',
  package='v3.asset.file.android.apk',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n#v3/asset/file/android/apk/apk.proto\x12\x19v3.asset.file.android.apk\"(\n\x07Message\x12\x0f\n\x07\x63ontent\x18\x01 \x01(\x0c\x12\x0c\n\x04path\x18\x02 \x01(\t')
)




_MESSAGE = _descriptor.Descriptor(
  name='Message',
  full_name='v3.asset.file.android.apk.Message',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='content', full_name='v3.asset.file.android.apk.Message.content', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='path', full_name='v3.asset.file.android.apk.Message.path', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=66,
  serialized_end=106,
)

DESCRIPTOR.message_types_by_name['Message'] = _MESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Message = _reflection.GeneratedProtocolMessageType('Message', (_message.Message,), dict(
  DESCRIPTOR = _MESSAGE,
  __module__ = 'v3.asset.file.android.apk.apk_pb2'
  # @@protoc_insertion_point(class_scope:v3.asset.file.android.apk.Message)
  ))
_sym_db.RegisterMessage(Message)


# @@protoc_insertion_point(module_scope)
