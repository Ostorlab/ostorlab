# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: agent_timeout.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

DESCRIPTOR = _descriptor.FileDescriptor(
    name='agent_timeout.proto',
    package='',
    syntax='proto2',
    serialized_pb=_b(
        '\n\x13\x61gent_timeout.proto\"}\n\ragent_timeout\x12\x0f\n\x07scan_id\x18\x01 \x02(\x05\x12\x0e\n\x06source\x18\x02 \x02(\t\x12\x1e\n\x07message\x18\x03 \x01(\t:\ragent_timeout\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\x16\n\x0e\x63orrelation_id\x18\x05 \x02(\t')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_AGENT_TIMEOUT = _descriptor.Descriptor(
    name='agent_timeout',
    full_name='agent_timeout',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='scan_id', full_name='agent_timeout.scan_id', index=0,
            number=1, type=5, cpp_type=1, label=2,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='source', full_name='agent_timeout.source', index=1,
            number=2, type=9, cpp_type=9, label=2,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='message', full_name='agent_timeout.message', index=2,
            number=3, type=9, cpp_type=9, label=1,
            has_default_value=True, default_value=_b("agent_timeout").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='description', full_name='agent_timeout.description', index=3,
            number=4, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='correlation_id', full_name='agent_timeout.correlation_id', index=4,
            number=5, type=9, cpp_type=9, label=2,
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
    serialized_start=23,
    serialized_end=148,
)

DESCRIPTOR.message_types_by_name['agent_timeout'] = _AGENT_TIMEOUT

agent_timeout = _reflection.GeneratedProtocolMessageType('agent_timeout', (_message.Message,), dict(
    DESCRIPTOR=_AGENT_TIMEOUT,
    __module__='agent_timeout_pb2'
    # @@protoc_insertion_point(class_scope:agent_timeout)
))
_sym_db.RegisterMessage(agent_timeout)

# @@protoc_insertion_point(module_scope)
