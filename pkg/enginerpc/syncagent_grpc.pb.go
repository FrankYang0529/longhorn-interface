// Code generated by protoc-gen-go-grpc. DO NOT EDIT.
// versions:
// - protoc-gen-go-grpc v1.3.0
// - protoc             v4.24.3
// source: pkg/enginerpc/syncagent.proto

package enginerpc

import (
	context "context"
	grpc "google.golang.org/grpc"
	codes "google.golang.org/grpc/codes"
	status "google.golang.org/grpc/status"
	emptypb "google.golang.org/protobuf/types/known/emptypb"
)

// This is a compile-time assertion to ensure that this generated file
// is compatible with the grpc package it is being compiled against.
// Requires gRPC-Go v1.32.0 or later.
const _ = grpc.SupportPackageIsVersion7

const (
	SyncAgentService_FileRemove_FullMethodName            = "/pkg.enginerpc.SyncAgentService/FileRemove"
	SyncAgentService_FileRename_FullMethodName            = "/pkg.enginerpc.SyncAgentService/FileRename"
	SyncAgentService_FileSend_FullMethodName              = "/pkg.enginerpc.SyncAgentService/FileSend"
	SyncAgentService_FilesSync_FullMethodName             = "/pkg.enginerpc.SyncAgentService/FilesSync"
	SyncAgentService_SnapshotClone_FullMethodName         = "/pkg.enginerpc.SyncAgentService/SnapshotClone"
	SyncAgentService_VolumeExport_FullMethodName          = "/pkg.enginerpc.SyncAgentService/VolumeExport"
	SyncAgentService_ReceiverLaunch_FullMethodName        = "/pkg.enginerpc.SyncAgentService/ReceiverLaunch"
	SyncAgentService_BackupCreate_FullMethodName          = "/pkg.enginerpc.SyncAgentService/BackupCreate"
	SyncAgentService_BackupRemove_FullMethodName          = "/pkg.enginerpc.SyncAgentService/BackupRemove"
	SyncAgentService_BackupRestore_FullMethodName         = "/pkg.enginerpc.SyncAgentService/BackupRestore"
	SyncAgentService_BackupStatus_FullMethodName          = "/pkg.enginerpc.SyncAgentService/BackupStatus"
	SyncAgentService_Reset_FullMethodName                 = "/pkg.enginerpc.SyncAgentService/Reset"
	SyncAgentService_RestoreStatus_FullMethodName         = "/pkg.enginerpc.SyncAgentService/RestoreStatus"
	SyncAgentService_SnapshotPurge_FullMethodName         = "/pkg.enginerpc.SyncAgentService/SnapshotPurge"
	SyncAgentService_SnapshotPurgeStatus_FullMethodName   = "/pkg.enginerpc.SyncAgentService/SnapshotPurgeStatus"
	SyncAgentService_ReplicaRebuildStatus_FullMethodName  = "/pkg.enginerpc.SyncAgentService/ReplicaRebuildStatus"
	SyncAgentService_SnapshotCloneStatus_FullMethodName   = "/pkg.enginerpc.SyncAgentService/SnapshotCloneStatus"
	SyncAgentService_SnapshotHash_FullMethodName          = "/pkg.enginerpc.SyncAgentService/SnapshotHash"
	SyncAgentService_SnapshotHashStatus_FullMethodName    = "/pkg.enginerpc.SyncAgentService/SnapshotHashStatus"
	SyncAgentService_SnapshotHashCancel_FullMethodName    = "/pkg.enginerpc.SyncAgentService/SnapshotHashCancel"
	SyncAgentService_SnapshotHashLockState_FullMethodName = "/pkg.enginerpc.SyncAgentService/SnapshotHashLockState"
)

