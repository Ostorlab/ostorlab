# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v3/asset/link/link.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='v3/asset/link/link.proto',
  package='v3.asset.link',
  syntax='proto2',
  serialized_pb=_b('\n\x18v3/asset/link/link.proto\x12\rv3.asset.link\"0\n\x11link_extra_header\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\r\n\x05value\x18\x02 \x02(\t\"*\n\x0blink_cookie\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\r\n\x05value\x18\x02 \x02(\t\"<\n\x0flink_form_input\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x02(\t\x12\x0c\n\x04type\x18\x03 \x02(\t\"L\n\tlink_form\x12.\n\x06inputs\x18\x01 \x03(\x0b\x32\x1e.v3.asset.link.link_form_input\x12\x0f\n\x07\x65nctype\x18\x02 \x02(\t\"M\n\x0flink_credential\x12\x0c\n\x04type\x18\x01 \x02(\t\x12\r\n\x05login\x18\x02 \x01(\t\x12\x10\n\x08password\x18\x03 \x01(\t\x12\x0b\n\x03url\x18\x04 \x01(\t\"\xb0\x02\n\x07Message\x12\x0b\n\x03url\x18\x01 \x02(\t\x12\x0e\n\x06method\x18\x02 \x02(\t\x12\x0e\n\x04\x62ody\x18\x03 \x01(\x0cH\x00\x12(\n\x04\x66orm\x18\x04 \x01(\x0b\x32\x18.v3.asset.link.link_formH\x00\x12\x37\n\rextra_headers\x18\x05 \x03(\x0b\x32 .v3.asset.link.link_extra_header\x12+\n\x07\x63ookies\x18\x06 \x03(\x0b\x32\x1a.v3.asset.link.link_cookie\x12\x32\n\ncredential\x18\x07 \x01(\x0b\x32\x1e.v3.asset.link.link_credential\x12&\n\x06parent\x18\x08 \x01(\x0b\x32\x16.v3.asset.link.MessageB\x0c\n\nbody_oneof')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_LINK_EXTRA_HEADER = _descriptor.Descriptor(
  name='link_extra_header',
  full_name='v3.asset.link.link_extra_header',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='v3.asset.link.link_extra_header.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='v3.asset.link.link_extra_header.value', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=43,
  serialized_end=91,
)


_LINK_COOKIE = _descriptor.Descriptor(
  name='link_cookie',
  full_name='v3.asset.link.link_cookie',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='v3.asset.link.link_cookie.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='v3.asset.link.link_cookie.value', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=93,
  serialized_end=135,
)


_LINK_FORM_INPUT = _descriptor.Descriptor(
  name='link_form_input',
  full_name='v3.asset.link.link_form_input',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='v3.asset.link.link_form_input.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='v3.asset.link.link_form_input.value', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='v3.asset.link.link_form_input.type', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=137,
  serialized_end=197,
)


_LINK_FORM = _descriptor.Descriptor(
  name='link_form',
  full_name='v3.asset.link.link_form',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='inputs', full_name='v3.asset.link.link_form.inputs', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='enctype', full_name='v3.asset.link.link_form.enctype', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=199,
  serialized_end=275,
)


_LINK_CREDENTIAL = _descriptor.Descriptor(
  name='link_credential',
  full_name='v3.asset.link.link_credential',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='v3.asset.link.link_credential.type', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='login', full_name='v3.asset.link.link_credential.login', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='password', full_name='v3.asset.link.link_credential.password', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='url', full_name='v3.asset.link.link_credential.url', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=277,
  serialized_end=354,
)


_MESSAGE = _descriptor.Descriptor(
  name='Message',
  full_name='v3.asset.link.Message',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='url', full_name='v3.asset.link.Message.url', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='method', full_name='v3.asset.link.Message.method', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='body', full_name='v3.asset.link.Message.body', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='form', full_name='v3.asset.link.Message.form', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='extra_headers', full_name='v3.asset.link.Message.extra_headers', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cookies', full_name='v3.asset.link.Message.cookies', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='credential', full_name='v3.asset.link.Message.credential', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='parent', full_name='v3.asset.link.Message.parent', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='body_oneof', full_name='v3.asset.link.Message.body_oneof',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=357,
  serialized_end=661,
)

