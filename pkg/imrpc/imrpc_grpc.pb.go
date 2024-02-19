// Code generated by protoc-gen-go-grpc. DO NOT EDIT.
// versions:
// - protoc-gen-go-grpc v1.3.0
// - protoc             v4.24.3
// source: pkg/imrpc/imrpc.proto

package imrpc

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
	ProcessManagerService_ProcessCreate_FullMethodName  = "/pkg.imrpc.ProcessManagerService/ProcessCreate"
	ProcessManagerService_ProcessDelete_FullMethodName  = "/pkg.imrpc.ProcessManagerService/ProcessDelete"
	ProcessManagerService_ProcessGet_FullMethodName     = "/pkg.imrpc.ProcessManagerService/ProcessGet"
	ProcessManagerService_ProcessList_FullMethodName    = "/pkg.imrpc.ProcessManagerService/ProcessList"
	ProcessManagerService_ProcessLog_FullMethodName     = "/pkg.imrpc.ProcessManagerService/ProcessLog"
	ProcessManagerService_ProcessWatch_FullMethodName   = "/pkg.imrpc.ProcessManagerService/ProcessWatch"
	ProcessManagerService_ProcessReplace_FullMethodName = "/pkg.imrpc.ProcessManagerService/ProcessReplace"
	ProcessManagerService_VersionGet_FullMethodName     = "/pkg.imrpc.ProcessManagerService/VersionGet"
)

// ProcessManagerServiceClient is the client API for ProcessManagerService service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream.
type ProcessManagerServiceClient interface {
	ProcessCreate(ctx context.Context, in *ProcessCreateRequest, opts ...grpc.CallOption) (*ProcessResponse, error)
	ProcessDelete(ctx context.Context, in *ProcessDeleteRequest, opts ...grpc.CallOption) (*ProcessResponse, error)
	ProcessGet(ctx context.Context, in *ProcessGetRequest, opts ...grpc.CallOption) (*ProcessResponse, error)
	ProcessList(ctx context.Context, in *ProcessListRequest, opts ...grpc.CallOption) (*ProcessListResponse, error)
	ProcessLog(ctx context.Context, in *LogRequest, opts ...grpc.CallOption) (ProcessManagerService_ProcessLogClient, error)
	ProcessWatch(ctx context.Context, in *emptypb.Empty, opts ...grpc.CallOption) (ProcessManagerService_ProcessWatchClient, error)
	ProcessReplace(ctx context.Context, in *ProcessReplaceRequest, opts ...grpc.CallOption) (*ProcessResponse, error)
	VersionGet(ctx context.Context, in *emptypb.Empty, opts ...grpc.CallOption) (*VersionResponse, error)
}

type processManagerServiceClient struct {
	cc grpc.ClientConnInterface
}

func NewProcessManagerServiceClient(cc grpc.ClientConnInterface) ProcessManagerServiceClient {
	return &processManagerServiceClient{cc}
}

