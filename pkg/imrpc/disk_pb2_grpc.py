# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from pkg.imrpc import disk_pb2 as pkg_dot_imrpc_dot_disk__pb2


class DiskServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.DiskCreate = channel.unary_unary(
                '/pkg.imrpc.DiskService/DiskCreate',
                request_serializer=pkg_dot_imrpc_dot_disk__pb2.DiskCreateRequest.SerializeToString,
                response_deserializer=pkg_dot_imrpc_dot_disk__pb2.Disk.FromString,
                )
        self.DiskDelete = channel.unary_unary(
                '/pkg.imrpc.DiskService/DiskDelete',
                request_serializer=pkg_dot_imrpc_dot_disk__pb2.DiskDeleteRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.DiskGet = channel.unary_unary(
                '/pkg.imrpc.DiskService/DiskGet',
                request_serializer=pkg_dot_imrpc_dot_disk__pb2.DiskGetRequest.SerializeToString,
                response_deserializer=pkg_dot_imrpc_dot_disk__pb2.Disk.FromString,
                )
        self.DiskReplicaInstanceList = channel.unary_unary(
                '/pkg.imrpc.DiskService/DiskReplicaInstanceList',
                request_serializer=pkg_dot_imrpc_dot_disk__pb2.DiskReplicaInstanceListRequest.SerializeToString,
                response_deserializer=pkg_dot_imrpc_dot_disk__pb2.DiskReplicaInstanceListResponse.FromString,
                )
        self.DiskReplicaInstanceDelete = channel.unary_unary(
                '/pkg.imrpc.DiskService/DiskReplicaInstanceDelete',
                request_serializer=pkg_dot_imrpc_dot_disk__pb2.DiskReplicaInstanceDeleteRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.VersionGet = channel.unary_unary(
                '/pkg.imrpc.DiskService/VersionGet',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=pkg_dot_imrpc_dot_disk__pb2.DiskVersionResponse.FromString,
                )


class DiskServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def DiskCreate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DiskDelete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DiskGet(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DiskReplicaInstanceList(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DiskReplicaInstanceDelete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def VersionGet(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DiskServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'DiskCreate': grpc.unary_unary_rpc_method_handler(
                    servicer.DiskCreate,
                    request_deserializer=pkg_dot_imrpc_dot_disk__pb2.DiskCreateRequest.FromString,
                    response_serializer=pkg_dot_imrpc_dot_disk__pb2.Disk.SerializeToString,
            ),
            'DiskDelete': grpc.unary_unary_rpc_method_handler(
                    servicer.DiskDelete,
                    request_deserializer=pkg_dot_imrpc_dot_disk__pb2.DiskDeleteRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'DiskGet': grpc.unary_unary_rpc_method_handler(
                    servicer.DiskGet,
                    request_deserializer=pkg_dot_imrpc_dot_disk__pb2.DiskGetRequest.FromString,
                    response_serializer=pkg_dot_imrpc_dot_disk__pb2.Disk.SerializeToString,
            ),
            'DiskReplicaInstanceList': grpc.unary_unary_rpc_method_handler(
                    servicer.DiskReplicaInstanceList,
                    request_deserializer=pkg_dot_imrpc_dot_disk__pb2.DiskReplicaInstanceListRequest.FromString,
                    response_serializer=pkg_dot_imrpc_dot_disk__pb2.DiskReplicaInstanceListResponse.SerializeToString,
            ),
            'DiskReplicaInstanceDelete': grpc.unary_unary_rpc_method_handler(
                    servicer.DiskReplicaInstanceDelete,
                    request_deserializer=pkg_dot_imrpc_dot_disk__pb2.DiskReplicaInstanceDeleteRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'VersionGet': grpc.unary_unary_rpc_method_handler(
                    servicer.VersionGet,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=pkg_dot_imrpc_dot_disk__pb2.DiskVersionResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'pkg.imrpc.DiskService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DiskService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def DiskCreate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pkg.imrpc.DiskService/DiskCreate',
            pkg_dot_imrpc_dot_disk__pb2.DiskCreateRequest.SerializeToString,
            pkg_dot_imrpc_dot_disk__pb2.Disk.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DiskDelete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pkg.imrpc.DiskService/DiskDelete',
            pkg_dot_imrpc_dot_disk__pb2.DiskDeleteRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DiskGet(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pkg.imrpc.DiskService/DiskGet',
            pkg_dot_imrpc_dot_disk__pb2.DiskGetRequest.SerializeToString,
            pkg_dot_imrpc_dot_disk__pb2.Disk.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DiskReplicaInstanceList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pkg.imrpc.DiskService/DiskReplicaInstanceList',
            pkg_dot_imrpc_dot_disk__pb2.DiskReplicaInstanceListRequest.SerializeToString,
            pkg_dot_imrpc_dot_disk__pb2.DiskReplicaInstanceListResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DiskReplicaInstanceDelete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pkg.imrpc.DiskService/DiskReplicaInstanceDelete',
            pkg_dot_imrpc_dot_disk__pb2.DiskReplicaInstanceDeleteRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def VersionGet(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pkg.imrpc.DiskService/VersionGet',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            pkg_dot_imrpc_dot_disk__pb2.DiskVersionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)