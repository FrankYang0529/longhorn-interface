// Code generated by protoc-gen-go-grpc. DO NOT EDIT.
// versions:
// - protoc-gen-go-grpc v1.3.0
// - protoc             v4.24.3
// source: pkg/imrpc/instance.proto

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
	InstanceService_InstanceCreate_FullMethodName  = "/pkg.imrpc.InstanceService/InstanceCreate"
	InstanceService_InstanceDelete_FullMethodName  = "/pkg.imrpc.InstanceService/InstanceDelete"
	InstanceService_InstanceGet_FullMethodName     = "/pkg.imrpc.InstanceService/InstanceGet"
	InstanceService_InstanceList_FullMethodName    = "/pkg.imrpc.InstanceService/InstanceList"
	InstanceService_InstanceLog_FullMethodName     = "/pkg.imrpc.InstanceService/InstanceLog"
	InstanceService_InstanceWatch_FullMethodName   = "/pkg.imrpc.InstanceService/InstanceWatch"
	InstanceService_InstanceReplace_FullMethodName = "/pkg.imrpc.InstanceService/InstanceReplace"
	InstanceService_VersionGet_FullMethodName      = "/pkg.imrpc.InstanceService/VersionGet"
)

// InstanceServiceClient is the client API for InstanceService service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream.
type InstanceServiceClient interface {
	InstanceCreate(ctx context.Context, in *InstanceCreateRequest, opts ...grpc.CallOption) (*InstanceResponse, error)
	InstanceDelete(ctx context.Context, in *InstanceDeleteRequest, opts ...grpc.CallOption) (*InstanceResponse, error)
	InstanceGet(ctx context.Context, in *InstanceGetRequest, opts ...grpc.CallOption) (*InstanceResponse, error)
	InstanceList(ctx context.Context, in *emptypb.Empty, opts ...grpc.CallOption) (*InstanceListResponse, error)
	InstanceLog(ctx context.Context, in *InstanceLogRequest, opts ...grpc.CallOption) (InstanceService_InstanceLogClient, error)
	InstanceWatch(ctx context.Context, in *emptypb.Empty, opts ...grpc.CallOption) (InstanceService_InstanceWatchClient, error)
	InstanceReplace(ctx context.Context, in *InstanceReplaceRequest, opts ...grpc.CallOption) (*InstanceResponse, error)
	VersionGet(ctx context.Context, in *emptypb.Empty, opts ...grpc.CallOption) (*VersionResponse, error)
}

type instanceServiceClient struct {
	cc grpc.ClientConnInterface
}

func NewInstanceServiceClient(cc grpc.ClientConnInterface) InstanceServiceClient {
	return &instanceServiceClient{cc}
}