_LINK_FORM.fields_by_name['inputs'].message_type = _LINK_FORM_INPUT
_MESSAGE.fields_by_name['form'].message_type = _LINK_FORM
_MESSAGE.fields_by_name['extra_headers'].message_type = _LINK_EXTRA_HEADER
_MESSAGE.fields_by_name['cookies'].message_type = _LINK_COOKIE
_MESSAGE.fields_by_name['credential'].message_type = _LINK_CREDENTIAL
_MESSAGE.fields_by_name['parent'].message_type = _MESSAGE
_MESSAGE.oneofs_by_name['body_oneof'].fields.append(
  _MESSAGE.fields_by_name['body'])
_MESSAGE.fields_by_name['body'].containing_oneof = _MESSAGE.oneofs_by_name['body_oneof']
_MESSAGE.oneofs_by_name['body_oneof'].fields.append(
  _MESSAGE.fields_by_name['form'])
_MESSAGE.fields_by_name['form'].containing_oneof = _MESSAGE.oneofs_by_name['body_oneof']
DESCRIPTOR.message_types_by_name['link_extra_header'] = _LINK_EXTRA_HEADER
DESCRIPTOR.message_types_by_name['link_cookie'] = _LINK_COOKIE
DESCRIPTOR.message_types_by_name['link_form_input'] = _LINK_FORM_INPUT
DESCRIPTOR.message_types_by_name['link_form'] = _LINK_FORM
DESCRIPTOR.message_types_by_name['link_credential'] = _LINK_CREDENTIAL
DESCRIPTOR.message_types_by_name['Message'] = _MESSAGE

link_extra_header = _reflection.GeneratedProtocolMessageType('link_extra_header', (_message.Message,), dict(
  DESCRIPTOR = _LINK_EXTRA_HEADER,
  __module__ = 'v3.asset.link.link_pb2'
  # @@protoc_insertion_point(class_scope:v3.asset.link.link_extra_header)
  ))
_sym_db.RegisterMessage(link_extra_header)

link_cookie = _reflection.GeneratedProtocolMessageType('link_cookie', (_message.Message,), dict(
  DESCRIPTOR = _LINK_COOKIE,
  __module__ = 'v3.asset.link.link_pb2'
  # @@protoc_insertion_point(class_scope:v3.asset.link.link_cookie)
  ))
_sym_db.RegisterMessage(link_cookie)

link_form_input = _reflection.GeneratedProtocolMessageType('link_form_input', (_message.Message,), dict(
  DESCRIPTOR = _LINK_FORM_INPUT,
  __module__ = 'v3.asset.link.link_pb2'
  # @@protoc_insertion_point(class_scope:v3.asset.link.link_form_input)
  ))
_sym_db.RegisterMessage(link_form_input)

link_form = _reflection.GeneratedProtocolMessageType('link_form', (_message.Message,), dict(
  DESCRIPTOR = _LINK_FORM,
  __module__ = 'v3.asset.link.link_pb2'
  # @@protoc_insertion_point(class_scope:v3.asset.link.link_form)
  ))
_sym_db.RegisterMessage(link_form)

link_credential = _reflection.GeneratedProtocolMessageType('link_credential', (_message.Message,), dict(
  DESCRIPTOR = _LINK_CREDENTIAL,
  __module__ = 'v3.asset.link.link_pb2'
  # @@protoc_insertion_point(class_scope:v3.asset.link.link_credential)
  ))
_sym_db.RegisterMessage(link_credential)

Message = _reflection.GeneratedProtocolMessageType('Message', (_message.Message,), dict(
  DESCRIPTOR = _MESSAGE,
  __module__ = 'v3.asset.link.link_pb2'
  # @@protoc_insertion_point(class_scope:v3.asset.link.Message)
  ))
_sym_db.RegisterMessage(Message)


# @@protoc_insertion_point(module_scope)