# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pkg/imrpc/imrpc.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15pkg/imrpc/imrpc.proto\x12\tpkg.imrpc\x1a\x1bgoogle/protobuf/empty.proto\"`\n\x0bProcessSpec\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06\x62inary\x18\x02 \x01(\t\x12\x0c\n\x04\x61rgs\x18\x03 \x03(\t\x12\x12\n\nport_count\x18\x04 \x01(\x05\x12\x11\n\tport_args\x18\x05 \x03(\t\"\xc8\x01\n\rProcessStatus\x12\r\n\x05state\x18\x01 \x01(\t\x12\x11\n\terror_msg\x18\x02 \x01(\t\x12\x12\n\nport_start\x18\x03 \x01(\x05\x12\x10\n\x08port_end\x18\x04 \x01(\x05\x12<\n\nconditions\x18\x05 \x03(\x0b\x32(.pkg.imrpc.ProcessStatus.ConditionsEntry\x1a\x31\n\x0f\x43onditionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x08:\x02\x38\x01\"<\n\x14ProcessCreateRequest\x12$\n\x04spec\x18\x01 \x01(\x0b\x32\x16.pkg.imrpc.ProcessSpec\"$\n\x14ProcessDeleteRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"!\n\x11ProcessGetRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"r\n\x0fProcessResponse\x12$\n\x04spec\x18\x01 \x01(\x0b\x32\x16.pkg.imrpc.ProcessSpec\x12(\n\x06status\x18\x02 \x01(\x0b\x32\x18.pkg.imrpc.ProcessStatus\x12\x0f\n\x07\x64\x65leted\x18\x03 \x01(\x08\"\x14\n\x12ProcessListRequest\"\xa5\x01\n\x13ProcessListResponse\x12@\n\tprocesses\x18\x01 \x03(\x0b\x32-.pkg.imrpc.ProcessListResponse.ProcessesEntry\x1aL\n\x0eProcessesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12)\n\x05value\x18\x02 \x01(\x0b\x32\x1a.pkg.imrpc.ProcessResponse:\x02\x38\x01\"\x1a\n\nLogRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"W\n\x15ProcessReplaceRequest\x12$\n\x04spec\x18\x01 \x01(\x0b\x32\x16.pkg.imrpc.ProcessSpec\x12\x18\n\x10terminate_signal\x18\x02 \x01(\t\"\x1b\n\x0bLogResponse\x12\x0c\n\x04line\x18\x02 \x01(\t\"\xe4\x01\n\x0fVersionResponse\x12\x0f\n\x07version\x18\x01 \x01(\t\x12\x11\n\tgitCommit\x18\x02 \x01(\t\x12\x11\n\tbuildDate\x18\x03 \x01(\t\x12!\n\x19instanceManagerAPIVersion\x18\x04 \x01(\x03\x12$\n\x1cinstanceManagerAPIMinVersion\x18\x05 \x01(\x03\x12&\n\x1einstanceManagerProxyAPIVersion\x18\x06 \x01(\x03\x12)\n!instanceManagerProxyAPIMinVersion\x18\x07 \x01(\x03\x32\xee\x04\n\x15ProcessManagerService\x12N\n\rProcessCreate\x12\x1f.pkg.imrpc.ProcessCreateRequest\x1a\x1a.pkg.imrpc.ProcessResponse\"\x00\x12N\n\rProcessDelete\x12\x1f.pkg.imrpc.ProcessDeleteRequest\x1a\x1a.pkg.imrpc.ProcessResponse\"\x00\x12H\n\nProcessGet\x12\x1c.pkg.imrpc.ProcessGetRequest\x1a\x1a.pkg.imrpc.ProcessResponse\"\x00\x12N\n\x0bProcessList\x12\x1d.pkg.imrpc.ProcessListRequest\x1a\x1e.pkg.imrpc.ProcessListResponse\"\x00\x12?\n\nProcessLog\x12\x15.pkg.imrpc.LogRequest\x1a\x16.pkg.imrpc.LogResponse\"\x00\x30\x01\x12\x46\n\x0cProcessWatch\x12\x16.google.protobuf.Empty\x1a\x1a.pkg.imrpc.ProcessResponse\"\x00\x30\x01\x12P\n\x0eProcessReplace\x12 .pkg.imrpc.ProcessReplaceRequest\x1a\x1a.pkg.imrpc.ProcessResponse\"\x00\x12@\n\nVersionGet\x12\x16.google.protobuf.Empty\x1a\x1a.pkg.imrpc.VersionResponseB2Z0github.com/longhorn/longhorn-interface/pkg/imrpcb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'pkg.imrpc.imrpc_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z0github.com/longhorn/longhorn-interface/pkg/imrpc'
  _PROCESSSTATUS_CONDITIONSENTRY._options = None
  _PROCESSSTATUS_CONDITIONSENTRY._serialized_options = b'8\001'
  _PROCESSLISTRESPONSE_PROCESSESENTRY._options = None
  _PROCESSLISTRESPONSE_PROCESSESENTRY._serialized_options = b'8\001'
  _globals['_PROCESSSPEC']._serialized_start=65
  _globals['_PROCESSSPEC']._serialized_end=161
  _globals['_PROCESSSTATUS']._serialized_start=164
  _globals['_PROCESSSTATUS']._serialized_end=364
  _globals['_PROCESSSTATUS_CONDITIONSENTRY']._serialized_start=315
  _globals['_PROCESSSTATUS_CONDITIONSENTRY']._serialized_end=364
  _globals['_PROCESSCREATEREQUEST']._serialized_start=366
  _globals['_PROCESSCREATEREQUEST']._serialized_end=426
  _globals['_PROCESSDELETEREQUEST']._serialized_start=428
  _globals['_PROCESSDELETEREQUEST']._serialized_end=464
  _globals['_PROCESSGETREQUEST']._serialized_start=466
  _globals['_PROCESSGETREQUEST']._serialized_end=499
  _globals['_PROCESSRESPONSE']._serialized_start=501
  _globals['_PROCESSRESPONSE']._serialized_end=615
  _globals['_PROCESSLISTREQUEST']._serialized_start=617
  _globals['_PROCESSLISTREQUEST']._serialized_end=637
  _globals['_PROCESSLISTRESPONSE']._serialized_start=640
  _globals['_PROCESSLISTRESPONSE']._serialized_end=805
  _globals['_PROCESSLISTRESPONSE_PROCESSESENTRY']._serialized_start=729
  _globals['_PROCESSLISTRESPONSE_PROCESSESENTRY']._serialized_end=805
  _globals['_LOGREQUEST']._serialized_start=807
  _globals['_LOGREQUEST']._serialized_end=833
  _globals['_PROCESSREPLACEREQUEST']._serialized_start=835
  _globals['_PROCESSREPLACEREQUEST']._serialized_end=922
  _globals['_LOGRESPONSE']._serialized_start=924
  _globals['_LOGRESPONSE']._serialized_end=951
  _globals['_VERSIONRESPONSE']._serialized_start=954
  _globals['_VERSIONRESPONSE']._serialized_end=1182
  _globals['_PROCESSMANAGERSERVICE']._serialized_start=1185
  _globals['_PROCESSMANAGERSERVICE']._serialized_end=1807
# @@protoc_insertion_point(module_scope)
