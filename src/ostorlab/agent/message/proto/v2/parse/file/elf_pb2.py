# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: elf.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

DESCRIPTOR = _descriptor.FileDescriptor(
    name='elf.proto',
    package='',
    syntax='proto2',
    serialized_options=None,
    serialized_pb=_b(
        '\n\telf.proto\"=\n\x03\x65lf\x12\x0f\n\x07scan_id\x18\x01 \x02(\x05\x12\x10\n\x08\x66ilename\x18\x02 \x02(\t\x12\x13\n\x0b\x66ilecontent\x18\x03 \x02(\x0c')
)

_ELF = _descriptor.Descriptor(
    name='elf',
    full_name='elf',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='scan_id', full_name='elf.scan_id', index=0,
            number=1, type=5, cpp_type=1, label=2,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='filename', full_name='elf.filename', index=1,
            number=2, type=9, cpp_type=9, label=2,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='filecontent', full_name='elf.filecontent', index=2,
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

DESCRIPTOR.message_types_by_name['elf'] = _ELF
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

elf = _reflection.GeneratedProtocolMessageType('elf', (_message.Message,), dict(
    DESCRIPTOR=_ELF,
    __module__='elf_pb2'
    # @@protoc_insertion_point(class_scope:elf)
))
_sym_db.RegisterMessage(elf)

# @@protoc_insertion_point(module_scope)
