# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ios.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

DESCRIPTOR = _descriptor.FileDescriptor(
    name='ios.proto',
    package='',
    serialized_pb=_b(
        '\n\tios.proto\"I\n\x03ios\x12\x0f\n\x07scan_id\x18\x01 \x02(\x05\x12\x0c\n\x04\x66ile\x18\x02 \x02(\x0c\x12\x0c\n\x04hash\x18\x03 \x02(\t\x12\x15\n\x08platform\x18\x04 \x01(\t:\x03ios')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_IOS = _descriptor.Descriptor(
    name='ios',
    full_name='ios',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='scan_id', full_name='ios.scan_id', index=0,
            number=1, type=5, cpp_type=1, label=2,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='file', full_name='ios.file', index=1,
            number=2, type=12, cpp_type=9, label=2,
            has_default_value=False, default_value=_b(""),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='hash', full_name='ios.hash', index=2,
            number=3, type=9, cpp_type=9, label=2,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='platform', full_name='ios.platform', index=3,
            number=4, type=9, cpp_type=9, label=1,
            has_default_value=True, default_value=_b("ios").decode('utf-8'),
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
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=13,
    serialized_end=86,
)

DESCRIPTOR.message_types_by_name['ios'] = _IOS

ios = _reflection.GeneratedProtocolMessageType('ios', (_message.Message,), dict(
    DESCRIPTOR=_IOS,
    __module__='ios_pb2'
    # @@protoc_insertion_point(class_scope:ios)
))
_sym_db.RegisterMessage(ios)

# @@protoc_insertion_point(module_scope)
