# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ostorlab/agent/message/proto/v3/asset/ip/v6/whois/whois.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n=ostorlab/agent/message/proto/v3/asset/ip/v6/whois/whois.proto\x12\x31ostorlab.agent.message.proto.v3.asset.ip.v6.whois\"L\n\x07Network\x12\x0c\n\x04\x63idr\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0e\n\x06handle\x18\x03 \x01(\t\x12\x15\n\rparent_handle\x18\x04 \x01(\t\"E\n\x07\x43ontact\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04kind\x18\x02 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x03 \x01(\t\x12\r\n\x05\x65mail\x18\x04 \x01(\t\"c\n\x06\x45ntity\x12\x0c\n\x04name\x18\x01 \x01(\t\x12K\n\x07\x63ontact\x18\x02 \x01(\x0b\x32:.ostorlab.agent.message.proto.v3.asset.ip.v6.whois.Contact\"\xc2\x02\n\x07Message\x12\x0c\n\x04host\x18\x01 \x01(\t\x12\x0c\n\x04mask\x18\x02 \x01(\t\x12\x12\n\x07version\x18\x03 \x01(\x05:\x01\x36\x12\x14\n\x0c\x61sn_registry\x18\x04 \x01(\t\x12\x12\n\nasn_number\x18\x05 \x01(\x05\x12\x18\n\x10\x61sn_country_code\x18\x06 \x01(\t\x12\x10\n\x08\x61sn_date\x18\x07 \x01(\t\x12\x17\n\x0f\x61sn_description\x18\x08 \x01(\t\x12K\n\x07network\x18\t \x01(\x0b\x32:.ostorlab.agent.message.proto.v3.asset.ip.v6.whois.Network\x12K\n\x08\x65ntities\x18\n \x03(\x0b\x32\x39.ostorlab.agent.message.proto.v3.asset.ip.v6.whois.Entity')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ostorlab.agent.message.proto.v3.asset.ip.v6.whois.whois_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _NETWORK._serialized_start=116
  _NETWORK._serialized_end=192
  _CONTACT._serialized_start=194
  _CONTACT._serialized_end=263
  _ENTITY._serialized_start=265
  _ENTITY._serialized_end=364
  _MESSAGE._serialized_start=367
  _MESSAGE._serialized_end=689
# @@protoc_insertion_point(module_scope)
