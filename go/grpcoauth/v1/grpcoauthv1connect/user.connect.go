// Code generated by protoc-gen-connect-go. DO NOT EDIT.
//
// Source: grpcoauth/v1/user.proto

package grpcoauthv1connect

import (
	connect "connectrpc.com/connect"
	context "context"
	errors "errors"
	v1 "github.com/vet1ments/grpcoauth/go/grpcoauth/v1"
	http "net/http"
	strings "strings"
)

// This is a compile-time assertion to ensure that this generated file and the connect package are
// compatible. If you get a compiler error that this constant is not defined, this code was
// generated with a version of connect newer than the one compiled into your binary. You can fix the
// problem by either regenerating this code with an older version of connect or updating the connect
// version compiled into your binary.
const _ = connect.IsAtLeastVersion1_13_0

const (
	// UserServiceName is the fully-qualified name of the UserService service.
	UserServiceName = "grpcoauth.v1.UserService"
)

// These constants are the fully-qualified names of the RPCs defined in this package. They're
// exposed at runtime as Spec.Procedure and as the final two segments of the HTTP route.
//
// Note that these are different from the fully-qualified method names used by
// google.golang.org/protobuf/reflect/protoreflect. To convert from these constants to
// reflection-formatted method names, remove the leading slash and convert the remaining slash to a
// period.
const (
	// UserServiceGetUserProcedure is the fully-qualified name of the UserService's GetUser RPC.
	UserServiceGetUserProcedure = "/grpcoauth.v1.UserService/GetUser"
	// UserServiceCreateUserProcedure is the fully-qualified name of the UserService's CreateUser RPC.
	UserServiceCreateUserProcedure = "/grpcoauth.v1.UserService/CreateUser"
	// UserServiceGetUserByTokenProcedure is the fully-qualified name of the UserService's
	// GetUserByToken RPC.
	UserServiceGetUserByTokenProcedure = "/grpcoauth.v1.UserService/GetUserByToken"
	// UserServiceGetUserListByTokenProcedure is the fully-qualified name of the UserService's
	// GetUserListByToken RPC.
	UserServiceGetUserListByTokenProcedure = "/grpcoauth.v1.UserService/GetUserListByToken"
)

// These variables are the protoreflect.Descriptor objects for the RPCs defined in this package.
var (
	userServiceServiceDescriptor                  = v1.File_grpcoauth_v1_user_proto.Services().ByName("UserService")
	userServiceGetUserMethodDescriptor            = userServiceServiceDescriptor.Methods().ByName("GetUser")
	userServiceCreateUserMethodDescriptor         = userServiceServiceDescriptor.Methods().ByName("CreateUser")
	userServiceGetUserByTokenMethodDescriptor     = userServiceServiceDescriptor.Methods().ByName("GetUserByToken")
	userServiceGetUserListByTokenMethodDescriptor = userServiceServiceDescriptor.Methods().ByName("GetUserListByToken")
)

// UserServiceClient is a client for the grpcoauth.v1.UserService service.
type UserServiceClient interface {
	GetUser(context.Context, *connect.Request[v1.GetUserRequest]) (*connect.Response[v1.GetUserResponse], error)
	CreateUser(context.Context, *connect.Request[v1.CreateUserRequest]) (*connect.Response[v1.CreateUserResponse], error)
	GetUserByToken(context.Context, *connect.Request[v1.GetUserByTokenRequest]) (*connect.Response[v1.GetUserByTokenResponse], error)
	GetUserListByToken(context.Context, *connect.Request[v1.GetUserListByTokenRequest]) (*connect.Response[v1.GetUserListByTokenResponse], error)
}

