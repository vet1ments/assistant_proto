// Code generated by protoc-gen-grpc-gateway. DO NOT EDIT.
// source: grpcoauth/v1/oauth.proto

/*
Package grpcoauthv1 is a reverse proxy.

It translates gRPC into RESTful JSON APIs.
*/
package grpcoauthv1

import (
	"context"
	"io"
	"net/http"

	"github.com/grpc-ecosystem/grpc-gateway/v2/runtime"
	"github.com/grpc-ecosystem/grpc-gateway/v2/utilities"
	"google.golang.org/grpc"
	"google.golang.org/grpc/codes"
	"google.golang.org/grpc/grpclog"
	"google.golang.org/grpc/metadata"
	"google.golang.org/grpc/status"
	"google.golang.org/protobuf/proto"
)

// Suppress "imported and not used" errors
var _ codes.Code
var _ io.Reader
var _ status.Status
var _ = runtime.String
var _ = utilities.NewDoubleArray
var _ = metadata.Join

var (
	filter_Oauth2Service_GetAuthorizeCode_0 = &utilities.DoubleArray{Encoding: map[string]int{}, Base: []int(nil), Check: []int(nil)}
)

func request_Oauth2Service_GetAuthorizeCode_0(ctx context.Context, marshaler runtime.Marshaler, client Oauth2ServiceClient, req *http.Request, pathParams map[string]string) (proto.Message, runtime.ServerMetadata, error) {
	var protoReq GetAuthorizeCodeRequest
	var metadata runtime.ServerMetadata

	if err := req.ParseForm(); err != nil {
		return nil, metadata, status.Errorf(codes.InvalidArgument, "%v", err)
	}
	if err := runtime.PopulateQueryParameters(&protoReq, req.Form, filter_Oauth2Service_GetAuthorizeCode_0); err != nil {
		return nil, metadata, status.Errorf(codes.InvalidArgument, "%v", err)
	}

	msg, err := client.GetAuthorizeCode(ctx, &protoReq, grpc.Header(&metadata.HeaderMD), grpc.Trailer(&metadata.TrailerMD))
	return msg, metadata, err

}

func local_request_Oauth2Service_GetAuthorizeCode_0(ctx context.Context, marshaler runtime.Marshaler, server Oauth2ServiceServer, req *http.Request, pathParams map[string]string) (proto.Message, runtime.ServerMetadata, error) {
	var protoReq GetAuthorizeCodeRequest
	var metadata runtime.ServerMetadata

	if err := req.ParseForm(); err != nil {
		return nil, metadata, status.Errorf(codes.InvalidArgument, "%v", err)
	}
	if err := runtime.PopulateQueryParameters(&protoReq, req.Form, filter_Oauth2Service_GetAuthorizeCode_0); err != nil {
		return nil, metadata, status.Errorf(codes.InvalidArgument, "%v", err)
	}

	msg, err := server.GetAuthorizeCode(ctx, &protoReq)
	return msg, metadata, err

}

var (
	filter_OauthCallbackService_Callback_0 = &utilities.DoubleArray{Encoding: map[string]int{}, Base: []int(nil), Check: []int(nil)}
)

func request_OauthCallbackService_Callback_0(ctx context.Context, marshaler runtime.Marshaler, client OauthCallbackServiceClient, req *http.Request, pathParams map[string]string) (proto.Message, runtime.ServerMetadata, error) {
	var protoReq CallbackRequest
	var metadata runtime.ServerMetadata

	if err := req.ParseForm(); err != nil {
		return nil, metadata, status.Errorf(codes.InvalidArgument, "%v", err)
	}
	if err := runtime.PopulateQueryParameters(&protoReq, req.Form, filter_OauthCallbackService_Callback_0); err != nil {
		return nil, metadata, status.Errorf(codes.InvalidArgument, "%v", err)
	}

	msg, err := client.Callback(ctx, &protoReq, grpc.Header(&metadata.HeaderMD), grpc.Trailer(&metadata.TrailerMD))
	return msg, metadata, err

}

