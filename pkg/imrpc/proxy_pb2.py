# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pkg/imrpc/proxy.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from pkg.enginerpc import controller_pb2 as pkg_dot_enginerpc_dot_controller__pb2
from pkg.enginerpc import syncagent_pb2 as pkg_dot_enginerpc_dot_syncagent__pb2
from pkg.imrpc import common_pb2 as pkg_dot_imrpc_dot_common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15pkg/imrpc/proxy.proto\x12\tpkg.imrpc\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1epkg/enginerpc/controller.proto\x1a\x1dpkg/enginerpc/syncagent.proto\x1a\x16pkg/imrpc/common.proto\"\xbc\x01\n\x12ProxyEngineRequest\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12?\n\x14\x62\x61\x63kend_store_driver\x18\x02 \x01(\x0e\x32\x1d.pkg.imrpc.BackendStoreDriverB\x02\x18\x01\x12\x13\n\x0b\x65ngine_name\x18\x03 \x01(\t\x12\x13\n\x0bvolume_name\x18\x04 \x01(\t\x12*\n\x0b\x64\x61ta_engine\x18\x05 \x01(\x0e\x32\x15.pkg.imrpc.DataEngine\"K\n\x1a\x45ngineVersionProxyResponse\x12-\n\x07version\x18\x01 \x01(\x0b\x32\x1c.pkg.enginerpc.VersionOutput\"E\n\x1c\x45ngineVolumeGetProxyResponse\x12%\n\x06volume\x18\x01 \x01(\x0b\x32\x15.pkg.enginerpc.Volume\"\x8c\x01\n\x19\x45ngineVolumeExpandRequest\x12;\n\x14proxy_engine_request\x18\x01 \x01(\x0b\x32\x1d.pkg.imrpc.ProxyEngineRequest\x12\x32\n\x06\x65xpand\x18\x02 \x01(\x0b\x32\".pkg.enginerpc.VolumeExpandRequest\"\xa2\x01\n EngineVolumeFrontendStartRequest\x12;\n\x14proxy_engine_request\x18\x01 \x01(\x0b\x32\x1d.pkg.imrpc.ProxyEngineRequest\x12\x41\n\x0e\x66rontend_start\x18\x02 \x01(\x0b\x32).pkg.enginerpc.VolumeFrontendStartRequest\"\x99\x01\n\x1b\x45ngineVolumeSnapshotRequest\x12;\n\x14proxy_engine_request\x18\x01 \x01(\x0b\x32\x1d.pkg.imrpc.ProxyEngineRequest\x12=\n\x0fsnapshot_volume\x18\x02 \x01(\x0b\x32$.pkg.enginerpc.VolumeSnapshotRequest\"Y\n!EngineVolumeSnapshotProxyResponse\x12\x34\n\x08snapshot\x18\x01 \x01(\x0b\x32\".pkg.enginerpc.VolumeSnapshotReply\"\xc1\x01\n/EngineVolumeUnmapMarkSnapChainRemovedSetRequest\x12;\n\x14proxy_engine_request\x18\x01 \x01(\x0b\x32\x1d.pkg.imrpc.ProxyEngineRequest\x12Q\n\x0funmap_mark_snap\x18\x02 \x01(\x0b\x32\x38.pkg.enginerpc.VolumeUnmapMarkSnapChainRemovedSetRequest\"\xa5\x01\n&EngineVolumeSnapshotMaxCountSetRequest\x12;\n\x14proxy_engine_request\x18\x01 \x01(\x0b\x32\x1d.pkg.imrpc.ProxyEngineRequest\x12>\n\x05\x63ount\x18\x02 \x01(\x0b\x32/.pkg.enginerpc.VolumeSnapshotMaxCountSetRequest\"\xa2\x01\n%EngineVolumeSnapshotMaxSizeSetRequest\x12;\n\x14proxy_engine_request\x18\x01 \x01(\x0b\x32\x1d.pkg.imrpc.ProxyEngineRequest\x12<\n\x04size\x18\x02 \x01(\x0b\x32..pkg.enginerpc.VolumeSnapshotMaxSizeSetRequest\"\xb8\x01\n\x1f\x45ngineSnapshotListProxyResponse\x12\x44\n\x05\x64isks\x18\x01 \x03(\x0b\x32\x35.pkg.imrpc.EngineSnapshotListProxyResponse.DisksEntry\x1aO\n\nDisksEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x30\n\x05value\x18\x02 \x01(\x0b\x32!.pkg.imrpc.EngineSnapshotDiskInfo:\x02\x38\x01\"\xde\x02\n\x16\x45ngineSnapshotDiskInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06parent\x18\x02 \x01(\t\x12\x41\n\x08\x63hildren\x18\x03 \x03(\x0b\x32/.pkg.imrpc.EngineSnapshotDiskInfo.ChildrenEntry\x12\x0f\n\x07removed\x18\x04 \x01(\x08\x12\x14\n\x0cuser_created\x18\x05 \x01(\x08\x12\x0f\n\x07\x63reated\x18\x06 \x01(\t\x12\x0c\n\x04size\x18\x07 \x01(\t\x12=\n\x06labels\x18\x08 \x03(\x0b\x32-.pkg.imrpc.EngineSnapshotDiskInfo.LabelsEntry\x1a/\n\rChildrenEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x08:\x02\x38\x01\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"h\n\x1b\x45ngineSnapshotRevertRequest\x12;\n\x14proxy_engine_request\x18\x01 \x01(\x0b\x32\x1d.pkg.imrpc.ProxyEngineRequest\x12\x0c\n\x04name\x18\x02 \x01(\t\"v\n\x1a\x45ngineSnapshotPurgeRequest\x12;\n\x14proxy_engine_request\x18\x01 \x01(\x0b\x32\x1d.pkg.imrpc.ProxyEngineRequest\x12\x1b\n\x13skip_if_in_progress\x18\x02 \x01(\x08\"\xd2\x01\n&EngineSnapshotPurgeStatusProxyResponse\x12M\n\x06status\x18\x01 \x03(\x0b\x32=.pkg.imrpc.EngineSnapshotPurgeStatusProxyResponse.StatusEntry\x1aY\n\x0bStatusEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x39\n\x05value\x18\x02 \x01(\x0b\x32*.pkg.enginerpc.SnapshotPurgeStatusResponse:\x02\x38\x01\"\x8f\x02\n\x1a\x45ngineSnapshotCloneRequest\x12;\n\x14proxy_engine_request\x18\x01 \x01(\x0b\x32\x1d.pkg.imrpc.ProxyEngineRequest\x12\x1b\n\x13\x66rom_engine_address\x18\x02 \x01(\t\x12\x15\n\rsnapshot_name\x18\x03 \x01(\t\x12%\n\x1d\x65xport_backing_image_if_exist\x18\x04 \x01(\x08\x12%\n\x1d\x66ile_sync_http_client_timeout\x18\x05 \x01(\x05\x12\x18\n\x10\x66rom_engine_name\x18\x06 \x01(\t\x12\x18\n\x10\x66rom_volume_name\x18\x07 \x01(\t\"\xd2\x01\n&EngineSnapshotCloneStatusProxyResponse\x12M\n\x06status\x18\x01 \x03(\x0b\x32=.pkg.imrpc.EngineSnapshotCloneStatusProxyResponse.StatusEntry\x1aY\n\x0bStatusEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x39\n\x05value\x18\x02 \x01(\x0b\x32*.pkg.enginerpc.SnapshotCloneStatusResponse:\x02\x38\x01\"i\n\x1b\x45ngineSnapshotRemoveRequest\x12;\n\x14proxy_engine_request\x18\x01 \x01(\x0b\x32\x1d.pkg.imrpc.ProxyEngineRequest\x12\r\n\x05names\x18\x02 \x03(\t\"\xac\x03\n\x1b\x45ngineSnapshotBackupRequest\x12;\n\x14proxy_engine_request\x18\x01 \x01(\x0b\x32\x1d.pkg.imrpc.ProxyEngineRequest\x12\x0c\n\x04\x65nvs\x18\x08 \x03(\t\x12\x13\n\x0b\x62\x61\x63kup_name\x18\x02 \x01(\t\x12\x15\n\rsnapshot_name\x18\x03 \x01(\t\x12\x15\n\rbackup_target\x18\x04 \x01(\t\x12\x1a\n\x12\x62\x61\x63king_image_name\x18\x05 \x01(\t\x12\x1e\n\x16\x62\x61\x63king_image_checksum\x18\x06 \x01(\t\x12\x42\n\x06labels\x18\x07 \x03(\x0b\x32\x32.pkg.imrpc.EngineSnapshotBackupRequest.LabelsEntry\x12\x1a\n\x12\x63ompression_method\x18\t \x01(\t\x12\x18\n\x10\x63oncurrent_limit\x18\n \x01(\x05\x12\x1a\n\x12storage_class_name\x18\x0b \x01(\t\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"_\n!EngineSnapshotBackupProxyResponse\x12\x11\n\tbackup_id\x18\x01 \x01(\t\x12\x0f\n\x07replica\x18\x02 \x01(\t\x12\x16\n\x0eis_incremental\x18\x03 \x01(\x08\"\xa4\x01\n!EngineSnapshotBackupStatusRequest\x12;\n\x14proxy_engine_request\x18\x01 \x01(\x0b\x32\x1d.pkg.imrpc.ProxyEngineRequest\x12\x13\n\x0b\x62\x61\x63kup_name\x18\x02 \x01(\t\x12\x17\n\x0freplica_address\x18\x03 \x01(\t\x12\x14\n\x0creplica_name\x18\x04 \x01(\t\"\x9d\x01\n\'EngineSnapshotBackupStatusProxyResponse\x12\x12\n\nbackup_url\x18\x01 \x01(\t\x12\r\n\x05\x65rror\x18\x02 \x01(\t\x12\x10\n\x08progress\x18\x03 \x01(\x05\x12\x15\n\rsnapshot_name\x18\x04 \x01(\t\x12\r\n\x05state\x18\x05 \x01(\t\x12\x17\n\x0freplica_address\x18\x06 \x01(\t\"\xb3\x01\n\x1a\x45ngineBackupRestoreRequest\x12;\n\x14proxy_engine_request\x18\x01 \x01(\x0b\x32\x1d.pkg.imrpc.ProxyEngineRequest\x12\x0c\n\x04\x65nvs\x18\x02 \x03(\t\x12\x0b\n\x03url\x18\x03 \x01(\t\x12\x0e\n\x06target\x18\x04 \x01(\t\x12\x13\n\x0bvolume_name\x18\x05 \x01(\t\x12\x18\n\x10\x63oncurrent_limit\x18\x06 \x01(\x05\"5\n EngineBackupRestoreProxyResponse\x12\x11\n\ttaskError\x18\x01 \x01(\x0c\"\xcc\x01\n&EngineBackupRestoreStatusProxyResponse\x12M\n\x06status\x18\x01 \x03(\x0b\x32=.pkg.imrpc.EngineBackupRestoreStatusProxyResponse.StatusEntry\x1aS\n\x0bStatusEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x33\n\x05value\x18\x02 \x01(\x0b\x32$.pkg.imrpc.EngineBackupRestoreStatus:\x02\x38\x01\"\xc0\x01\n\x19\x45ngineBackupRestoreStatus\x12\x14\n\x0cis_restoring\x18\x01 \x01(\x08\x12\x15\n\rlast_restored\x18\x02 \x01(\t\x12 \n\x18\x63urrent_restoring_backup\x18\x03 \x01(\t\x12\x10\n\x08progress\x18\x04 \x01(\x05\x12\r\n\x05\x65rror\x18\x05 \x01(\t\x12\x10\n\x08\x66ilename\x18\x06 \x01(\t\x12\r\n\x05state\x18\x07 \x01(\t\x12\x12\n\nbackup_url\x18\x08 \x01(\t\"_\n EngineBackupRestoreFinishRequest\x12;\n\x14proxy_engine_request\x18\x01 \x01(\x0b\x32\x1d.pkg.imrpc.ProxyEngineRequest\"\xf4\x01\n\x17\x45ngineReplicaAddRequest\x12;\n\x14proxy_engine_request\x18\x01 \x01(\x0b\x32\x1d.pkg.imrpc.ProxyEngineRequest\x12\x17\n\x0freplica_address\x18\x02 \x01(\t\x12\x0f\n\x07restore\x18\x03 \x01(\x08\x12\x0c\n\x04size\x18\x04 \x01(\x03\x12\x14\n\x0c\x63urrent_size\x18\x05 \x01(\x03\x12\x11\n\tfast_sync\x18\x06 \x01(\x08\x12%\n\x1d\x66ile_sync_http_client_timeout\x18\x07 \x01(\x05\x12\x14\n\x0creplica_name\x18\x08 \x01(\t\"W\n\x1e\x45ngineReplicaListProxyResponse\x12\x35\n\x0creplica_list\x18\x01 \x01(\x0b\x32\x1f.pkg.enginerpc.ReplicaListReply\"\x8f\x01\n!EngineReplicaVerifyRebuildRequest\x12;\n\x14proxy_engine_request\x18\x01 \x01(\x0b\x32\x1d.pkg.imrpc.ProxyEngineRequest\x12\x17\n\x0freplica_address\x18\x02 \x01(\t\x12\x14\n\x0creplica_name\x18\x03 \x01(\t\"\xd5\x01\n\'EngineReplicaRebuildStatusProxyResponse\x12N\n\x06status\x18\x01 \x03(\x0b\x32>.pkg.imrpc.EngineReplicaRebuildStatusProxyResponse.StatusEntry\x1aZ\n\x0bStatusEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12:\n\x05value\x18\x02 \x01(\x0b\x32+.pkg.enginerpc.ReplicaRebuildStatusResponse:\x02\x38\x01\"\x88\x01\n\x1a\x45ngineReplicaRemoveRequest\x12;\n\x14proxy_engine_request\x18\x01 \x01(\x0b\x32\x1d.pkg.imrpc.ProxyEngineRequest\x12\x17\n\x0freplica_address\x18\x02 \x01(\t\x12\x14\n\x0creplica_name\x18\x03 \x01(\t\"\xa0\x01\n\x1e\x45ngineReplicaModeUpdateRequest\x12;\n\x14proxy_engine_request\x18\x01 \x01(\x0b\x32\x1d.pkg.imrpc.ProxyEngineRequest\x12\x17\n\x0freplica_address\x18\x02 \x01(\t\x12(\n\x04mode\x18\x03 \x01(\x0e\x32\x1a.pkg.enginerpc.ReplicaMode\"\x7f\n\x19\x45ngineSnapshotHashRequest\x12;\n\x14proxy_engine_request\x18\x01 \x01(\x0b\x32\x1d.pkg.imrpc.ProxyEngineRequest\x12\x15\n\rsnapshot_name\x18\x02 \x01(\t\x12\x0e\n\x06rehash\x18\x03 \x01(\x08\"u\n\x1f\x45ngineSnapshotHashStatusRequest\x12;\n\x14proxy_engine_request\x18\x01 \x01(\x0b\x32\x1d.pkg.imrpc.ProxyEngineRequest\x12\x15\n\rsnapshot_name\x18\x02 \x01(\t\"\xcf\x01\n%EngineSnapshotHashStatusProxyResponse\x12L\n\x06status\x18\x01 \x03(\x0b\x32<.pkg.imrpc.EngineSnapshotHashStatusProxyResponse.StatusEntry\x1aX\n\x0bStatusEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x38\n\x05value\x18\x02 \x01(\x0b\x32).pkg.enginerpc.SnapshotHashStatusResponse:\x02\x38\x01\"H\n\x1d\x45ngineMetricsGetProxyResponse\x12\'\n\x07metrics\x18\x01 \x01(\x0b\x32\x16.pkg.enginerpc.Metrics\"+\n\x14RemountVolumeRequest\x12\x13\n\x0bvolume_name\x18\x01 \x01(\t2\xb9\x17\n\x12ProxyEngineService\x12X\n\x10ServerVersionGet\x12\x1d.pkg.imrpc.ProxyEngineRequest\x1a%.pkg.imrpc.EngineVersionProxyResponse\x12S\n\tVolumeGet\x12\x1d.pkg.imrpc.ProxyEngineRequest\x1a\'.pkg.imrpc.EngineVolumeGetProxyResponse\x12L\n\x0cVolumeExpand\x12$.pkg.imrpc.EngineVolumeExpandRequest\x1a\x16.google.protobuf.Empty\x12Z\n\x13VolumeFrontendStart\x12+.pkg.imrpc.EngineVolumeFrontendStartRequest\x1a\x16.google.protobuf.Empty\x12O\n\x16VolumeFrontendShutdown\x12\x1d.pkg.imrpc.ProxyEngineRequest\x1a\x16.google.protobuf.Empty\x12x\n\"VolumeUnmapMarkSnapChainRemovedSet\x12:.pkg.imrpc.EngineVolumeUnmapMarkSnapChainRemovedSetRequest\x1a\x16.google.protobuf.Empty\x12\x66\n\x19VolumeSnapshotMaxCountSet\x12\x31.pkg.imrpc.EngineVolumeSnapshotMaxCountSetRequest\x1a\x16.google.protobuf.Empty\x12\x64\n\x18VolumeSnapshotMaxSizeSet\x12\x30.pkg.imrpc.EngineVolumeSnapshotMaxSizeSetRequest\x1a\x16.google.protobuf.Empty\x12\x66\n\x0eVolumeSnapshot\x12&.pkg.imrpc.EngineVolumeSnapshotRequest\x1a,.pkg.imrpc.EngineVolumeSnapshotProxyResponse\x12Y\n\x0cSnapshotList\x12\x1d.pkg.imrpc.ProxyEngineRequest\x1a*.pkg.imrpc.EngineSnapshotListProxyResponse\x12P\n\x0eSnapshotRevert\x12&.pkg.imrpc.EngineSnapshotRevertRequest\x1a\x16.google.protobuf.Empty\x12N\n\rSnapshotPurge\x12%.pkg.imrpc.EngineSnapshotPurgeRequest\x1a\x16.google.protobuf.Empty\x12g\n\x13SnapshotPurgeStatus\x12\x1d.pkg.imrpc.ProxyEngineRequest\x1a\x31.pkg.imrpc.EngineSnapshotPurgeStatusProxyResponse\x12N\n\rSnapshotClone\x12%.pkg.imrpc.EngineSnapshotCloneRequest\x1a\x16.google.protobuf.Empty\x12g\n\x13SnapshotCloneStatus\x12\x1d.pkg.imrpc.ProxyEngineRequest\x1a\x31.pkg.imrpc.EngineSnapshotCloneStatusProxyResponse\x12P\n\x0eSnapshotRemove\x12&.pkg.imrpc.EngineSnapshotRemoveRequest\x1a\x16.google.protobuf.Empty\x12L\n\x0cSnapshotHash\x12$.pkg.imrpc.EngineSnapshotHashRequest\x1a\x16.google.protobuf.Empty\x12r\n\x12SnapshotHashStatus\x12*.pkg.imrpc.EngineSnapshotHashStatusRequest\x1a\x30.pkg.imrpc.EngineSnapshotHashStatusProxyResponse\x12\x66\n\x0eSnapshotBackup\x12&.pkg.imrpc.EngineSnapshotBackupRequest\x1a,.pkg.imrpc.EngineSnapshotBackupProxyResponse\x12x\n\x14SnapshotBackupStatus\x12,.pkg.imrpc.EngineSnapshotBackupStatusRequest\x1a\x32.pkg.imrpc.EngineSnapshotBackupStatusProxyResponse\x12\x63\n\rBackupRestore\x12%.pkg.imrpc.EngineBackupRestoreRequest\x1a+.pkg.imrpc.EngineBackupRestoreProxyResponse\x12g\n\x13\x42\x61\x63kupRestoreStatus\x12\x1d.pkg.imrpc.ProxyEngineRequest\x1a\x31.pkg.imrpc.EngineBackupRestoreStatusProxyResponse\x12Z\n\x13\x42\x61\x63kupRestoreFinish\x12+.pkg.imrpc.EngineBackupRestoreFinishRequest\x1a\x16.google.protobuf.Empty\x12J\n\x18\x43leanupBackupMountPoints\x12\x16.google.protobuf.Empty\x1a\x16.google.protobuf.Empty\x12H\n\nReplicaAdd\x12\".pkg.imrpc.EngineReplicaAddRequest\x1a\x16.google.protobuf.Empty\x12W\n\x0bReplicaList\x12\x1d.pkg.imrpc.ProxyEngineRequest\x1a).pkg.imrpc.EngineReplicaListProxyResponse\x12l\n\x17ReplicaRebuildingStatus\x12\x1d.pkg.imrpc.ProxyEngineRequest\x1a\x32.pkg.imrpc.EngineReplicaRebuildStatusProxyResponse\x12\\\n\x14ReplicaVerifyRebuild\x12,.pkg.imrpc.EngineReplicaVerifyRebuildRequest\x1a\x16.google.protobuf.Empty\x12N\n\rReplicaRemove\x12%.pkg.imrpc.EngineReplicaRemoveRequest\x1a\x16.google.protobuf.Empty\x12V\n\x11ReplicaModeUpdate\x12).pkg.imrpc.EngineReplicaModeUpdateRequest\x1a\x16.google.protobuf.Empty\x12U\n\nMetricsGet\x12\x1d.pkg.imrpc.ProxyEngineRequest\x1a(.pkg.imrpc.EngineMetricsGetProxyResponse\x12P\n\x15RemountReadOnlyVolume\x12\x1f.pkg.imrpc.RemountVolumeRequest\x1a\x16.google.protobuf.EmptyB2Z0github.com/longhorn/longhorn-interface/pkg/imrpcb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'pkg.imrpc.proxy_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z0github.com/longhorn/longhorn-interface/pkg/imrpc'
  _PROXYENGINEREQUEST.fields_by_name['backend_store_driver']._options = None
  _PROXYENGINEREQUEST.fields_by_name['backend_store_driver']._serialized_options = b'\030\001'
  _ENGINESNAPSHOTLISTPROXYRESPONSE_DISKSENTRY._options = None
  _ENGINESNAPSHOTLISTPROXYRESPONSE_DISKSENTRY._serialized_options = b'8\001'
  _ENGINESNAPSHOTDISKINFO_CHILDRENENTRY._options = None
  _ENGINESNAPSHOTDISKINFO_CHILDRENENTRY._serialized_options = b'8\001'
  _ENGINESNAPSHOTDISKINFO_LABELSENTRY._options = None
  _ENGINESNAPSHOTDISKINFO_LABELSENTRY._serialized_options = b'8\001'
  _ENGINESNAPSHOTPURGESTATUSPROXYRESPONSE_STATUSENTRY._options = None
  _ENGINESNAPSHOTPURGESTATUSPROXYRESPONSE_STATUSENTRY._serialized_options = b'8\001'
  _ENGINESNAPSHOTCLONESTATUSPROXYRESPONSE_STATUSENTRY._options = None
  _ENGINESNAPSHOTCLONESTATUSPROXYRESPONSE_STATUSENTRY._serialized_options = b'8\001'
  _ENGINESNAPSHOTBACKUPREQUEST_LABELSENTRY._options = None
  _ENGINESNAPSHOTBACKUPREQUEST_LABELSENTRY._serialized_options = b'8\001'
  _ENGINEBACKUPRESTORESTATUSPROXYRESPONSE_STATUSENTRY._options = None
  _ENGINEBACKUPRESTORESTATUSPROXYRESPONSE_STATUSENTRY._serialized_options = b'8\001'
  _ENGINEREPLICAREBUILDSTATUSPROXYRESPONSE_STATUSENTRY._options = None
  _ENGINEREPLICAREBUILDSTATUSPROXYRESPONSE_STATUSENTRY._serialized_options = b'8\001'
  _ENGINESNAPSHOTHASHSTATUSPROXYRESPONSE_STATUSENTRY._options = None
  _ENGINESNAPSHOTHASHSTATUSPROXYRESPONSE_STATUSENTRY._serialized_options = b'8\001'
  _globals['_PROXYENGINEREQUEST']._serialized_start=153
  _globals['_PROXYENGINEREQUEST']._serialized_end=341
  _globals['_ENGINEVERSIONPROXYRESPONSE']._serialized_start=343
  _globals['_ENGINEVERSIONPROXYRESPONSE']._serialized_end=418
  _globals['_ENGINEVOLUMEGETPROXYRESPONSE']._serialized_start=420
  _globals['_ENGINEVOLUMEGETPROXYRESPONSE']._serialized_end=489
  _globals['_ENGINEVOLUMEEXPANDREQUEST']._serialized_start=492
  _globals['_ENGINEVOLUMEEXPANDREQUEST']._serialized_end=632
  _globals['_ENGINEVOLUMEFRONTENDSTARTREQUEST']._serialized_start=635
  _globals['_ENGINEVOLUMEFRONTENDSTARTREQUEST']._serialized_end=797
  _globals['_ENGINEVOLUMESNAPSHOTREQUEST']._serialized_start=800
  _globals['_ENGINEVOLUMESNAPSHOTREQUEST']._serialized_end=953
  _globals['_ENGINEVOLUMESNAPSHOTPROXYRESPONSE']._serialized_start=955
  _globals['_ENGINEVOLUMESNAPSHOTPROXYRESPONSE']._serialized_end=1044
  _globals['_ENGINEVOLUMEUNMAPMARKSNAPCHAINREMOVEDSETREQUEST']._serialized_start=1047
  _globals['_ENGINEVOLUMEUNMAPMARKSNAPCHAINREMOVEDSETREQUEST']._serialized_end=1240
  _globals['_ENGINEVOLUMESNAPSHOTMAXCOUNTSETREQUEST']._serialized_start=1243
  _globals['_ENGINEVOLUMESNAPSHOTMAXCOUNTSETREQUEST']._serialized_end=1408
  _globals['_ENGINEVOLUMESNAPSHOTMAXSIZESETREQUEST']._serialized_start=1411
  _globals['_ENGINEVOLUMESNAPSHOTMAXSIZESETREQUEST']._serialized_end=1573
  _globals['_ENGINESNAPSHOTLISTPROXYRESPONSE']._serialized_start=1576
  _globals['_ENGINESNAPSHOTLISTPROXYRESPONSE']._serialized_end=1760
  _globals['_ENGINESNAPSHOTLISTPROXYRESPONSE_DISKSENTRY']._serialized_start=1681
  _globals['_ENGINESNAPSHOTLISTPROXYRESPONSE_DISKSENTRY']._serialized_end=1760
  _globals['_ENGINESNAPSHOTDISKINFO']._serialized_start=1763
  _globals['_ENGINESNAPSHOTDISKINFO']._serialized_end=2113
  _globals['_ENGINESNAPSHOTDISKINFO_CHILDRENENTRY']._serialized_start=2019
  _globals['_ENGINESNAPSHOTDISKINFO_CHILDRENENTRY']._serialized_end=2066
  _globals['_ENGINESNAPSHOTDISKINFO_LABELSENTRY']._serialized_start=2068
  _globals['_ENGINESNAPSHOTDISKINFO_LABELSENTRY']._serialized_end=2113
  _globals['_ENGINESNAPSHOTREVERTREQUEST']._serialized_start=2115
  _globals['_ENGINESNAPSHOTREVERTREQUEST']._serialized_end=2219
  _globals['_ENGINESNAPSHOTPURGEREQUEST']._serialized_start=2221
  _globals['_ENGINESNAPSHOTPURGEREQUEST']._serialized_end=2339
  _globals['_ENGINESNAPSHOTPURGESTATUSPROXYRESPONSE']._serialized_start=2342
  _globals['_ENGINESNAPSHOTPURGESTATUSPROXYRESPONSE']._serialized_end=2552
  _globals['_ENGINESNAPSHOTPURGESTATUSPROXYRESPONSE_STATUSENTRY']._serialized_start=2463
  _globals['_ENGINESNAPSHOTPURGESTATUSPROXYRESPONSE_STATUSENTRY']._serialized_end=2552
  _globals['_ENGINESNAPSHOTCLONEREQUEST']._serialized_start=2555
  _globals['_ENGINESNAPSHOTCLONEREQUEST']._serialized_end=2826
  _globals['_ENGINESNAPSHOTCLONESTATUSPROXYRESPONSE']._serialized_start=2829
  _globals['_ENGINESNAPSHOTCLONESTATUSPROXYRESPONSE']._serialized_end=3039
  _globals['_ENGINESNAPSHOTCLONESTATUSPROXYRESPONSE_STATUSENTRY']._serialized_start=2950
  _globals['_ENGINESNAPSHOTCLONESTATUSPROXYRESPONSE_STATUSENTRY']._serialized_end=3039
  _globals['_ENGINESNAPSHOTREMOVEREQUEST']._serialized_start=3041
  _globals['_ENGINESNAPSHOTREMOVEREQUEST']._serialized_end=3146
  _globals['_ENGINESNAPSHOTBACKUPREQUEST']._serialized_start=3149
  _globals['_ENGINESNAPSHOTBACKUPREQUEST']._serialized_end=3577
  _globals['_ENGINESNAPSHOTBACKUPREQUEST_LABELSENTRY']._serialized_start=2068
  _globals['_ENGINESNAPSHOTBACKUPREQUEST_LABELSENTRY']._serialized_end=2113
  _globals['_ENGINESNAPSHOTBACKUPPROXYRESPONSE']._serialized_start=3579
  _globals['_ENGINESNAPSHOTBACKUPPROXYRESPONSE']._serialized_end=3674
  _globals['_ENGINESNAPSHOTBACKUPSTATUSREQUEST']._serialized_start=3677
  _globals['_ENGINESNAPSHOTBACKUPSTATUSREQUEST']._serialized_end=3841
  _globals['_ENGINESNAPSHOTBACKUPSTATUSPROXYRESPONSE']._serialized_start=3844
  _globals['_ENGINESNAPSHOTBACKUPSTATUSPROXYRESPONSE']._serialized_end=4001
  _globals['_ENGINEBACKUPRESTOREREQUEST']._serialized_start=4004
  _globals['_ENGINEBACKUPRESTOREREQUEST']._serialized_end=4183
  _globals['_ENGINEBACKUPRESTOREPROXYRESPONSE']._serialized_start=4185
  _globals['_ENGINEBACKUPRESTOREPROXYRESPONSE']._serialized_end=4238
  _globals['_ENGINEBACKUPRESTORESTATUSPROXYRESPONSE']._serialized_start=4241
  _globals['_ENGINEBACKUPRESTORESTATUSPROXYRESPONSE']._serialized_end=4445
  _globals['_ENGINEBACKUPRESTORESTATUSPROXYRESPONSE_STATUSENTRY']._serialized_start=4362
  _globals['_ENGINEBACKUPRESTORESTATUSPROXYRESPONSE_STATUSENTRY']._serialized_end=4445
  _globals['_ENGINEBACKUPRESTORESTATUS']._serialized_start=4448
  _globals['_ENGINEBACKUPRESTORESTATUS']._serialized_end=4640
  _globals['_ENGINEBACKUPRESTOREFINISHREQUEST']._serialized_start=4642
  _globals['_ENGINEBACKUPRESTOREFINISHREQUEST']._serialized_end=4737
  _globals['_ENGINEREPLICAADDREQUEST']._serialized_start=4740
  _globals['_ENGINEREPLICAADDREQUEST']._serialized_end=4984
  _globals['_ENGINEREPLICALISTPROXYRESPONSE']._serialized_start=4986
  _globals['_ENGINEREPLICALISTPROXYRESPONSE']._serialized_end=5073
  _globals['_ENGINEREPLICAVERIFYREBUILDREQUEST']._serialized_start=5076
  _globals['_ENGINEREPLICAVERIFYREBUILDREQUEST']._serialized_end=5219
  _globals['_ENGINEREPLICAREBUILDSTATUSPROXYRESPONSE']._serialized_start=5222
  _globals['_ENGINEREPLICAREBUILDSTATUSPROXYRESPONSE']._serialized_end=5435
  _globals['_ENGINEREPLICAREBUILDSTATUSPROXYRESPONSE_STATUSENTRY']._serialized_start=5345
  _globals['_ENGINEREPLICAREBUILDSTATUSPROXYRESPONSE_STATUSENTRY']._serialized_end=5435
  _globals['_ENGINEREPLICAREMOVEREQUEST']._serialized_start=5438
  _globals['_ENGINEREPLICAREMOVEREQUEST']._serialized_end=5574
  _globals['_ENGINEREPLICAMODEUPDATEREQUEST']._serialized_start=5577
  _globals['_ENGINEREPLICAMODEUPDATEREQUEST']._serialized_end=5737
  _globals['_ENGINESNAPSHOTHASHREQUEST']._serialized_start=5739
  _globals['_ENGINESNAPSHOTHASHREQUEST']._serialized_end=5866
  _globals['_ENGINESNAPSHOTHASHSTATUSREQUEST']._serialized_start=5868
  _globals['_ENGINESNAPSHOTHASHSTATUSREQUEST']._serialized_end=5985
  _globals['_ENGINESNAPSHOTHASHSTATUSPROXYRESPONSE']._serialized_start=5988
  _globals['_ENGINESNAPSHOTHASHSTATUSPROXYRESPONSE']._serialized_end=6195
  _globals['_ENGINESNAPSHOTHASHSTATUSPROXYRESPONSE_STATUSENTRY']._serialized_start=6107
  _globals['_ENGINESNAPSHOTHASHSTATUSPROXYRESPONSE_STATUSENTRY']._serialized_end=6195
  _globals['_ENGINEMETRICSGETPROXYRESPONSE']._serialized_start=6197
  _globals['_ENGINEMETRICSGETPROXYRESPONSE']._serialized_end=6269
  _globals['_REMOUNTVOLUMEREQUEST']._serialized_start=6271
  _globals['_REMOUNTVOLUMEREQUEST']._serialized_end=6314
  _globals['_PROXYENGINESERVICE']._serialized_start=6317
  _globals['_PROXYENGINESERVICE']._serialized_end=9318
# @@protoc_insertion_point(module_scope)