// NewUserServiceClient constructs a client for the grpcoauth.v1.UserService service. By default, it
// uses the Connect protocol with the binary Protobuf Codec, asks for gzipped responses, and sends
// uncompressed requests. To use the gRPC or gRPC-Web protocols, supply the connect.WithGRPC() or
// connect.WithGRPCWeb() options.
//
// The URL supplied here should be the base URL for the Connect or gRPC server (for example,
// http://api.acme.com or https://acme.com/grpc).
func NewUserServiceClient(httpClient connect.HTTPClient, baseURL string, opts ...connect.ClientOption) UserServiceClient {
	baseURL = strings.TrimRight(baseURL, "/")
	return &userServiceClient{
		getUser: connect.NewClient[v1.GetUserRequest, v1.GetUserResponse](
			httpClient,
			baseURL+UserServiceGetUserProcedure,
			connect.WithSchema(userServiceGetUserMethodDescriptor),
			connect.WithClientOptions(opts...),
		),
		createUser: connect.NewClient[v1.CreateUserRequest, v1.CreateUserResponse](
			httpClient,
			baseURL+UserServiceCreateUserProcedure,
			connect.WithSchema(userServiceCreateUserMethodDescriptor),
			connect.WithClientOptions(opts...),
		),
		getUserByToken: connect.NewClient[v1.GetUserByTokenRequest, v1.GetUserByTokenResponse](
			httpClient,
			baseURL+UserServiceGetUserByTokenProcedure,
			connect.WithSchema(userServiceGetUserByTokenMethodDescriptor),
			connect.WithClientOptions(opts...),
		),
		getUserListByToken: connect.NewClient[v1.GetUserListByTokenRequest, v1.GetUserListByTokenResponse](
			httpClient,
			baseURL+UserServiceGetUserListByTokenProcedure,
			connect.WithSchema(userServiceGetUserListByTokenMethodDescriptor),
			connect.WithClientOptions(opts...),
		),
	}
}

// userServiceClient implements UserServiceClient.
type userServiceClient struct {
	getUser            *connect.Client[v1.GetUserRequest, v1.GetUserResponse]
	createUser         *connect.Client[v1.CreateUserRequest, v1.CreateUserResponse]
	getUserByToken     *connect.Client[v1.GetUserByTokenRequest, v1.GetUserByTokenResponse]
	getUserListByToken *connect.Client[v1.GetUserListByTokenRequest, v1.GetUserListByTokenResponse]
}

// GetUser calls grpcoauth.v1.UserService.GetUser.
func (c *userServiceClient) GetUser(ctx context.Context, req *connect.Request[v1.GetUserRequest]) (*connect.Response[v1.GetUserResponse], error) {
	return c.getUser.CallUnary(ctx, req)
}

// CreateUser calls grpcoauth.v1.UserService.CreateUser.
func (c *userServiceClient) CreateUser(ctx context.Context, req *connect.Request[v1.CreateUserRequest]) (*connect.Response[v1.CreateUserResponse], error) {
	return c.createUser.CallUnary(ctx, req)
}

// GetUserByToken calls grpcoauth.v1.UserService.GetUserByToken.
func (c *userServiceClient) GetUserByToken(ctx context.Context, req *connect.Request[v1.GetUserByTokenRequest]) (*connect.Response[v1.GetUserByTokenResponse], error) {
	return c.getUserByToken.CallUnary(ctx, req)
}

// GetUserListByToken calls grpcoauth.v1.UserService.GetUserListByToken.
func (c *userServiceClient) GetUserListByToken(ctx context.Context, req *connect.Request[v1.GetUserListByTokenRequest]) (*connect.Response[v1.GetUserListByTokenResponse], error) {
	return c.getUserListByToken.CallUnary(ctx, req)
}

// UserServiceHandler is an implementation of the grpcoauth.v1.UserService service.
type UserServiceHandler interface {
	GetUser(context.Context, *connect.Request[v1.GetUserRequest]) (*connect.Response[v1.GetUserResponse], error)
	CreateUser(context.Context, *connect.Request[v1.CreateUserRequest]) (*connect.Response[v1.CreateUserResponse], error)
	GetUserByToken(context.Context, *connect.Request[v1.GetUserByTokenRequest]) (*connect.Response[v1.GetUserByTokenResponse], error)
	GetUserListByToken(context.Context, *connect.Request[v1.GetUserListByTokenRequest]) (*connect.Response[v1.GetUserListByTokenResponse], error)
}

