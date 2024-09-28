# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from grpcoauth.v1 import user_pb2 as grpcoauth_dot_v1_dot_user__pb2


class UserServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetAccessTokenInfo = channel.unary_unary(
                '/grpcoauth.v1.UserService/GetAccessTokenInfo',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=grpcoauth_dot_v1_dot_user__pb2.GetAccessTokenInfoResponse.FromString,
                _registered_method=True)
        self.GetUserMe = channel.unary_unary(
                '/grpcoauth.v1.UserService/GetUserMe',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=grpcoauth_dot_v1_dot_user__pb2.GetUserMeResponse.FromString,
                _registered_method=True)
        self.UserLogout = channel.unary_unary(
                '/grpcoauth.v1.UserService/UserLogout',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=grpcoauth_dot_v1_dot_user__pb2.UserLogoutResponse.FromString,
                _registered_method=True)


class UserServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetAccessTokenInfo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetUserMe(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UserLogout(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_UserServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetAccessTokenInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAccessTokenInfo,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=grpcoauth_dot_v1_dot_user__pb2.GetAccessTokenInfoResponse.SerializeToString,
            ),
            'GetUserMe': grpc.unary_unary_rpc_method_handler(
                    servicer.GetUserMe,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=grpcoauth_dot_v1_dot_user__pb2.GetUserMeResponse.SerializeToString,
            ),
            'UserLogout': grpc.unary_unary_rpc_method_handler(
                    servicer.UserLogout,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=grpcoauth_dot_v1_dot_user__pb2.UserLogoutResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'grpcoauth.v1.UserService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('grpcoauth.v1.UserService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class UserService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetAccessTokenInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/grpcoauth.v1.UserService/GetAccessTokenInfo',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            grpcoauth_dot_v1_dot_user__pb2.GetAccessTokenInfoResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetUserMe(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/grpcoauth.v1.UserService/GetUserMe',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            grpcoauth_dot_v1_dot_user__pb2.GetUserMeResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def UserLogout(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/grpcoauth.v1.UserService/UserLogout',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            grpcoauth_dot_v1_dot_user__pb2.UserLogoutResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
