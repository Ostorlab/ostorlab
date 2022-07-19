# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v3/capture/request_response/request_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='v3/capture/request_response/request_response.proto',
  package='v3.capture.request_response',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n2v3/capture/request_response/request_response.proto\x12\x1bv3.capture.request_response\"%\n\x06header\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"j\n\x07request\x12\x0e\n\x06method\x18\x01 \x01(\t\x12\x0b\n\x03url\x18\x02 \x01(\t\x12\x34\n\x07headers\x18\x03 \x03(\x0b\x32#.v3.capture.request_response.header\x12\x0c\n\x04\x62ody\x18\x04 \x01(\x0c\"\xba\x01\n\x08response\x12\x0b\n\x03url\x18\x01 \x01(\t\x12\x0e\n\x06status\x18\x02 \x01(\x05\x12\x13\n\x0bstatus_text\x18\x03 \x01(\t\x12\x34\n\x07headers\x18\x04 \x03(\x0b\x32#.v3.capture.request_response.header\x12\x11\n\tremote_ip\x18\x05 \x01(\t\x12\x13\n\x0bremote_port\x18\x06 \x01(\x05\x12\x10\n\x08protocol\x18\x07 \x01(\t\x12\x0c\n\x04\x62ody\x18\x08 \x01(\x0c\"y\n\x07Message\x12\x35\n\x07request\x18\x01 \x01(\x0b\x32$.v3.capture.request_response.request\x12\x37\n\x08response\x18\x02 \x01(\x0b\x32%.v3.capture.request_response.response')
)




_HEADER = _descriptor.Descriptor(
  name='header',
  full_name='v3.capture.request_response.header',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='v3.capture.request_response.header.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='v3.capture.request_response.header.value', index=1,
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
  serialized_start=83,
  serialized_end=120,
)


_REQUEST = _descriptor.Descriptor(
  name='request',
  full_name='v3.capture.request_response.request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='method', full_name='v3.capture.request_response.request.method', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='url', full_name='v3.capture.request_response.request.url', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='headers', full_name='v3.capture.request_response.request.headers', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='body', full_name='v3.capture.request_response.request.body', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=122,
  serialized_end=228,
)


_RESPONSE = _descriptor.Descriptor(
  name='response',
  full_name='v3.capture.request_response.response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='url', full_name='v3.capture.request_response.response.url', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='v3.capture.request_response.response.status', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status_text', full_name='v3.capture.request_response.response.status_text', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='headers', full_name='v3.capture.request_response.response.headers', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='remote_ip', full_name='v3.capture.request_response.response.remote_ip', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='remote_port', full_name='v3.capture.request_response.response.remote_port', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='protocol', full_name='v3.capture.request_response.response.protocol', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='body', full_name='v3.capture.request_response.response.body', index=7,
      number=8, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=231,
  serialized_end=417,
)


_MESSAGE = _descriptor.Descriptor(
  name='Message',
  full_name='v3.capture.request_response.Message',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='request', full_name='v3.capture.request_response.Message.request', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='response', full_name='v3.capture.request_response.Message.response', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=419,
  serialized_end=540,
)

_REQUEST.fields_by_name['headers'].message_type = _HEADER
_RESPONSE.fields_by_name['headers'].message_type = _HEADER
_MESSAGE.fields_by_name['request'].message_type = _REQUEST
_MESSAGE.fields_by_name['response'].message_type = _RESPONSE
DESCRIPTOR.message_types_by_name['header'] = _HEADER
DESCRIPTOR.message_types_by_name['request'] = _REQUEST
DESCRIPTOR.message_types_by_name['response'] = _RESPONSE
DESCRIPTOR.message_types_by_name['Message'] = _MESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

header = _reflection.GeneratedProtocolMessageType('header', (_message.Message,), dict(
  DESCRIPTOR = _HEADER,
  __module__ = 'v3.capture.request_response.request_response_pb2'
  # @@protoc_insertion_point(class_scope:v3.capture.request_response.header)
  ))
_sym_db.RegisterMessage(header)

request = _reflection.GeneratedProtocolMessageType('request', (_message.Message,), dict(
  DESCRIPTOR = _REQUEST,
  __module__ = 'v3.capture.request_response.request_response_pb2'
  # @@protoc_insertion_point(class_scope:v3.capture.request_response.request)
  ))
_sym_db.RegisterMessage(request)

response = _reflection.GeneratedProtocolMessageType('response', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSE,
  __module__ = 'v3.capture.request_response.request_response_pb2'
  # @@protoc_insertion_point(class_scope:v3.capture.request_response.response)
  ))
_sym_db.RegisterMessage(response)

Message = _reflection.GeneratedProtocolMessageType('Message', (_message.Message,), dict(
  DESCRIPTOR = _MESSAGE,
  __module__ = 'v3.capture.request_response.request_response_pb2'
  # @@protoc_insertion_point(class_scope:v3.capture.request_response.Message)
  ))
_sym_db.RegisterMessage(Message)


# @@protoc_insertion_point(module_scope)
