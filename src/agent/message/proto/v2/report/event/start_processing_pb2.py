# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: start_processing.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

DESCRIPTOR = _descriptor.FileDescriptor(
    name='start_processing.proto',
    package='',
    syntax='proto2',
    serialized_pb=_b(
        '\n\x16start_processing.proto\"\x83\x01\n\x10start_processing\x12\x0f\n\x07scan_id\x18\x01 \x02(\x05\x12\x0e\n\x06source\x18\x02 \x02(\t\x12!\n\x07message\x18\x03 \x01(\t:\x10start_processing\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\x16\n\x0e\x63orrelation_id\x18\x05 \x02(\t')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_START_PROCESSING = _descriptor.Descriptor(
    name='start_processing',
    full_name='start_processing',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='scan_id', full_name='start_processing.scan_id', index=0,
            number=1, type=5, cpp_type=1, label=2,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='source', full_name='start_processing.source', index=1,
            number=2, type=9, cpp_type=9, label=2,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='message', full_name='start_processing.message', index=2,
            number=3, type=9, cpp_type=9, label=1,
            has_default_value=True, default_value=_b("start_processing").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='description', full_name='start_processing.description', index=3,
            number=4, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='correlation_id', full_name='start_processing.correlation_id', index=4,
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
    serialized_start=27,
    serialized_end=158,
)

DESCRIPTOR.message_types_by_name['start_processing'] = _START_PROCESSING

start_processing = _reflection.GeneratedProtocolMessageType('start_processing', (_message.Message,), dict(
    DESCRIPTOR=_START_PROCESSING,
    __module__='start_processing_pb2'
    # @@protoc_insertion_point(class_scope:start_processing)
))
_sym_db.RegisterMessage(start_processing)

# @@protoc_insertion_point(module_scope)