func local_request_OauthCallbackService_Callback_0(ctx context.Context, marshaler runtime.Marshaler, server OauthCallbackServiceServer, req *http.Request, pathParams map[string]string) (proto.Message, runtime.ServerMetadata, error) {
	var protoReq CallbackRequest
	var metadata runtime.ServerMetadata

	if err := req.ParseForm(); err != nil {
		return nil, metadata, status.Errorf(codes.InvalidArgument, "%v", err)
	}
	if err := runtime.PopulateQueryParameters(&protoReq, req.Form, filter_OauthCallbackService_Callback_0); err != nil {
		return nil, metadata, status.Errorf(codes.InvalidArgument, "%v", err)
	}

	msg, err := server.Callback(ctx, &protoReq)
	return msg, metadata, err

}

// RegisterOauth2ServiceHandlerServer registers the http handlers for service Oauth2Service to "mux".
// UnaryRPC     :call Oauth2ServiceServer directly.
// StreamingRPC :currently unsupported pending https://github.com/grpc/grpc-go/issues/906.
// Note that using this registration option will cause many gRPC library features to stop working. Consider using RegisterOauth2ServiceHandlerFromEndpoint instead.
// GRPC interceptors will not work for this type of registration. To use interceptors, you must use the "runtime.WithMiddlewares" option in the "runtime.NewServeMux" call.
func RegisterOauth2ServiceHandlerServer(ctx context.Context, mux *runtime.ServeMux, server Oauth2ServiceServer) error {

	mux.Handle("GET", pattern_Oauth2Service_GetAuthorizeCode_0, func(w http.ResponseWriter, req *http.Request, pathParams map[string]string) {
		ctx, cancel := context.WithCancel(req.Context())
		defer cancel()
		var stream runtime.ServerTransportStream
		ctx = grpc.NewContextWithServerTransportStream(ctx, &stream)
		inboundMarshaler, outboundMarshaler := runtime.MarshalerForRequest(mux, req)
		var err error
		var annotatedContext context.Context
		annotatedContext, err = runtime.AnnotateIncomingContext(ctx, mux, req, "/grpcoauth.v1.Oauth2Service/GetAuthorizeCode", runtime.WithHTTPPathPattern("/authorize"))
		if err != nil {
			runtime.HTTPError(ctx, mux, outboundMarshaler, w, req, err)
			return
		}
		resp, md, err := local_request_Oauth2Service_GetAuthorizeCode_0(annotatedContext, inboundMarshaler, server, req, pathParams)
		md.HeaderMD, md.TrailerMD = metadata.Join(md.HeaderMD, stream.Header()), metadata.Join(md.TrailerMD, stream.Trailer())
		annotatedContext = runtime.NewServerMetadataContext(annotatedContext, md)
		if err != nil {
			runtime.HTTPError(annotatedContext, mux, outboundMarshaler, w, req, err)
			return
		}

		forward_Oauth2Service_GetAuthorizeCode_0(annotatedContext, mux, outboundMarshaler, w, req, resp, mux.GetForwardResponseOptions()...)

	})

	return nil
}

// RegisterOauthCallbackServiceHandlerServer registers the http handlers for service OauthCallbackService to "mux".
// UnaryRPC     :call OauthCallbackServiceServer directly.
// StreamingRPC :currently unsupported pending https://github.com/grpc/grpc-go/issues/906.
// Note that using this registration option will cause many gRPC library features to stop working. Consider using RegisterOauthCallbackServiceHandlerFromEndpoint instead.
// GRPC interceptors will not work for this type of registration. To use interceptors, you must use the "runtime.WithMiddlewares" option in the "runtime.NewServeMux" call.
func RegisterOauthCallbackServiceHandlerServer(ctx context.Context, mux *runtime.ServeMux, server OauthCallbackServiceServer) error {

	mux.Handle("GET", pattern_OauthCallbackService_Callback_0, func(w http.ResponseWriter, req *http.Request, pathParams map[string]string) {
		ctx, cancel := context.WithCancel(req.Context())
		defer cancel()
		var stream runtime.ServerTransportStream
		ctx = grpc.NewContextWithServerTransportStream(ctx, &stream)
		inboundMarshaler, outboundMarshaler := runtime.MarshalerForRequest(mux, req)
		var err error
		var annotatedContext context.Context
		annotatedContext, err = runtime.AnnotateIncomingContext(ctx, mux, req, "/grpcoauth.v1.OauthCallbackService/Callback", runtime.WithHTTPPathPattern("/callback/*"))
		if err != nil {
			runtime.HTTPError(ctx, mux, outboundMarshaler, w, req, err)
			return
		}
		resp, md, err := local_request_OauthCallbackService_Callback_0(annotatedContext, inboundMarshaler, server, req, pathParams)
		md.HeaderMD, md.TrailerMD = metadata.Join(md.HeaderMD, stream.Header()), metadata.Join(md.TrailerMD, stream.Trailer())
		annotatedContext = runtime.NewServerMetadataContext(annotatedContext, md)
		if err != nil {
			runtime.HTTPError(annotatedContext, mux, outboundMarshaler, w, req, err)
			return
		}

		forward_OauthCallbackService_Callback_0(annotatedContext, mux, outboundMarshaler, w, req, resp, mux.GetForwardResponseOptions()...)

	})

	return nil
}