// NewUserServiceHandler builds an HTTP handler from the service implementation. It returns the path
// on which to mount the handler and the handler itself.
//
// By default, handlers support the Connect, gRPC, and gRPC-Web protocols with the binary Protobuf
// and JSON codecs. They also support gzip compression.
func NewUserServiceHandler(svc UserServiceHandler, opts ...connect.HandlerOption) (string, http.Handler) {
	userServiceGetUserHandler := connect.NewUnaryHandler(
		UserServiceGetUserProcedure,
		svc.GetUser,
		connect.WithSchema(userServiceGetUserMethodDescriptor),
		connect.WithHandlerOptions(opts...),
	)
	userServiceCreateUserHandler := connect.NewUnaryHandler(
		UserServiceCreateUserProcedure,
		svc.CreateUser,
		connect.WithSchema(userServiceCreateUserMethodDescriptor),
		connect.WithHandlerOptions(opts...),
	)
	userServiceGetUserByTokenHandler := connect.NewUnaryHandler(
		UserServiceGetUserByTokenProcedure,
		svc.GetUserByToken,
		connect.WithSchema(userServiceGetUserByTokenMethodDescriptor),
		connect.WithHandlerOptions(opts...),
	)
	userServiceGetUserListByTokenHandler := connect.NewUnaryHandler(
		UserServiceGetUserListByTokenProcedure,
		svc.GetUserListByToken,
		connect.WithSchema(userServiceGetUserListByTokenMethodDescriptor),
		connect.WithHandlerOptions(opts...),
	)
	return "/grpcoauth.v1.UserService/", http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		switch r.URL.Path {
		case UserServiceGetUserProcedure:
			userServiceGetUserHandler.ServeHTTP(w, r)
		case UserServiceCreateUserProcedure:
			userServiceCreateUserHandler.ServeHTTP(w, r)
		case UserServiceGetUserByTokenProcedure:
			userServiceGetUserByTokenHandler.ServeHTTP(w, r)
		case UserServiceGetUserListByTokenProcedure:
			userServiceGetUserListByTokenHandler.ServeHTTP(w, r)
		default:
			http.NotFound(w, r)
		}
	})
}

// UnimplementedUserServiceHandler returns CodeUnimplemented from all methods.
type UnimplementedUserServiceHandler struct{}

func (UnimplementedUserServiceHandler) GetUser(context.Context, *connect.Request[v1.GetUserRequest]) (*connect.Response[v1.GetUserResponse], error) {
	return nil, connect.NewError(connect.CodeUnimplemented, errors.New("grpcoauth.v1.UserService.GetUser is not implemented"))
}

func (UnimplementedUserServiceHandler) CreateUser(context.Context, *connect.Request[v1.CreateUserRequest]) (*connect.Response[v1.CreateUserResponse], error) {
	return nil, connect.NewError(connect.CodeUnimplemented, errors.New("grpcoauth.v1.UserService.CreateUser is not implemented"))
}

func (UnimplementedUserServiceHandler) GetUserByToken(context.Context, *connect.Request[v1.GetUserByTokenRequest]) (*connect.Response[v1.GetUserByTokenResponse], error) {
	return nil, connect.NewError(connect.CodeUnimplemented, errors.New("grpcoauth.v1.UserService.GetUserByToken is not implemented"))
}

func (UnimplementedUserServiceHandler) GetUserListByToken(context.Context, *connect.Request[v1.GetUserListByTokenRequest]) (*connect.Response[v1.GetUserListByTokenResponse], error) {
	return nil, connect.NewError(connect.CodeUnimplemented, errors.New("grpcoauth.v1.UserService.GetUserListByToken is not implemented"))
}
