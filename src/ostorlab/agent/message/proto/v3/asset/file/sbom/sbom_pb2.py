# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ostorlab/agent/message/proto/v3/asset/file/sbom/sbom.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:ostorlab/agent/message/proto/v3/asset/file/sbom/sbom.proto\x12/ostorlab.agent.message.proto.v3.asset.file.sbom\"\'\n\x0f\x41ndroidMetadata\x12\x14\n\x0cpackage_name\x18\x01 \x01(\t\" \n\x0bIOSMetadata\x12\x11\n\tbundle_id\x18\x01 \x01(\t\"\x83\x02\n\x07Message\x12\x0f\n\x07\x63ontent\x18\x01 \x01(\x0c\x12\x0c\n\x04path\x18\x02 \x01(\t\x12\x13\n\x0b\x63ontent_url\x18\x03 \x01(\t\x12\\\n\x10\x61ndroid_metadata\x18\x04 \x01(\x0b\x32@.ostorlab.agent.message.proto.v3.asset.file.sbom.AndroidMetadataH\x00\x12T\n\x0cios_metadata\x18\x05 \x01(\x0b\x32<.ostorlab.agent.message.proto.v3.asset.file.sbom.IOSMetadataH\x00\x42\x10\n\x0emetadata_oneof')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ostorlab.agent.message.proto.v3.asset.file.sbom.sbom_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _ANDROIDMETADATA._serialized_start=111
  _ANDROIDMETADATA._serialized_end=150
  _IOSMETADATA._serialized_start=152
  _IOSMETADATA._serialized_end=184
  _MESSAGE._serialized_start=187
  _MESSAGE._serialized_end=446
# @@protoc_insertion_point(module_scope)