// RegisterOauth2ServiceHandlerFromEndpoint is same as RegisterOauth2ServiceHandler but
// automatically dials to "endpoint" and closes the connection when "ctx" gets done.
func RegisterOauth2ServiceHandlerFromEndpoint(ctx context.Context, mux *runtime.ServeMux, endpoint string, opts []grpc.DialOption) (err error) {
	conn, err := grpc.NewClient(endpoint, opts...)
	if err != nil {
		return err
	}
	defer func() {
		if err != nil {
			if cerr := conn.Close(); cerr != nil {
				grpclog.Errorf("Failed to close conn to %s: %v", endpoint, cerr)
			}
			return
		}
		go func() {
			<-ctx.Done()
			if cerr := conn.Close(); cerr != nil {
				grpclog.Errorf("Failed to close conn to %s: %v", endpoint, cerr)
			}
		}()
	}()

	return RegisterOauth2ServiceHandler(ctx, mux, conn)
}

// RegisterOauth2ServiceHandler registers the http handlers for service Oauth2Service to "mux".
// The handlers forward requests to the grpc endpoint over "conn".
func RegisterOauth2ServiceHandler(ctx context.Context, mux *runtime.ServeMux, conn *grpc.ClientConn) error {
	return RegisterOauth2ServiceHandlerClient(ctx, mux, NewOauth2ServiceClient(conn))
}

// RegisterOauth2ServiceHandlerClient registers the http handlers for service Oauth2Service
// to "mux". The handlers forward requests to the grpc endpoint over the given implementation of "Oauth2ServiceClient".
// Note: the gRPC framework executes interceptors within the gRPC handler. If the passed in "Oauth2ServiceClient"
// doesn't go through the normal gRPC flow (creating a gRPC client etc.) then it will be up to the passed in
// "Oauth2ServiceClient" to call the correct interceptors. This client ignores the HTTP middlewares.
func RegisterOauth2ServiceHandlerClient(ctx context.Context, mux *runtime.ServeMux, client Oauth2ServiceClient) error {

	mux.Handle("GET", pattern_Oauth2Service_GetAuthorizeCode_0, func(w http.ResponseWriter, req *http.Request, pathParams map[string]string) {
		ctx, cancel := context.WithCancel(req.Context())
		defer cancel()
		inboundMarshaler, outboundMarshaler := runtime.MarshalerForRequest(mux, req)
		var err error
		var annotatedContext context.Context
		annotatedContext, err = runtime.AnnotateContext(ctx, mux, req, "/grpcoauth.v1.Oauth2Service/GetAuthorizeCode", runtime.WithHTTPPathPattern("/authorize"))
		if err != nil {
			runtime.HTTPError(ctx, mux, outboundMarshaler, w, req, err)
			return
		}
		resp, md, err := request_Oauth2Service_GetAuthorizeCode_0(annotatedContext, inboundMarshaler, client, req, pathParams)
		annotatedContext = runtime.NewServerMetadataContext(annotatedContext, md)
		if err != nil {
			runtime.HTTPError(annotatedContext, mux, outboundMarshaler, w, req, err)
			return
		}

		forward_Oauth2Service_GetAuthorizeCode_0(annotatedContext, mux, outboundMarshaler, w, req, resp, mux.GetForwardResponseOptions()...)

	})

	return nil
}

