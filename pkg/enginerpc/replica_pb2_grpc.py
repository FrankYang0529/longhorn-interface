# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from pkg.enginerpc import replica_pb2 as pkg_dot_enginerpc_dot_replica__pb2


class ReplicaServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ReplicaCreate = channel.unary_unary(
                '/pkg.enginerpc.ReplicaService/ReplicaCreate',
                request_serializer=pkg_dot_enginerpc_dot_replica__pb2.ReplicaCreateRequest.SerializeToString,
                response_deserializer=pkg_dot_enginerpc_dot_replica__pb2.ReplicaCreateResponse.FromString,
                )
        self.ReplicaDelete = channel.unary_unary(
                '/pkg.enginerpc.ReplicaService/ReplicaDelete',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.ReplicaGet = channel.unary_unary(
                '/pkg.enginerpc.ReplicaService/ReplicaGet',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=pkg_dot_enginerpc_dot_replica__pb2.ReplicaGetResponse.FromString,
                )
        self.ReplicaOpen = channel.unary_unary(
                '/pkg.enginerpc.ReplicaService/ReplicaOpen',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=pkg_dot_enginerpc_dot_replica__pb2.ReplicaOpenResponse.FromString,
                )
        self.ReplicaClose = channel.unary_unary(
                '/pkg.enginerpc.ReplicaService/ReplicaClose',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=pkg_dot_enginerpc_dot_replica__pb2.ReplicaCloseResponse.FromString,
                )
        self.ReplicaReload = channel.unary_unary(
                '/pkg.enginerpc.ReplicaService/ReplicaReload',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=pkg_dot_enginerpc_dot_replica__pb2.ReplicaReloadResponse.FromString,
                )
        self.ReplicaRevert = channel.unary_unary(
                '/pkg.enginerpc.ReplicaService/ReplicaRevert',
                request_serializer=pkg_dot_enginerpc_dot_replica__pb2.ReplicaRevertRequest.SerializeToString,
                response_deserializer=pkg_dot_enginerpc_dot_replica__pb2.ReplicaRevertResponse.FromString,
                )
        self.ReplicaSnapshot = channel.unary_unary(
                '/pkg.enginerpc.ReplicaService/ReplicaSnapshot',
                request_serializer=pkg_dot_enginerpc_dot_replica__pb2.ReplicaSnapshotRequest.SerializeToString,
                response_deserializer=pkg_dot_enginerpc_dot_replica__pb2.ReplicaSnapshotResponse.FromString,
                )
        self.ReplicaExpand = channel.unary_unary(
                '/pkg.enginerpc.ReplicaService/ReplicaExpand',
                request_serializer=pkg_dot_enginerpc_dot_replica__pb2.ReplicaExpandRequest.SerializeToString,
                response_deserializer=pkg_dot_enginerpc_dot_replica__pb2.ReplicaExpandResponse.FromString,
                )
        self.DiskRemove = channel.unary_unary(
                '/pkg.enginerpc.ReplicaService/DiskRemove',
                request_serializer=pkg_dot_enginerpc_dot_replica__pb2.DiskRemoveRequest.SerializeToString,
                response_deserializer=pkg_dot_enginerpc_dot_replica__pb2.DiskRemoveResponse.FromString,
                )
        self.DiskReplace = channel.unary_unary(
                '/pkg.enginerpc.ReplicaService/DiskReplace',
                request_serializer=pkg_dot_enginerpc_dot_replica__pb2.DiskReplaceRequest.SerializeToString,
                response_deserializer=pkg_dot_enginerpc_dot_replica__pb2.DiskReplaceResponse.FromString,
                )
        self.DiskPrepareRemove = channel.unary_unary(
                '/pkg.enginerpc.ReplicaService/DiskPrepareRemove',
                request_serializer=pkg_dot_enginerpc_dot_replica__pb2.DiskPrepareRemoveRequest.SerializeToString,
                response_deserializer=pkg_dot_enginerpc_dot_replica__pb2.DiskPrepareRemoveResponse.FromString,
                )
        self.DiskMarkAsRemoved = channel.unary_unary(
                '/pkg.enginerpc.ReplicaService/DiskMarkAsRemoved',
                request_serializer=pkg_dot_enginerpc_dot_replica__pb2.DiskMarkAsRemovedRequest.SerializeToString,
                response_deserializer=pkg_dot_enginerpc_dot_replica__pb2.DiskMarkAsRemovedResponse.FromString,
                )
        self.RebuildingSet = channel.unary_unary(
                '/pkg.enginerpc.ReplicaService/RebuildingSet',
                request_serializer=pkg_dot_enginerpc_dot_replica__pb2.RebuildingSetRequest.SerializeToString,
                response_deserializer=pkg_dot_enginerpc_dot_replica__pb2.RebuildingSetResponse.FromString,
                )
        self.RevisionCounterSet = channel.unary_unary(
                '/pkg.enginerpc.ReplicaService/RevisionCounterSet',
                request_serializer=pkg_dot_enginerpc_dot_replica__pb2.RevisionCounterSetRequest.SerializeToString,
                response_deserializer=pkg_dot_enginerpc_dot_replica__pb2.RevisionCounterSetResponse.FromString,
                )
        self.UnmapMarkDiskChainRemovedSet = channel.unary_unary(
                '/pkg.enginerpc.ReplicaService/UnmapMarkDiskChainRemovedSet',
                request_serializer=pkg_dot_enginerpc_dot_replica__pb2.UnmapMarkDiskChainRemovedSetRequest.SerializeToString,
                response_deserializer=pkg_dot_enginerpc_dot_replica__pb2.UnmapMarkDiskChainRemovedSetResponse.FromString,
                )
        self.SnapshotMaxCountSet = channel.unary_unary(
                '/pkg.enginerpc.ReplicaService/SnapshotMaxCountSet',
                request_serializer=pkg_dot_enginerpc_dot_replica__pb2.SnapshotMaxCountSetRequest.SerializeToString,
                response_deserializer=pkg_dot_enginerpc_dot_replica__pb2.SnapshotMaxCountSetResponse.FromString,
                )
        self.SnapshotMaxSizeSet = channel.unary_unary(
                '/pkg.enginerpc.ReplicaService/SnapshotMaxSizeSet',
                request_serializer=pkg_dot_enginerpc_dot_replica__pb2.SnapshotMaxSizeSetRequest.SerializeToString,
                response_deserializer=pkg_dot_enginerpc_dot_replica__pb2.SnapshotMaxSizeSetResponse.FromString,
                )


class ReplicaServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ReplicaCreate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReplicaDelete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReplicaGet(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReplicaOpen(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReplicaClose(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReplicaReload(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReplicaRevert(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReplicaSnapshot(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReplicaExpand(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DiskRemove(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DiskReplace(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DiskPrepareRemove(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DiskMarkAsRemoved(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RebuildingSet(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RevisionCounterSet(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UnmapMarkDiskChainRemovedSet(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SnapshotMaxCountSet(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SnapshotMaxSizeSet(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ReplicaServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ReplicaCreate': grpc.unary_unary_rpc_method_handler(
                    servicer.ReplicaCreate,
                    request_deserializer=pkg_dot_enginerpc_dot_replica__pb2.ReplicaCreateRequest.FromString,
                    response_serializer=pkg_dot_enginerpc_dot_replica__pb2.ReplicaCreateResponse.SerializeToString,
            ),
            'ReplicaDelete': grpc.unary_unary_rpc_method_handler(
                    servicer.ReplicaDelete,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'ReplicaGet': grpc.unary_unary_rpc_method_handler(
                    servicer.ReplicaGet,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=pkg_dot_enginerpc_dot_replica__pb2.ReplicaGetResponse.SerializeToString,
            ),
            'ReplicaOpen': grpc.unary_unary_rpc_method_handler(
                    servicer.ReplicaOpen,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=pkg_dot_enginerpc_dot_replica__pb2.ReplicaOpenResponse.SerializeToString,
            ),
            'ReplicaClose': grpc.unary_unary_rpc_method_handler(
                    servicer.ReplicaClose,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=pkg_dot_enginerpc_dot_replica__pb2.ReplicaCloseResponse.SerializeToString,
            ),
            'ReplicaReload': grpc.unary_unary_rpc_method_handler(
                    servicer.ReplicaReload,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=pkg_dot_enginerpc_dot_replica__pb2.ReplicaReloadResponse.SerializeToString,
            ),
            'ReplicaRevert': grpc.unary_unary_rpc_method_handler(
                    servicer.ReplicaRevert,
                    request_deserializer=pkg_dot_enginerpc_dot_replica__pb2.ReplicaRevertRequest.FromString,
                    response_serializer=pkg_dot_enginerpc_dot_replica__pb2.ReplicaRevertResponse.SerializeToString,
            ),
            'ReplicaSnapshot': grpc.unary_unary_rpc_method_handler(
                    servicer.ReplicaSnapshot,
                    request_deserializer=pkg_dot_enginerpc_dot_replica__pb2.ReplicaSnapshotRequest.FromString,
                    response_serializer=pkg_dot_enginerpc_dot_replica__pb2.ReplicaSnapshotResponse.SerializeToString,
            ),
            'ReplicaExpand': grpc.unary_unary_rpc_method_handler(
                    servicer.ReplicaExpand,
                    request_deserializer=pkg_dot_enginerpc_dot_replica__pb2.ReplicaExpandRequest.FromString,
                    response_serializer=pkg_dot_enginerpc_dot_replica__pb2.ReplicaExpandResponse.SerializeToString,
            ),
            'DiskRemove': grpc.unary_unary_rpc_method_handler(
                    servicer.DiskRemove,
                    request_deserializer=pkg_dot_enginerpc_dot_replica__pb2.DiskRemoveRequest.FromString,
                    response_serializer=pkg_dot_enginerpc_dot_replica__pb2.DiskRemoveResponse.SerializeToString,
            ),
            'DiskReplace': grpc.unary_unary_rpc_method_handler(
                    servicer.DiskReplace,
                    request_deserializer=pkg_dot_enginerpc_dot_replica__pb2.DiskReplaceRequest.FromString,
                    response_serializer=pkg_dot_enginerpc_dot_replica__pb2.DiskReplaceResponse.SerializeToString,
            ),
            'DiskPrepareRemove': grpc.unary_unary_rpc_method_handler(
                    servicer.DiskPrepareRemove,
                    request_deserializer=pkg_dot_enginerpc_dot_replica__pb2.DiskPrepareRemoveRequest.FromString,
                    response_serializer=pkg_dot_enginerpc_dot_replica__pb2.DiskPrepareRemoveResponse.SerializeToString,
            ),
            'DiskMarkAsRemoved': grpc.unary_unary_rpc_method_handler(
                    servicer.DiskMarkAsRemoved,
                    request_deserializer=pkg_dot_enginerpc_dot_replica__pb2.DiskMarkAsRemovedRequest.FromString,
                    response_serializer=pkg_dot_enginerpc_dot_replica__pb2.DiskMarkAsRemovedResponse.SerializeToString,
            ),
            'RebuildingSet': grpc.unary_unary_rpc_method_handler(
                    servicer.RebuildingSet,
                    request_deserializer=pkg_dot_enginerpc_dot_replica__pb2.RebuildingSetRequest.FromString,
                    response_serializer=pkg_dot_enginerpc_dot_replica__pb2.RebuildingSetResponse.SerializeToString,
            ),
            'RevisionCounterSet': grpc.unary_unary_rpc_method_handler(
                    servicer.RevisionCounterSet,
                    request_deserializer=pkg_dot_enginerpc_dot_replica__pb2.RevisionCounterSetRequest.FromString,
                    response_serializer=pkg_dot_enginerpc_dot_replica__pb2.RevisionCounterSetResponse.SerializeToString,
            ),
            'UnmapMarkDiskChainRemovedSet': grpc.unary_unary_rpc_method_handler(
                    servicer.UnmapMarkDiskChainRemovedSet,
                    request_deserializer=pkg_dot_enginerpc_dot_replica__pb2.UnmapMarkDiskChainRemovedSetRequest.FromString,
                    response_serializer=pkg_dot_enginerpc_dot_replica__pb2.UnmapMarkDiskChainRemovedSetResponse.SerializeToString,
            ),
            'SnapshotMaxCountSet': grpc.unary_unary_rpc_method_handler(
                    servicer.SnapshotMaxCountSet,
                    request_deserializer=pkg_dot_enginerpc_dot_replica__pb2.SnapshotMaxCountSetRequest.FromString,
                    response_serializer=pkg_dot_enginerpc_dot_replica__pb2.SnapshotMaxCountSetResponse.SerializeToString,
            ),
            'SnapshotMaxSizeSet': grpc.unary_unary_rpc_method_handler(
                    servicer.SnapshotMaxSizeSet,
                    request_deserializer=pkg_dot_enginerpc_dot_replica__pb2.SnapshotMaxSizeSetRequest.FromString,
                    response_serializer=pkg_dot_enginerpc_dot_replica__pb2.SnapshotMaxSizeSetResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'pkg.enginerpc.ReplicaService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ReplicaService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ReplicaCreate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pkg.enginerpc.ReplicaService/ReplicaCreate',
            pkg_dot_enginerpc_dot_replica__pb2.ReplicaCreateRequest.SerializeToString,
            pkg_dot_enginerpc_dot_replica__pb2.ReplicaCreateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReplicaDelete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pkg.enginerpc.ReplicaService/ReplicaDelete',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReplicaGet(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pkg.enginerpc.ReplicaService/ReplicaGet',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            pkg_dot_enginerpc_dot_replica__pb2.ReplicaGetResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReplicaOpen(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pkg.enginerpc.ReplicaService/ReplicaOpen',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            pkg_dot_enginerpc_dot_replica__pb2.ReplicaOpenResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReplicaClose(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pkg.enginerpc.ReplicaService/ReplicaClose',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            pkg_dot_enginerpc_dot_replica__pb2.ReplicaCloseResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReplicaReload(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pkg.enginerpc.ReplicaService/ReplicaReload',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            pkg_dot_enginerpc_dot_replica__pb2.ReplicaReloadResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReplicaRevert(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pkg.enginerpc.ReplicaService/ReplicaRevert',
            pkg_dot_enginerpc_dot_replica__pb2.ReplicaRevertRequest.SerializeToString,
            pkg_dot_enginerpc_dot_replica__pb2.ReplicaRevertResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReplicaSnapshot(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pkg.enginerpc.ReplicaService/ReplicaSnapshot',
            pkg_dot_enginerpc_dot_replica__pb2.ReplicaSnapshotRequest.SerializeToString,
            pkg_dot_enginerpc_dot_replica__pb2.ReplicaSnapshotResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReplicaExpand(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pkg.enginerpc.ReplicaService/ReplicaExpand',
            pkg_dot_enginerpc_dot_replica__pb2.ReplicaExpandRequest.SerializeToString,
            pkg_dot_enginerpc_dot_replica__pb2.ReplicaExpandResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DiskRemove(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pkg.enginerpc.ReplicaService/DiskRemove',
            pkg_dot_enginerpc_dot_replica__pb2.DiskRemoveRequest.SerializeToString,
            pkg_dot_enginerpc_dot_replica__pb2.DiskRemoveResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DiskReplace(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pkg.enginerpc.ReplicaService/DiskReplace',
            pkg_dot_enginerpc_dot_replica__pb2.DiskReplaceRequest.SerializeToString,
            pkg_dot_enginerpc_dot_replica__pb2.DiskReplaceResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DiskPrepareRemove(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pkg.enginerpc.ReplicaService/DiskPrepareRemove',
            pkg_dot_enginerpc_dot_replica__pb2.DiskPrepareRemoveRequest.SerializeToString,
            pkg_dot_enginerpc_dot_replica__pb2.DiskPrepareRemoveResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DiskMarkAsRemoved(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pkg.enginerpc.ReplicaService/DiskMarkAsRemoved',
            pkg_dot_enginerpc_dot_replica__pb2.DiskMarkAsRemovedRequest.SerializeToString,
            pkg_dot_enginerpc_dot_replica__pb2.DiskMarkAsRemovedResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RebuildingSet(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pkg.enginerpc.ReplicaService/RebuildingSet',
            pkg_dot_enginerpc_dot_replica__pb2.RebuildingSetRequest.SerializeToString,
            pkg_dot_enginerpc_dot_replica__pb2.RebuildingSetResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RevisionCounterSet(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pkg.enginerpc.ReplicaService/RevisionCounterSet',
            pkg_dot_enginerpc_dot_replica__pb2.RevisionCounterSetRequest.SerializeToString,
            pkg_dot_enginerpc_dot_replica__pb2.RevisionCounterSetResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UnmapMarkDiskChainRemovedSet(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pkg.enginerpc.ReplicaService/UnmapMarkDiskChainRemovedSet',
            pkg_dot_enginerpc_dot_replica__pb2.UnmapMarkDiskChainRemovedSetRequest.SerializeToString,
            pkg_dot_enginerpc_dot_replica__pb2.UnmapMarkDiskChainRemovedSetResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SnapshotMaxCountSet(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pkg.enginerpc.ReplicaService/SnapshotMaxCountSet',
            pkg_dot_enginerpc_dot_replica__pb2.SnapshotMaxCountSetRequest.SerializeToString,
            pkg_dot_enginerpc_dot_replica__pb2.SnapshotMaxCountSetResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SnapshotMaxSizeSet(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pkg.enginerpc.ReplicaService/SnapshotMaxSizeSet',
            pkg_dot_enginerpc_dot_replica__pb2.SnapshotMaxSizeSetRequest.SerializeToString,
            pkg_dot_enginerpc_dot_replica__pb2.SnapshotMaxSizeSetResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)