func (c *processManagerServiceClient) ProcessCreate(ctx context.Context, in *ProcessCreateRequest, opts ...grpc.CallOption) (*ProcessResponse, error) {
	out := new(ProcessResponse)
	err := c.cc.Invoke(ctx, ProcessManagerService_ProcessCreate_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *processManagerServiceClient) ProcessDelete(ctx context.Context, in *ProcessDeleteRequest, opts ...grpc.CallOption) (*ProcessResponse, error) {
	out := new(ProcessResponse)
	err := c.cc.Invoke(ctx, ProcessManagerService_ProcessDelete_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *processManagerServiceClient) ProcessGet(ctx context.Context, in *ProcessGetRequest, opts ...grpc.CallOption) (*ProcessResponse, error) {
	out := new(ProcessResponse)
	err := c.cc.Invoke(ctx, ProcessManagerService_ProcessGet_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *processManagerServiceClient) ProcessList(ctx context.Context, in *ProcessListRequest, opts ...grpc.CallOption) (*ProcessListResponse, error) {
	out := new(ProcessListResponse)
	err := c.cc.Invoke(ctx, ProcessManagerService_ProcessList_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *processManagerServiceClient) ProcessLog(ctx context.Context, in *LogRequest, opts ...grpc.CallOption) (ProcessManagerService_ProcessLogClient, error) {
	stream, err := c.cc.NewStream(ctx, &ProcessManagerService_ServiceDesc.Streams[0], ProcessManagerService_ProcessLog_FullMethodName, opts...)
	if err != nil {
		return nil, err
	}
	x := &processManagerServiceProcessLogClient{stream}
	if err := x.ClientStream.SendMsg(in); err != nil {
		return nil, err
	}
	if err := x.ClientStream.CloseSend(); err != nil {
		return nil, err
	}
	return x, nil
}

type ProcessManagerService_ProcessLogClient interface {
	Recv() (*LogResponse, error)
	grpc.ClientStream
}

type processManagerServiceProcessLogClient struct {
	grpc.ClientStream
}

func (x *processManagerServiceProcessLogClient) Recv() (*LogResponse, error) {
	m := new(LogResponse)
	if err := x.ClientStream.RecvMsg(m); err != nil {
		return nil, err
	}
	return m, nil
}

func (c *processManagerServiceClient) ProcessWatch(ctx context.Context, in *emptypb.Empty, opts ...grpc.CallOption) (ProcessManagerService_ProcessWatchClient, error) {
	stream, err := c.cc.NewStream(ctx, &ProcessManagerService_ServiceDesc.Streams[1], ProcessManagerService_ProcessWatch_FullMethodName, opts...)
	if err != nil {
		return nil, err
	}
	x := &processManagerServiceProcessWatchClient{stream}
	if err := x.ClientStream.SendMsg(in); err != nil {
		return nil, err
	}
	if err := x.ClientStream.CloseSend(); err != nil {
		return nil, err
	}
	return x, nil
}

type ProcessManagerService_ProcessWatchClient interface {
	Recv() (*ProcessResponse, error)
	grpc.ClientStream
}

type processManagerServiceProcessWatchClient struct {
	grpc.ClientStream
}

func (x *processManagerServiceProcessWatchClient) Recv() (*ProcessResponse, error) {
	m := new(ProcessResponse)
	if err := x.ClientStream.RecvMsg(m); err != nil {
		return nil, err
	}
	return m, nil
}

func (c *processManagerServiceClient) ProcessReplace(ctx context.Context, in *ProcessReplaceRequest, opts ...grpc.CallOption) (*ProcessResponse, error) {
	out := new(ProcessResponse)
	err := c.cc.Invoke(ctx, ProcessManagerService_ProcessReplace_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *processManagerServiceClient) VersionGet(ctx context.Context, in *emptypb.Empty, opts ...grpc.CallOption) (*VersionResponse, error) {
	out := new(VersionResponse)
	err := c.cc.Invoke(ctx, ProcessManagerService_VersionGet_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// ProcessManagerServiceServer is the server API for ProcessManagerService service.
// All implementations must embed UnimplementedProcessManagerServiceServer
// for forward compatibility
type ProcessManagerServiceServer interface {
	ProcessCreate(context.Context, *ProcessCreateRequest) (*ProcessResponse, error)
	ProcessDelete(context.Context, *ProcessDeleteRequest) (*ProcessResponse, error)
	ProcessGet(context.Context, *ProcessGetRequest) (*ProcessResponse, error)
	ProcessList(context.Context, *ProcessListRequest) (*ProcessListResponse, error)
	ProcessLog(*LogRequest, ProcessManagerService_ProcessLogServer) error
	ProcessWatch(*emptypb.Empty, ProcessManagerService_ProcessWatchServer) error
	ProcessReplace(context.Context, *ProcessReplaceRequest) (*ProcessResponse, error)
	VersionGet(context.Context, *emptypb.Empty) (*VersionResponse, error)
	mustEmbedUnimplementedProcessManagerServiceServer()
}

// UnimplementedProcessManagerServiceServer must be embedded to have forward compatible implementations.
type UnimplementedProcessManagerServiceServer struct {
}

func (UnimplementedProcessManagerServiceServer) ProcessCreate(context.Context, *ProcessCreateRequest) (*ProcessResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method ProcessCreate not implemented")
}
func (UnimplementedProcessManagerServiceServer) ProcessDelete(context.Context, *ProcessDeleteRequest) (*ProcessResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method ProcessDelete not implemented")
}
func (UnimplementedProcessManagerServiceServer) ProcessGet(context.Context, *ProcessGetRequest) (*ProcessResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method ProcessGet not implemented")
}
func (UnimplementedProcessManagerServiceServer) ProcessList(context.Context, *ProcessListRequest) (*ProcessListResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method ProcessList not implemented")
}
func (UnimplementedProcessManagerServiceServer) ProcessLog(*LogRequest, ProcessManagerService_ProcessLogServer) error {
	return status.Errorf(codes.Unimplemented, "method ProcessLog not implemented")
}
func (UnimplementedProcessManagerServiceServer) ProcessWatch(*emptypb.Empty, ProcessManagerService_ProcessWatchServer) error {
	return status.Errorf(codes.Unimplemented, "method ProcessWatch not implemented")
}
func (UnimplementedProcessManagerServiceServer) ProcessReplace(context.Context, *ProcessReplaceRequest) (*ProcessResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method ProcessReplace not implemented")
}
func (UnimplementedProcessManagerServiceServer) VersionGet(context.Context, *emptypb.Empty) (*VersionResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method VersionGet not implemented")
}
func (UnimplementedProcessManagerServiceServer) mustEmbedUnimplementedProcessManagerServiceServer() {}

// UnsafeProcessManagerServiceServer may be embedded to opt out of forward compatibility for this service.
// Use of this interface is not recommended, as added methods to ProcessManagerServiceServer will
// result in compilation errors.
type UnsafeProcessManagerServiceServer interface {
	mustEmbedUnimplementedProcessManagerServiceServer()
}

func RegisterProcessManagerServiceServer(s grpc.ServiceRegistrar, srv ProcessManagerServiceServer) {
	s.RegisterService(&ProcessManagerService_ServiceDesc, srv)
}

func _ProcessManagerService_ProcessCreate_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(ProcessCreateRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(ProcessManagerServiceServer).ProcessCreate(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: ProcessManagerService_ProcessCreate_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(ProcessManagerServiceServer).ProcessCreate(ctx, req.(*ProcessCreateRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _ProcessManagerService_ProcessDelete_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(ProcessDeleteRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(ProcessManagerServiceServer).ProcessDelete(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: ProcessManagerService_ProcessDelete_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(ProcessManagerServiceServer).ProcessDelete(ctx, req.(*ProcessDeleteRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _ProcessManagerService_ProcessGet_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(ProcessGetRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(ProcessManagerServiceServer).ProcessGet(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: ProcessManagerService_ProcessGet_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(ProcessManagerServiceServer).ProcessGet(ctx, req.(*ProcessGetRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _ProcessManagerService_ProcessList_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(ProcessListRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(ProcessManagerServiceServer).ProcessList(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: ProcessManagerService_ProcessList_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(ProcessManagerServiceServer).ProcessList(ctx, req.(*ProcessListRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _ProcessManagerService_ProcessLog_Handler(srv interface{}, stream grpc.ServerStream) error {
	m := new(LogRequest)
	if err := stream.RecvMsg(m); err != nil {
		return err
	}
	return srv.(ProcessManagerServiceServer).ProcessLog(m, &processManagerServiceProcessLogServer{stream})
}

type ProcessManagerService_ProcessLogServer interface {
	Send(*LogResponse) error
	grpc.ServerStream
}

type processManagerServiceProcessLogServer struct {
	grpc.ServerStream
}

func (x *processManagerServiceProcessLogServer) Send(m *LogResponse) error {
	return x.ServerStream.SendMsg(m)
}

func _ProcessManagerService_ProcessWatch_Handler(srv interface{}, stream grpc.ServerStream) error {
	m := new(emptypb.Empty)
	if err := stream.RecvMsg(m); err != nil {
		return err
	}
	return srv.(ProcessManagerServiceServer).ProcessWatch(m, &processManagerServiceProcessWatchServer{stream})
}

type ProcessManagerService_ProcessWatchServer interface {
	Send(*ProcessResponse) error
	grpc.ServerStream
}

type processManagerServiceProcessWatchServer struct {
	grpc.ServerStream
}

func (x *processManagerServiceProcessWatchServer) Send(m *ProcessResponse) error {
	return x.ServerStream.SendMsg(m)
}

func _ProcessManagerService_ProcessReplace_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(ProcessReplaceRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(ProcessManagerServiceServer).ProcessReplace(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: ProcessManagerService_ProcessReplace_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(ProcessManagerServiceServer).ProcessReplace(ctx, req.(*ProcessReplaceRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _ProcessManagerService_VersionGet_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(emptypb.Empty)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(ProcessManagerServiceServer).VersionGet(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: ProcessManagerService_VersionGet_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(ProcessManagerServiceServer).VersionGet(ctx, req.(*emptypb.Empty))
	}
	return interceptor(ctx, in, info, handler)
}

// ProcessManagerService_ServiceDesc is the grpc.ServiceDesc for ProcessManagerService service.
// It's only intended for direct use with grpc.RegisterService,
// and not to be introspected or modified (even as a copy)
var ProcessManagerService_ServiceDesc = grpc.ServiceDesc{
	ServiceName: "pkg.imrpc.ProcessManagerService",
	HandlerType: (*ProcessManagerServiceServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "ProcessCreate",
			Handler:    _ProcessManagerService_ProcessCreate_Handler,
		},
		{
			MethodName: "ProcessDelete",
			Handler:    _ProcessManagerService_ProcessDelete_Handler,
		},
		{
			MethodName: "ProcessGet",
			Handler:    _ProcessManagerService_ProcessGet_Handler,
		},
		{
			MethodName: "ProcessList",
			Handler:    _ProcessManagerService_ProcessList_Handler,
		},
		{
			MethodName: "ProcessReplace",
			Handler:    _ProcessManagerService_ProcessReplace_Handler,
		},
		{
			MethodName: "VersionGet",
			Handler:    _ProcessManagerService_VersionGet_Handler,
		},
	},
	Streams: []grpc.StreamDesc{
		{
			StreamName:    "ProcessLog",
			Handler:       _ProcessManagerService_ProcessLog_Handler,
			ServerStreams: true,
		},
		{
			StreamName:    "ProcessWatch",
			Handler:       _ProcessManagerService_ProcessWatch_Handler,
			ServerStreams: true,
		},
	},
	Metadata: "pkg/imrpc/imrpc.proto",
}