var (
	pattern_Oauth2Service_GetAuthorizeCode_0 = runtime.MustPattern(runtime.NewPattern(1, []int{2, 0}, []string{"authorize"}, ""))
)

var (
	forward_Oauth2Service_GetAuthorizeCode_0 = runtime.ForwardResponseMessage
)

// RegisterOauthCallbackServiceHandlerFromEndpoint is same as RegisterOauthCallbackServiceHandler but
// automatically dials to "endpoint" and closes the connection when "ctx" gets done.
func RegisterOauthCallbackServiceHandlerFromEndpoint(ctx context.Context, mux *runtime.ServeMux, endpoint string, opts []grpc.DialOption) (err error) {
	conn, err := grpc.NewClient(endpoint, opts...)
	if err != nil {
		return err
	}
	defer func() {
		if err != nil {
			if cerr := conn.Close(); cerr != nil {
				grpclog.Errorf("Failed to close conn to %s: %v", endpoint, cerr)
			}
			return
		}
		go func() {
			<-ctx.Done()
			if cerr := conn.Close(); cerr != nil {
				grpclog.Errorf("Failed to close conn to %s: %v", endpoint, cerr)
			}
		}()
	}()

	return RegisterOauthCallbackServiceHandler(ctx, mux, conn)
}

// RegisterOauthCallbackServiceHandler registers the http handlers for service OauthCallbackService to "mux".
// The handlers forward requests to the grpc endpoint over "conn".
func RegisterOauthCallbackServiceHandler(ctx context.Context, mux *runtime.ServeMux, conn *grpc.ClientConn) error {
	return RegisterOauthCallbackServiceHandlerClient(ctx, mux, NewOauthCallbackServiceClient(conn))
}

// RegisterOauthCallbackServiceHandlerClient registers the http handlers for service OauthCallbackService
// to "mux". The handlers forward requests to the grpc endpoint over the given implementation of "OauthCallbackServiceClient".
// Note: the gRPC framework executes interceptors within the gRPC handler. If the passed in "OauthCallbackServiceClient"
// doesn't go through the normal gRPC flow (creating a gRPC client etc.) then it will be up to the passed in
// "OauthCallbackServiceClient" to call the correct interceptors. This client ignores the HTTP middlewares.
func RegisterOauthCallbackServiceHandlerClient(ctx context.Context, mux *runtime.ServeMux, client OauthCallbackServiceClient) error {

	mux.Handle("GET", pattern_OauthCallbackService_Callback_0, func(w http.ResponseWriter, req *http.Request, pathParams map[string]string) {
		ctx, cancel := context.WithCancel(req.Context())
		defer cancel()
		inboundMarshaler, outboundMarshaler := runtime.MarshalerForRequest(mux, req)
		var err error
		var annotatedContext context.Context
		annotatedContext, err = runtime.AnnotateContext(ctx, mux, req, "/grpcoauth.v1.OauthCallbackService/Callback", runtime.WithHTTPPathPattern("/callback/*"))
		if err != nil {
			runtime.HTTPError(ctx, mux, outboundMarshaler, w, req, err)
			return
		}
		resp, md, err := request_OauthCallbackService_Callback_0(annotatedContext, inboundMarshaler, client, req, pathParams)
		annotatedContext = runtime.NewServerMetadataContext(annotatedContext, md)
		if err != nil {
			runtime.HTTPError(annotatedContext, mux, outboundMarshaler, w, req, err)
			return
		}

		forward_OauthCallbackService_Callback_0(annotatedContext, mux, outboundMarshaler, w, req, resp, mux.GetForwardResponseOptions()...)

	})

	return nil
}

var (
	pattern_OauthCallbackService_Callback_0 = runtime.MustPattern(runtime.NewPattern(1, []int{2, 0, 1, 0}, []string{"callback"}, ""))
)

var (
	forward_OauthCallbackService_Callback_0 = runtime.ForwardResponseMessage
)