// SyncAgentServiceClient is the client API for SyncAgentService service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream.
type SyncAgentServiceClient interface {
	FileRemove(ctx context.Context, in *FileRemoveRequest, opts ...grpc.CallOption) (*emptypb.Empty, error)
	FileRename(ctx context.Context, in *FileRenameRequest, opts ...grpc.CallOption) (*emptypb.Empty, error)
	FileSend(ctx context.Context, in *FileSendRequest, opts ...grpc.CallOption) (*emptypb.Empty, error)
	FilesSync(ctx context.Context, in *FilesSyncRequest, opts ...grpc.CallOption) (*emptypb.Empty, error)
	SnapshotClone(ctx context.Context, in *SnapshotCloneRequest, opts ...grpc.CallOption) (*emptypb.Empty, error)
	VolumeExport(ctx context.Context, in *VolumeExportRequest, opts ...grpc.CallOption) (*emptypb.Empty, error)
	ReceiverLaunch(ctx context.Context, in *ReceiverLaunchRequest, opts ...grpc.CallOption) (*ReceiverLaunchResponse, error)
	BackupCreate(ctx context.Context, in *BackupCreateRequest, opts ...grpc.CallOption) (*BackupCreateResponse, error)
	BackupRemove(ctx context.Context, in *BackupRemoveRequest, opts ...grpc.CallOption) (*emptypb.Empty, error)
	BackupRestore(ctx context.Context, in *BackupRestoreRequest, opts ...grpc.CallOption) (*emptypb.Empty, error)
	BackupStatus(ctx context.Context, in *BackupStatusRequest, opts ...grpc.CallOption) (*BackupStatusResponse, error)
	Reset(ctx context.Context, in *emptypb.Empty, opts ...grpc.CallOption) (*emptypb.Empty, error)
	RestoreStatus(ctx context.Context, in *emptypb.Empty, opts ...grpc.CallOption) (*RestoreStatusResponse, error)
	SnapshotPurge(ctx context.Context, in *emptypb.Empty, opts ...grpc.CallOption) (*emptypb.Empty, error)
	SnapshotPurgeStatus(ctx context.Context, in *emptypb.Empty, opts ...grpc.CallOption) (*SnapshotPurgeStatusResponse, error)
	ReplicaRebuildStatus(ctx context.Context, in *emptypb.Empty, opts ...grpc.CallOption) (*ReplicaRebuildStatusResponse, error)
	SnapshotCloneStatus(ctx context.Context, in *emptypb.Empty, opts ...grpc.CallOption) (*SnapshotCloneStatusResponse, error)
	SnapshotHash(ctx context.Context, in *SnapshotHashRequest, opts ...grpc.CallOption) (*emptypb.Empty, error)
	SnapshotHashStatus(ctx context.Context, in *SnapshotHashStatusRequest, opts ...grpc.CallOption) (*SnapshotHashStatusResponse, error)
	SnapshotHashCancel(ctx context.Context, in *SnapshotHashCancelRequest, opts ...grpc.CallOption) (*emptypb.Empty, error)
	SnapshotHashLockState(ctx context.Context, in *emptypb.Empty, opts ...grpc.CallOption) (*SnapshotHashLockStateResponse, error)
}

type syncAgentServiceClient struct {
	cc grpc.ClientConnInterface
}

func NewSyncAgentServiceClient(cc grpc.ClientConnInterface) SyncAgentServiceClient {
	return &syncAgentServiceClient{cc}
}

