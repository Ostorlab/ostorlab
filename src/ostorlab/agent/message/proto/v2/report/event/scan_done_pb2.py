# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: scan_done.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

DESCRIPTOR = _descriptor.FileDescriptor(
    name='scan_done.proto',
    package='report.event',
    syntax='proto2',
    serialized_options=None,
    serialized_pb=_b(
        '\n\x0fscan_done.proto\x12\x0creport.event\"u\n\tscan_done\x12\x0f\n\x07scan_id\x18\x01 \x02(\x05\x12\x0e\n\x06source\x18\x02 \x02(\t\x12\x1a\n\x07message\x18\x03 \x01(\t:\tscan_done\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\x16\n\x0e\x63orrelation_id\x18\x05 \x02(\t')
)

_SCAN_DONE = _descriptor.Descriptor(
    name='scan_done',
    full_name='report.event.scan_done',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='scan_id', full_name='report.event.scan_done.scan_id', index=0,
            number=1, type=5, cpp_type=1, label=2,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='source', full_name='report.event.scan_done.source', index=1,
            number=2, type=9, cpp_type=9, label=2,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='message', full_name='report.event.scan_done.message', index=2,
            number=3, type=9, cpp_type=9, label=1,
            has_default_value=True, default_value=_b("scan_done").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='description', full_name='report.event.scan_done.description', index=3,
            number=4, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='correlation_id', full_name='report.event.scan_done.correlation_id', index=4,
            number=5, type=9, cpp_type=9, label=2,
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
    serialized_start=33,
    serialized_end=150,
)

DESCRIPTOR.message_types_by_name['scan_done'] = _SCAN_DONE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

scan_done = _reflection.GeneratedProtocolMessageType('scan_done', (_message.Message,), dict(
    DESCRIPTOR=_SCAN_DONE,
    __module__='scan_done_pb2'
    # @@protoc_insertion_point(class_scope:report.event.scan_done)
))
_sym_db.RegisterMessage(scan_done)

# @@protoc_insertion_point(module_scope)