func (c *instanceServiceClient) InstanceCreate(ctx context.Context, in *InstanceCreateRequest, opts ...grpc.CallOption) (*InstanceResponse, error) {
	out := new(InstanceResponse)
	err := c.cc.Invoke(ctx, InstanceService_InstanceCreate_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *instanceServiceClient) InstanceDelete(ctx context.Context, in *InstanceDeleteRequest, opts ...grpc.CallOption) (*InstanceResponse, error) {
	out := new(InstanceResponse)
	err := c.cc.Invoke(ctx, InstanceService_InstanceDelete_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *instanceServiceClient) InstanceGet(ctx context.Context, in *InstanceGetRequest, opts ...grpc.CallOption) (*InstanceResponse, error) {
	out := new(InstanceResponse)
	err := c.cc.Invoke(ctx, InstanceService_InstanceGet_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *instanceServiceClient) InstanceList(ctx context.Context, in *emptypb.Empty, opts ...grpc.CallOption) (*InstanceListResponse, error) {
	out := new(InstanceListResponse)
	err := c.cc.Invoke(ctx, InstanceService_InstanceList_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *instanceServiceClient) InstanceLog(ctx context.Context, in *InstanceLogRequest, opts ...grpc.CallOption) (InstanceService_InstanceLogClient, error) {
	stream, err := c.cc.NewStream(ctx, &InstanceService_ServiceDesc.Streams[0], InstanceService_InstanceLog_FullMethodName, opts...)
	if err != nil {
		return nil, err
	}
	x := &instanceServiceInstanceLogClient{stream}
	if err := x.ClientStream.SendMsg(in); err != nil {
		return nil, err
	}
	if err := x.ClientStream.CloseSend(); err != nil {
		return nil, err
	}
	return x, nil
}

type InstanceService_InstanceLogClient interface {
	Recv() (*LogResponse, error)
	grpc.ClientStream
}

type instanceServiceInstanceLogClient struct {
	grpc.ClientStream
}

func (x *instanceServiceInstanceLogClient) Recv() (*LogResponse, error) {
	m := new(LogResponse)
	if err := x.ClientStream.RecvMsg(m); err != nil {
		return nil, err
	}
	return m, nil
}

func (c *instanceServiceClient) InstanceWatch(ctx context.Context, in *emptypb.Empty, opts ...grpc.CallOption) (InstanceService_InstanceWatchClient, error) {
	stream, err := c.cc.NewStream(ctx, &InstanceService_ServiceDesc.Streams[1], InstanceService_InstanceWatch_FullMethodName, opts...)
	if err != nil {
		return nil, err
	}
	x := &instanceServiceInstanceWatchClient{stream}
	if err := x.ClientStream.SendMsg(in); err != nil {
		return nil, err
	}
	if err := x.ClientStream.CloseSend(); err != nil {
		return nil, err
	}
	return x, nil
}

type InstanceService_InstanceWatchClient interface {
	Recv() (*emptypb.Empty, error)
	grpc.ClientStream
}

type instanceServiceInstanceWatchClient struct {
	grpc.ClientStream
}

func (x *instanceServiceInstanceWatchClient) Recv() (*emptypb.Empty, error) {
	m := new(emptypb.Empty)
	if err := x.ClientStream.RecvMsg(m); err != nil {
		return nil, err
	}
	return m, nil
}

func (c *instanceServiceClient) InstanceReplace(ctx context.Context, in *InstanceReplaceRequest, opts ...grpc.CallOption) (*InstanceResponse, error) {
	out := new(InstanceResponse)
	err := c.cc.Invoke(ctx, InstanceService_InstanceReplace_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *instanceServiceClient) VersionGet(ctx context.Context, in *emptypb.Empty, opts ...grpc.CallOption) (*VersionResponse, error) {
	out := new(VersionResponse)
	err := c.cc.Invoke(ctx, InstanceService_VersionGet_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// InstanceServiceServer is the server API for InstanceService service.
// All implementations must embed UnimplementedInstanceServiceServer
// for forward compatibility
type InstanceServiceServer interface {
	InstanceCreate(context.Context, *InstanceCreateRequest) (*InstanceResponse, error)
	InstanceDelete(context.Context, *InstanceDeleteRequest) (*InstanceResponse, error)
	InstanceGet(context.Context, *InstanceGetRequest) (*InstanceResponse, error)
	InstanceList(context.Context, *emptypb.Empty) (*InstanceListResponse, error)
	InstanceLog(*InstanceLogRequest, InstanceService_InstanceLogServer) error
	InstanceWatch(*emptypb.Empty, InstanceService_InstanceWatchServer) error
	InstanceReplace(context.Context, *InstanceReplaceRequest) (*InstanceResponse, error)
	VersionGet(context.Context, *emptypb.Empty) (*VersionResponse, error)
	mustEmbedUnimplementedInstanceServiceServer()
}

// UnimplementedInstanceServiceServer must be embedded to have forward compatible implementations.
type UnimplementedInstanceServiceServer struct {
}

func (UnimplementedInstanceServiceServer) InstanceCreate(context.Context, *InstanceCreateRequest) (*InstanceResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method InstanceCreate not implemented")
}
func (UnimplementedInstanceServiceServer) InstanceDelete(context.Context, *InstanceDeleteRequest) (*InstanceResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method InstanceDelete not implemented")
}
func (UnimplementedInstanceServiceServer) InstanceGet(context.Context, *InstanceGetRequest) (*InstanceResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method InstanceGet not implemented")
}
func (UnimplementedInstanceServiceServer) InstanceList(context.Context, *emptypb.Empty) (*InstanceListResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method InstanceList not implemented")
}
func (UnimplementedInstanceServiceServer) InstanceLog(*InstanceLogRequest, InstanceService_InstanceLogServer) error {
	return status.Errorf(codes.Unimplemented, "method InstanceLog not implemented")
}
func (UnimplementedInstanceServiceServer) InstanceWatch(*emptypb.Empty, InstanceService_InstanceWatchServer) error {
	return status.Errorf(codes.Unimplemented, "method InstanceWatch not implemented")
}
func (UnimplementedInstanceServiceServer) InstanceReplace(context.Context, *InstanceReplaceRequest) (*InstanceResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method InstanceReplace not implemented")
}
func (UnimplementedInstanceServiceServer) VersionGet(context.Context, *emptypb.Empty) (*VersionResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method VersionGet not implemented")
}
func (UnimplementedInstanceServiceServer) mustEmbedUnimplementedInstanceServiceServer() {}

// UnsafeInstanceServiceServer may be embedded to opt out of forward compatibility for this service.
// Use of this interface is not recommended, as added methods to InstanceServiceServer will
// result in compilation errors.
type UnsafeInstanceServiceServer interface {
	mustEmbedUnimplementedInstanceServiceServer()
}

func RegisterInstanceServiceServer(s grpc.ServiceRegistrar, srv InstanceServiceServer) {
	s.RegisterService(&InstanceService_ServiceDesc, srv)
}

func _InstanceService_InstanceCreate_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(InstanceCreateRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(InstanceServiceServer).InstanceCreate(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: InstanceService_InstanceCreate_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(InstanceServiceServer).InstanceCreate(ctx, req.(*InstanceCreateRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _InstanceService_InstanceDelete_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(InstanceDeleteRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(InstanceServiceServer).InstanceDelete(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: InstanceService_InstanceDelete_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(InstanceServiceServer).InstanceDelete(ctx, req.(*InstanceDeleteRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _InstanceService_InstanceGet_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(InstanceGetRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(InstanceServiceServer).InstanceGet(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: InstanceService_InstanceGet_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(InstanceServiceServer).InstanceGet(ctx, req.(*InstanceGetRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _InstanceService_InstanceList_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(emptypb.Empty)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(InstanceServiceServer).InstanceList(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: InstanceService_InstanceList_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(InstanceServiceServer).InstanceList(ctx, req.(*emptypb.Empty))
	}
	return interceptor(ctx, in, info, handler)
}

func _InstanceService_InstanceLog_Handler(srv interface{}, stream grpc.ServerStream) error {
	m := new(InstanceLogRequest)
	if err := stream.RecvMsg(m); err != nil {
		return err
	}
	return srv.(InstanceServiceServer).InstanceLog(m, &instanceServiceInstanceLogServer{stream})
}

type InstanceService_InstanceLogServer interface {
	Send(*LogResponse) error
	grpc.ServerStream
}

type instanceServiceInstanceLogServer struct {
	grpc.ServerStream
}

func (x *instanceServiceInstanceLogServer) Send(m *LogResponse) error {
	return x.ServerStream.SendMsg(m)
}

func _InstanceService_InstanceWatch_Handler(srv interface{}, stream grpc.ServerStream) error {
	m := new(emptypb.Empty)
	if err := stream.RecvMsg(m); err != nil {
		return err
	}
	return srv.(InstanceServiceServer).InstanceWatch(m, &instanceServiceInstanceWatchServer{stream})
}

type InstanceService_InstanceWatchServer interface {
	Send(*emptypb.Empty) error
	grpc.ServerStream
}

type instanceServiceInstanceWatchServer struct {
	grpc.ServerStream
}

func (x *instanceServiceInstanceWatchServer) Send(m *emptypb.Empty) error {
	return x.ServerStream.SendMsg(m)
}

func _InstanceService_InstanceReplace_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(InstanceReplaceRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(InstanceServiceServer).InstanceReplace(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: InstanceService_InstanceReplace_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(InstanceServiceServer).InstanceReplace(ctx, req.(*InstanceReplaceRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _InstanceService_VersionGet_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(emptypb.Empty)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(InstanceServiceServer).VersionGet(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: InstanceService_VersionGet_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(InstanceServiceServer).VersionGet(ctx, req.(*emptypb.Empty))
	}
	return interceptor(ctx, in, info, handler)
}

// InstanceService_ServiceDesc is the grpc.ServiceDesc for InstanceService service.
// It's only intended for direct use with grpc.RegisterService,
// and not to be introspected or modified (even as a copy)
var InstanceService_ServiceDesc = grpc.ServiceDesc{
	ServiceName: "pkg.imrpc.InstanceService",
	HandlerType: (*InstanceServiceServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "InstanceCreate",
			Handler:    _InstanceService_InstanceCreate_Handler,
		},
		{
			MethodName: "InstanceDelete",
			Handler:    _InstanceService_InstanceDelete_Handler,
		},
		{
			MethodName: "InstanceGet",
			Handler:    _InstanceService_InstanceGet_Handler,
		},
		{
			MethodName: "InstanceList",
			Handler:    _InstanceService_InstanceList_Handler,
		},
		{
			MethodName: "InstanceReplace",
			Handler:    _InstanceService_InstanceReplace_Handler,
		},
		{
			MethodName: "VersionGet",
			Handler:    _InstanceService_VersionGet_Handler,
		},
	},
	Streams: []grpc.StreamDesc{
		{
			StreamName:    "InstanceLog",
			Handler:       _InstanceService_InstanceLog_Handler,
			ServerStreams: true,
		},
		{
			StreamName:    "InstanceWatch",
			Handler:       _InstanceService_InstanceWatch_Handler,
			ServerStreams: true,
		},
	},
	Metadata: "pkg/imrpc/instance.proto",
}