func (c *syncAgentServiceClient) FileRemove(ctx context.Context, in *FileRemoveRequest, opts ...grpc.CallOption) (*emptypb.Empty, error) {
	out := new(emptypb.Empty)
	err := c.cc.Invoke(ctx, SyncAgentService_FileRemove_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *syncAgentServiceClient) FileRename(ctx context.Context, in *FileRenameRequest, opts ...grpc.CallOption) (*emptypb.Empty, error) {
	out := new(emptypb.Empty)
	err := c.cc.Invoke(ctx, SyncAgentService_FileRename_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *syncAgentServiceClient) FileSend(ctx context.Context, in *FileSendRequest, opts ...grpc.CallOption) (*emptypb.Empty, error) {
	out := new(emptypb.Empty)
	err := c.cc.Invoke(ctx, SyncAgentService_FileSend_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *syncAgentServiceClient) FilesSync(ctx context.Context, in *FilesSyncRequest, opts ...grpc.CallOption) (*emptypb.Empty, error) {
	out := new(emptypb.Empty)
	err := c.cc.Invoke(ctx, SyncAgentService_FilesSync_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *syncAgentServiceClient) SnapshotClone(ctx context.Context, in *SnapshotCloneRequest, opts ...grpc.CallOption) (*emptypb.Empty, error) {
	out := new(emptypb.Empty)
	err := c.cc.Invoke(ctx, SyncAgentService_SnapshotClone_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *syncAgentServiceClient) VolumeExport(ctx context.Context, in *VolumeExportRequest, opts ...grpc.CallOption) (*emptypb.Empty, error) {
	out := new(emptypb.Empty)
	err := c.cc.Invoke(ctx, SyncAgentService_VolumeExport_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *syncAgentServiceClient) ReceiverLaunch(ctx context.Context, in *ReceiverLaunchRequest, opts ...grpc.CallOption) (*ReceiverLaunchResponse, error) {
	out := new(ReceiverLaunchResponse)
	err := c.cc.Invoke(ctx, SyncAgentService_ReceiverLaunch_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *syncAgentServiceClient) BackupCreate(ctx context.Context, in *BackupCreateRequest, opts ...grpc.CallOption) (*BackupCreateResponse, error) {
	out := new(BackupCreateResponse)
	err := c.cc.Invoke(ctx, SyncAgentService_BackupCreate_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *syncAgentServiceClient) BackupRemove(ctx context.Context, in *BackupRemoveRequest, opts ...grpc.CallOption) (*emptypb.Empty, error) {
	out := new(emptypb.Empty)
	err := c.cc.Invoke(ctx, SyncAgentService_BackupRemove_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *syncAgentServiceClient) BackupRestore(ctx context.Context, in *BackupRestoreRequest, opts ...grpc.CallOption) (*emptypb.Empty, error) {
	out := new(emptypb.Empty)
	err := c.cc.Invoke(ctx, SyncAgentService_BackupRestore_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *syncAgentServiceClient) BackupStatus(ctx context.Context, in *BackupStatusRequest, opts ...grpc.CallOption) (*BackupStatusResponse, error) {
	out := new(BackupStatusResponse)
	err := c.cc.Invoke(ctx, SyncAgentService_BackupStatus_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *syncAgentServiceClient) Reset(ctx context.Context, in *emptypb.Empty, opts ...grpc.CallOption) (*emptypb.Empty, error) {
	out := new(emptypb.Empty)
	err := c.cc.Invoke(ctx, SyncAgentService_Reset_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *syncAgentServiceClient) RestoreStatus(ctx context.Context, in *emptypb.Empty, opts ...grpc.CallOption) (*RestoreStatusResponse, error) {
	out := new(RestoreStatusResponse)
	err := c.cc.Invoke(ctx, SyncAgentService_RestoreStatus_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *syncAgentServiceClient) SnapshotPurge(ctx context.Context, in *emptypb.Empty, opts ...grpc.CallOption) (*emptypb.Empty, error) {
	out := new(emptypb.Empty)
	err := c.cc.Invoke(ctx, SyncAgentService_SnapshotPurge_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *syncAgentServiceClient) SnapshotPurgeStatus(ctx context.Context, in *emptypb.Empty, opts ...grpc.CallOption) (*SnapshotPurgeStatusResponse, error) {
	out := new(SnapshotPurgeStatusResponse)
	err := c.cc.Invoke(ctx, SyncAgentService_SnapshotPurgeStatus_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *syncAgentServiceClient) ReplicaRebuildStatus(ctx context.Context, in *emptypb.Empty, opts ...grpc.CallOption) (*ReplicaRebuildStatusResponse, error) {
	out := new(ReplicaRebuildStatusResponse)
	err := c.cc.Invoke(ctx, SyncAgentService_ReplicaRebuildStatus_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *syncAgentServiceClient) SnapshotCloneStatus(ctx context.Context, in *emptypb.Empty, opts ...grpc.CallOption) (*SnapshotCloneStatusResponse, error) {
	out := new(SnapshotCloneStatusResponse)
	err := c.cc.Invoke(ctx, SyncAgentService_SnapshotCloneStatus_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *syncAgentServiceClient) SnapshotHash(ctx context.Context, in *SnapshotHashRequest, opts ...grpc.CallOption) (*emptypb.Empty, error) {
	out := new(emptypb.Empty)
	err := c.cc.Invoke(ctx, SyncAgentService_SnapshotHash_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *syncAgentServiceClient) SnapshotHashStatus(ctx context.Context, in *SnapshotHashStatusRequest, opts ...grpc.CallOption) (*SnapshotHashStatusResponse, error) {
	out := new(SnapshotHashStatusResponse)
	err := c.cc.Invoke(ctx, SyncAgentService_SnapshotHashStatus_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *syncAgentServiceClient) SnapshotHashCancel(ctx context.Context, in *SnapshotHashCancelRequest, opts ...grpc.CallOption) (*emptypb.Empty, error) {
	out := new(emptypb.Empty)
	err := c.cc.Invoke(ctx, SyncAgentService_SnapshotHashCancel_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *syncAgentServiceClient) SnapshotHashLockState(ctx context.Context, in *emptypb.Empty, opts ...grpc.CallOption) (*SnapshotHashLockStateResponse, error) {
	out := new(SnapshotHashLockStateResponse)
	err := c.cc.Invoke(ctx, SyncAgentService_SnapshotHashLockState_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// SyncAgentServiceServer is the server API for SyncAgentService service.
// All implementations must embed UnimplementedSyncAgentServiceServer
// for forward compatibility
type SyncAgentServiceServer interface {
	FileRemove(context.Context, *FileRemoveRequest) (*emptypb.Empty, error)
	FileRename(context.Context, *FileRenameRequest) (*emptypb.Empty, error)
	FileSend(context.Context, *FileSendRequest) (*emptypb.Empty, error)
	FilesSync(context.Context, *FilesSyncRequest) (*emptypb.Empty, error)
	SnapshotClone(context.Context, *SnapshotCloneRequest) (*emptypb.Empty, error)
	VolumeExport(context.Context, *VolumeExportRequest) (*emptypb.Empty, error)
	ReceiverLaunch(context.Context, *ReceiverLaunchRequest) (*ReceiverLaunchResponse, error)
	BackupCreate(context.Context, *BackupCreateRequest) (*BackupCreateResponse, error)
	BackupRemove(context.Context, *BackupRemoveRequest) (*emptypb.Empty, error)
	BackupRestore(context.Context, *BackupRestoreRequest) (*emptypb.Empty, error)
	BackupStatus(context.Context, *BackupStatusRequest) (*BackupStatusResponse, error)
	Reset(context.Context, *emptypb.Empty) (*emptypb.Empty, error)
	RestoreStatus(context.Context, *emptypb.Empty) (*RestoreStatusResponse, error)
	SnapshotPurge(context.Context, *emptypb.Empty) (*emptypb.Empty, error)
	SnapshotPurgeStatus(context.Context, *emptypb.Empty) (*SnapshotPurgeStatusResponse, error)
	ReplicaRebuildStatus(context.Context, *emptypb.Empty) (*ReplicaRebuildStatusResponse, error)
	SnapshotCloneStatus(context.Context, *emptypb.Empty) (*SnapshotCloneStatusResponse, error)
	SnapshotHash(context.Context, *SnapshotHashRequest) (*emptypb.Empty, error)
	SnapshotHashStatus(context.Context, *SnapshotHashStatusRequest) (*SnapshotHashStatusResponse, error)
	SnapshotHashCancel(context.Context, *SnapshotHashCancelRequest) (*emptypb.Empty, error)
	SnapshotHashLockState(context.Context, *emptypb.Empty) (*SnapshotHashLockStateResponse, error)
	mustEmbedUnimplementedSyncAgentServiceServer()
}

// UnimplementedSyncAgentServiceServer must be embedded to have forward compatible implementations.
type UnimplementedSyncAgentServiceServer struct {
}

func (UnimplementedSyncAgentServiceServer) FileRemove(context.Context, *FileRemoveRequest) (*emptypb.Empty, error) {
	return nil, status.Errorf(codes.Unimplemented, "method FileRemove not implemented")
}
func (UnimplementedSyncAgentServiceServer) FileRename(context.Context, *FileRenameRequest) (*emptypb.Empty, error) {
	return nil, status.Errorf(codes.Unimplemented, "method FileRename not implemented")
}
func (UnimplementedSyncAgentServiceServer) FileSend(context.Context, *FileSendRequest) (*emptypb.Empty, error) {
	return nil, status.Errorf(codes.Unimplemented, "method FileSend not implemented")
}
func (UnimplementedSyncAgentServiceServer) FilesSync(context.Context, *FilesSyncRequest) (*emptypb.Empty, error) {
	return nil, status.Errorf(codes.Unimplemented, "method FilesSync not implemented")
}
func (UnimplementedSyncAgentServiceServer) SnapshotClone(context.Context, *SnapshotCloneRequest) (*emptypb.Empty, error) {
	return nil, status.Errorf(codes.Unimplemented, "method SnapshotClone not implemented")
}
func (UnimplementedSyncAgentServiceServer) VolumeExport(context.Context, *VolumeExportRequest) (*emptypb.Empty, error) {
	return nil, status.Errorf(codes.Unimplemented, "method VolumeExport not implemented")
}
func (UnimplementedSyncAgentServiceServer) ReceiverLaunch(context.Context, *ReceiverLaunchRequest) (*ReceiverLaunchResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method ReceiverLaunch not implemented")
}
func (UnimplementedSyncAgentServiceServer) BackupCreate(context.Context, *BackupCreateRequest) (*BackupCreateResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method BackupCreate not implemented")
}
func (UnimplementedSyncAgentServiceServer) BackupRemove(context.Context, *BackupRemoveRequest) (*emptypb.Empty, error) {
	return nil, status.Errorf(codes.Unimplemented, "method BackupRemove not implemented")
}
func (UnimplementedSyncAgentServiceServer) BackupRestore(context.Context, *BackupRestoreRequest) (*emptypb.Empty, error) {
	return nil, status.Errorf(codes.Unimplemented, "method BackupRestore not implemented")
}
func (UnimplementedSyncAgentServiceServer) BackupStatus(context.Context, *BackupStatusRequest) (*BackupStatusResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method BackupStatus not implemented")
}
func (UnimplementedSyncAgentServiceServer) Reset(context.Context, *emptypb.Empty) (*emptypb.Empty, error) {
	return nil, status.Errorf(codes.Unimplemented, "method Reset not implemented")
}
func (UnimplementedSyncAgentServiceServer) RestoreStatus(context.Context, *emptypb.Empty) (*RestoreStatusResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method RestoreStatus not implemented")
}
func (UnimplementedSyncAgentServiceServer) SnapshotPurge(context.Context, *emptypb.Empty) (*emptypb.Empty, error) {
	return nil, status.Errorf(codes.Unimplemented, "method SnapshotPurge not implemented")
}
func (UnimplementedSyncAgentServiceServer) SnapshotPurgeStatus(context.Context, *emptypb.Empty) (*SnapshotPurgeStatusResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method SnapshotPurgeStatus not implemented")
}
func (UnimplementedSyncAgentServiceServer) ReplicaRebuildStatus(context.Context, *emptypb.Empty) (*ReplicaRebuildStatusResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method ReplicaRebuildStatus not implemented")
}
func (UnimplementedSyncAgentServiceServer) SnapshotCloneStatus(context.Context, *emptypb.Empty) (*SnapshotCloneStatusResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method SnapshotCloneStatus not implemented")
}
func (UnimplementedSyncAgentServiceServer) SnapshotHash(context.Context, *SnapshotHashRequest) (*emptypb.Empty, error) {
	return nil, status.Errorf(codes.Unimplemented, "method SnapshotHash not implemented")
}
func (UnimplementedSyncAgentServiceServer) SnapshotHashStatus(context.Context, *SnapshotHashStatusRequest) (*SnapshotHashStatusResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method SnapshotHashStatus not implemented")
}
func (UnimplementedSyncAgentServiceServer) SnapshotHashCancel(context.Context, *SnapshotHashCancelRequest) (*emptypb.Empty, error) {
	return nil, status.Errorf(codes.Unimplemented, "method SnapshotHashCancel not implemented")
}
func (UnimplementedSyncAgentServiceServer) SnapshotHashLockState(context.Context, *emptypb.Empty) (*SnapshotHashLockStateResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method SnapshotHashLockState not implemented")
}
func (UnimplementedSyncAgentServiceServer) mustEmbedUnimplementedSyncAgentServiceServer() {}

// UnsafeSyncAgentServiceServer may be embedded to opt out of forward compatibility for this service.
// Use of this interface is not recommended, as added methods to SyncAgentServiceServer will
// result in compilation errors.
type UnsafeSyncAgentServiceServer interface {
	mustEmbedUnimplementedSyncAgentServiceServer()
}

func RegisterSyncAgentServiceServer(s grpc.ServiceRegistrar, srv SyncAgentServiceServer) {
	s.RegisterService(&SyncAgentService_ServiceDesc, srv)
}

func _SyncAgentService_FileRemove_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(FileRemoveRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(SyncAgentServiceServer).FileRemove(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: SyncAgentService_FileRemove_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(SyncAgentServiceServer).FileRemove(ctx, req.(*FileRemoveRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _SyncAgentService_FileRename_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(FileRenameRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(SyncAgentServiceServer).FileRename(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: SyncAgentService_FileRename_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(SyncAgentServiceServer).FileRename(ctx, req.(*FileRenameRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _SyncAgentService_FileSend_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(FileSendRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(SyncAgentServiceServer).FileSend(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: SyncAgentService_FileSend_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(SyncAgentServiceServer).FileSend(ctx, req.(*FileSendRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _SyncAgentService_FilesSync_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(FilesSyncRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(SyncAgentServiceServer).FilesSync(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: SyncAgentService_FilesSync_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(SyncAgentServiceServer).FilesSync(ctx, req.(*FilesSyncRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _SyncAgentService_SnapshotClone_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(SnapshotCloneRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(SyncAgentServiceServer).SnapshotClone(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: SyncAgentService_SnapshotClone_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(SyncAgentServiceServer).SnapshotClone(ctx, req.(*SnapshotCloneRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _SyncAgentService_VolumeExport_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(VolumeExportRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(SyncAgentServiceServer).VolumeExport(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: SyncAgentService_VolumeExport_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(SyncAgentServiceServer).VolumeExport(ctx, req.(*VolumeExportRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _SyncAgentService_ReceiverLaunch_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(ReceiverLaunchRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(SyncAgentServiceServer).ReceiverLaunch(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: SyncAgentService_ReceiverLaunch_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(SyncAgentServiceServer).ReceiverLaunch(ctx, req.(*ReceiverLaunchRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _SyncAgentService_BackupCreate_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(BackupCreateRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(SyncAgentServiceServer).BackupCreate(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: SyncAgentService_BackupCreate_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(SyncAgentServiceServer).BackupCreate(ctx, req.(*BackupCreateRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _SyncAgentService_BackupRemove_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(BackupRemoveRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(SyncAgentServiceServer).BackupRemove(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: SyncAgentService_BackupRemove_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(SyncAgentServiceServer).BackupRemove(ctx, req.(*BackupRemoveRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _SyncAgentService_BackupRestore_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(BackupRestoreRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(SyncAgentServiceServer).BackupRestore(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: SyncAgentService_BackupRestore_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(SyncAgentServiceServer).BackupRestore(ctx, req.(*BackupRestoreRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _SyncAgentService_BackupStatus_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(BackupStatusRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(SyncAgentServiceServer).BackupStatus(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: SyncAgentService_BackupStatus_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(SyncAgentServiceServer).BackupStatus(ctx, req.(*BackupStatusRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _SyncAgentService_Reset_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(emptypb.Empty)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(SyncAgentServiceServer).Reset(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: SyncAgentService_Reset_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(SyncAgentServiceServer).Reset(ctx, req.(*emptypb.Empty))
	}
	return interceptor(ctx, in, info, handler)
}

func _SyncAgentService_RestoreStatus_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(emptypb.Empty)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(SyncAgentServiceServer).RestoreStatus(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: SyncAgentService_RestoreStatus_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(SyncAgentServiceServer).RestoreStatus(ctx, req.(*emptypb.Empty))
	}
	return interceptor(ctx, in, info, handler)
}

func _SyncAgentService_SnapshotPurge_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(emptypb.Empty)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(SyncAgentServiceServer).SnapshotPurge(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: SyncAgentService_SnapshotPurge_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(SyncAgentServiceServer).SnapshotPurge(ctx, req.(*emptypb.Empty))
	}
	return interceptor(ctx, in, info, handler)
}

func _SyncAgentService_SnapshotPurgeStatus_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(emptypb.Empty)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(SyncAgentServiceServer).SnapshotPurgeStatus(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: SyncAgentService_SnapshotPurgeStatus_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(SyncAgentServiceServer).SnapshotPurgeStatus(ctx, req.(*emptypb.Empty))
	}
	return interceptor(ctx, in, info, handler)
}

func _SyncAgentService_ReplicaRebuildStatus_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(emptypb.Empty)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(SyncAgentServiceServer).ReplicaRebuildStatus(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: SyncAgentService_ReplicaRebuildStatus_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(SyncAgentServiceServer).ReplicaRebuildStatus(ctx, req.(*emptypb.Empty))
	}
	return interceptor(ctx, in, info, handler)
}

func _SyncAgentService_SnapshotCloneStatus_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(emptypb.Empty)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(SyncAgentServiceServer).SnapshotCloneStatus(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: SyncAgentService_SnapshotCloneStatus_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(SyncAgentServiceServer).SnapshotCloneStatus(ctx, req.(*emptypb.Empty))
	}
	return interceptor(ctx, in, info, handler)
}

func _SyncAgentService_SnapshotHash_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(SnapshotHashRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(SyncAgentServiceServer).SnapshotHash(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: SyncAgentService_SnapshotHash_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(SyncAgentServiceServer).SnapshotHash(ctx, req.(*SnapshotHashRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _SyncAgentService_SnapshotHashStatus_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(SnapshotHashStatusRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(SyncAgentServiceServer).SnapshotHashStatus(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: SyncAgentService_SnapshotHashStatus_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(SyncAgentServiceServer).SnapshotHashStatus(ctx, req.(*SnapshotHashStatusRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _SyncAgentService_SnapshotHashCancel_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(SnapshotHashCancelRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(SyncAgentServiceServer).SnapshotHashCancel(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: SyncAgentService_SnapshotHashCancel_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(SyncAgentServiceServer).SnapshotHashCancel(ctx, req.(*SnapshotHashCancelRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _SyncAgentService_SnapshotHashLockState_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(emptypb.Empty)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(SyncAgentServiceServer).SnapshotHashLockState(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: SyncAgentService_SnapshotHashLockState_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(SyncAgentServiceServer).SnapshotHashLockState(ctx, req.(*emptypb.Empty))
	}
	return interceptor(ctx, in, info, handler)
}

// SyncAgentService_ServiceDesc is the grpc.ServiceDesc for SyncAgentService service.
// It's only intended for direct use with grpc.RegisterService,
// and not to be introspected or modified (even as a copy)
var SyncAgentService_ServiceDesc = grpc.ServiceDesc{
	ServiceName: "pkg.enginerpc.SyncAgentService",
	HandlerType: (*SyncAgentServiceServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "FileRemove",
			Handler:    _SyncAgentService_FileRemove_Handler,
		},
		{
			MethodName: "FileRename",
			Handler:    _SyncAgentService_FileRename_Handler,
		},
		{
			MethodName: "FileSend",
			Handler:    _SyncAgentService_FileSend_Handler,
		},
		{
			MethodName: "FilesSync",
			Handler:    _SyncAgentService_FilesSync_Handler,
		},
		{
			MethodName: "SnapshotClone",
			Handler:    _SyncAgentService_SnapshotClone_Handler,
		},
		{
			MethodName: "VolumeExport",
			Handler:    _SyncAgentService_VolumeExport_Handler,
		},
		{
			MethodName: "ReceiverLaunch",
			Handler:    _SyncAgentService_ReceiverLaunch_Handler,
		},
		{
			MethodName: "BackupCreate",
			Handler:    _SyncAgentService_BackupCreate_Handler,
		},
		{
			MethodName: "BackupRemove",
			Handler:    _SyncAgentService_BackupRemove_Handler,
		},
		{
			MethodName: "BackupRestore",
			Handler:    _SyncAgentService_BackupRestore_Handler,
		},
		{
			MethodName: "BackupStatus",
			Handler:    _SyncAgentService_BackupStatus_Handler,
		},
		{
			MethodName: "Reset",
			Handler:    _SyncAgentService_Reset_Handler,
		},
		{
			MethodName: "RestoreStatus",
			Handler:    _SyncAgentService_RestoreStatus_Handler,
		},
		{
			MethodName: "SnapshotPurge",
			Handler:    _SyncAgentService_SnapshotPurge_Handler,
		},
		{
			MethodName: "SnapshotPurgeStatus",
			Handler:    _SyncAgentService_SnapshotPurgeStatus_Handler,
		},
		{
			MethodName: "ReplicaRebuildStatus",
			Handler:    _SyncAgentService_ReplicaRebuildStatus_Handler,
		},
		{
			MethodName: "SnapshotCloneStatus",
			Handler:    _SyncAgentService_SnapshotCloneStatus_Handler,
		},
		{
			MethodName: "SnapshotHash",
			Handler:    _SyncAgentService_SnapshotHash_Handler,
		},
		{
			MethodName: "SnapshotHashStatus",
			Handler:    _SyncAgentService_SnapshotHashStatus_Handler,
		},
		{
			MethodName: "SnapshotHashCancel",
			Handler:    _SyncAgentService_SnapshotHashCancel_Handler,
		},
		{
			MethodName: "SnapshotHashLockState",
			Handler:    _SyncAgentService_SnapshotHashLockState_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "pkg/enginerpc/syncagent.proto",
}
