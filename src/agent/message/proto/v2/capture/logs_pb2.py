# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: logs.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

DESCRIPTOR = _descriptor.FileDescriptor(
    name='logs.proto',
    package='',
    syntax='proto2',
    serialized_pb=_b(
        '\n\nlogs.proto\"J\n\x04logs\x12\x0f\n\x07scan_id\x18\x01 \x02(\x05\x12\x11\n\ttimestamp\x18\x02 \x02(\x02\x12\r\n\x05level\x18\x03 \x02(\t\x12\x0f\n\x07message\x18\x04 \x02(\t')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_LOGS = _descriptor.Descriptor(
    name='logs',
    full_name='logs',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='scan_id', full_name='logs.scan_id', index=0,
            number=1, type=5, cpp_type=1, label=2,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='timestamp', full_name='logs.timestamp', index=1,
            number=2, type=2, cpp_type=6, label=2,
            has_default_value=False, default_value=float(0),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='level', full_name='logs.level', index=2,
            number=3, type=9, cpp_type=9, label=2,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='message', full_name='logs.message', index=3,
            number=4, type=9, cpp_type=9, label=2,
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
    serialized_start=14,
    serialized_end=88,
)

DESCRIPTOR.message_types_by_name['logs'] = _LOGS

logs = _reflection.GeneratedProtocolMessageType('logs', (_message.Message,), dict(
    DESCRIPTOR=_LOGS,
    __module__='logs_pb2'
    # @@protoc_insertion_point(class_scope:logs)
))
_sym_db.RegisterMessage(logs)

# @@protoc_insertion_point(module_scope)
