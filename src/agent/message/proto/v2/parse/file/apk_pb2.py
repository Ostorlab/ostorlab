# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: apk.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

DESCRIPTOR = _descriptor.FileDescriptor(
    name='apk.proto',
    package='',
    syntax='proto2',
    serialized_options=None,
    serialized_pb=_b(
        '\n\tapk.proto\"=\n\x03\x61pk\x12\x0f\n\x07scan_id\x18\x01 \x02(\x05\x12\x10\n\x08\x66ilename\x18\x02 \x02(\t\x12\x13\n\x0b\x66ilecontent\x18\x03 \x02(\x0c')
)

_APK = _descriptor.Descriptor(
    name='apk',
    full_name='apk',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='scan_id', full_name='apk.scan_id', index=0,
            number=1, type=5, cpp_type=1, label=2,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='filename', full_name='apk.filename', index=1,
            number=2, type=9, cpp_type=9, label=2,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='filecontent', full_name='apk.filecontent', index=2,
            number=3, type=12, cpp_type=9, label=2,
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
    serialized_start=13,
    serialized_end=74,
)

DESCRIPTOR.message_types_by_name['apk'] = _APK
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

apk = _reflection.GeneratedProtocolMessageType('apk', (_message.Message,), dict(
    DESCRIPTOR=_APK,
    __module__='apk_pb2'
    # @@protoc_insertion_point(class_scope:apk)
))
_sym_db.RegisterMessage(apk)

# @@protoc_insertion_point(module_scope)
