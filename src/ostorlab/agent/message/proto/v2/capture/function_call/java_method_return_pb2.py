# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: java_method_return.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

DESCRIPTOR = _descriptor.FileDescriptor(
    name='java_method_return.proto',
    package='',
    serialized_pb=_b(
        '\n\x18java_method_return.proto\"\xbf\x01\n\x10java_method_call\x12\x0f\n\x07scan_id\x18\x01 \x02(\x05\x12\x12\n\nclass_name\x18\x02 \x02(\t\x12\x13\n\x0bmethod_name\x18\x03 \x02(\t\x12\x11\n\tsignature\x18\x04 \x02(\t\x12-\n\x06result\x18\x06 \x02(\x0b\x32\x1d.java_method_call.java_object\x1a/\n\x0bjava_object\x12\x11\n\tsignature\x18\x04 \x02(\t\x12\r\n\x05value\x18\x05 \x02(\x0c')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_JAVA_METHOD_CALL_JAVA_OBJECT = _descriptor.Descriptor(
    name='java_object',
    full_name='java_method_call.java_object',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='signature', full_name='java_method_call.java_object.signature', index=0,
            number=4, type=9, cpp_type=9, label=2,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='value', full_name='java_method_call.java_object.value', index=1,
            number=5, type=12, cpp_type=9, label=2,
            has_default_value=False, default_value=_b(""),
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
    serialized_start=173,
    serialized_end=220,
)

_JAVA_METHOD_CALL = _descriptor.Descriptor(
    name='java_method_call',
    full_name='java_method_call',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='scan_id', full_name='java_method_call.scan_id', index=0,
            number=1, type=5, cpp_type=1, label=2,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='class_name', full_name='java_method_call.class_name', index=1,
            number=2, type=9, cpp_type=9, label=2,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='method_name', full_name='java_method_call.method_name', index=2,
            number=3, type=9, cpp_type=9, label=2,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='signature', full_name='java_method_call.signature', index=3,
            number=4, type=9, cpp_type=9, label=2,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='result', full_name='java_method_call.result', index=4,
            number=6, type=11, cpp_type=10, label=2,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
    ],
    extensions=[
    ],
    nested_types=[_JAVA_METHOD_CALL_JAVA_OBJECT, ],
    enum_types=[
    ],
    options=None,
    is_extendable=False,
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=29,
    serialized_end=220,
)

_JAVA_METHOD_CALL_JAVA_OBJECT.containing_type = _JAVA_METHOD_CALL
_JAVA_METHOD_CALL.fields_by_name['result'].message_type = _JAVA_METHOD_CALL_JAVA_OBJECT
DESCRIPTOR.message_types_by_name['java_method_call'] = _JAVA_METHOD_CALL

java_method_call = _reflection.GeneratedProtocolMessageType('java_method_call', (_message.Message,), dict(

    java_object=_reflection.GeneratedProtocolMessageType('java_object', (_message.Message,), dict(
        DESCRIPTOR=_JAVA_METHOD_CALL_JAVA_OBJECT,
        __module__='java_method_return_pb2'
        # @@protoc_insertion_point(class_scope:java_method_call.java_object)
    ))
    ,
    DESCRIPTOR=_JAVA_METHOD_CALL,
    __module__='java_method_return_pb2'
    # @@protoc_insertion_point(class_scope:java_method_call)
))
_sym_db.RegisterMessage(java_method_call)
_sym_db.RegisterMessage(java_method_call.java_object)

# @@protoc_insertion_point(module_scope)
