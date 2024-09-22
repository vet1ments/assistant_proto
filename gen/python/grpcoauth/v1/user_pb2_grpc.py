# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from grpcoauth.v1 import user_pb2 as grpcoauth_dot_v1_dot_user__pb2


class UserServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetUser = channel.unary_unary(
                '/grpcoauth.v1.UserService/GetUser',
                request_serializer=grpcoauth_dot_v1_dot_user__pb2.GetUserRequest.SerializeToString,
                response_deserializer=grpcoauth_dot_v1_dot_user__pb2.GetUserResponse.FromString,
                _registered_method=True)
        self.CreateUser = channel.unary_unary(
                '/grpcoauth.v1.UserService/CreateUser',
                request_serializer=grpcoauth_dot_v1_dot_user__pb2.CreateUserRequest.SerializeToString,
                response_deserializer=grpcoauth_dot_v1_dot_user__pb2.CreateUserResponse.FromString,
                _registered_method=True)
        self.GetUserByToken = channel.unary_unary(
                '/grpcoauth.v1.UserService/GetUserByToken',
                request_serializer=grpcoauth_dot_v1_dot_user__pb2.GetUserByTokenRequest.SerializeToString,
                response_deserializer=grpcoauth_dot_v1_dot_user__pb2.GetUserByTokenResponse.FromString,
                _registered_method=True)
        self.GetUserListByToken = channel.unary_unary(
                '/grpcoauth.v1.UserService/GetUserListByToken',
                request_serializer=grpcoauth_dot_v1_dot_user__pb2.GetUserListByTokenRequest.SerializeToString,
                response_deserializer=grpcoauth_dot_v1_dot_user__pb2.GetUserListByTokenResponse.FromString,
                _registered_method=True)


class UserServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetUserByToken(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetUserListByToken(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_UserServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetUser': grpc.unary_unary_rpc_method_handler(
                    servicer.GetUser,
                    request_deserializer=grpcoauth_dot_v1_dot_user__pb2.GetUserRequest.FromString,
                    response_serializer=grpcoauth_dot_v1_dot_user__pb2.GetUserResponse.SerializeToString,
            ),
            'CreateUser': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateUser,
                    request_deserializer=grpcoauth_dot_v1_dot_user__pb2.CreateUserRequest.FromString,
                    response_serializer=grpcoauth_dot_v1_dot_user__pb2.CreateUserResponse.SerializeToString,
            ),
            'GetUserByToken': grpc.unary_unary_rpc_method_handler(
                    servicer.GetUserByToken,
                    request_deserializer=grpcoauth_dot_v1_dot_user__pb2.GetUserByTokenRequest.FromString,
                    response_serializer=grpcoauth_dot_v1_dot_user__pb2.GetUserByTokenResponse.SerializeToString,
            ),
            'GetUserListByToken': grpc.unary_unary_rpc_method_handler(
                    servicer.GetUserListByToken,
                    request_deserializer=grpcoauth_dot_v1_dot_user__pb2.GetUserListByTokenRequest.FromString,
                    response_serializer=grpcoauth_dot_v1_dot_user__pb2.GetUserListByTokenResponse.SerializeToString,
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
    def GetUser(request,
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
            '/grpcoauth.v1.UserService/GetUser',
            grpcoauth_dot_v1_dot_user__pb2.GetUserRequest.SerializeToString,
            grpcoauth_dot_v1_dot_user__pb2.GetUserResponse.FromString,
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
    def CreateUser(request,
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
            '/grpcoauth.v1.UserService/CreateUser',
            grpcoauth_dot_v1_dot_user__pb2.CreateUserRequest.SerializeToString,
            grpcoauth_dot_v1_dot_user__pb2.CreateUserResponse.FromString,
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
    def GetUserByToken(request,
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
            '/grpcoauth.v1.UserService/GetUserByToken',
            grpcoauth_dot_v1_dot_user__pb2.GetUserByTokenRequest.SerializeToString,
            grpcoauth_dot_v1_dot_user__pb2.GetUserByTokenResponse.FromString,
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
    def GetUserListByToken(request,
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
            '/grpcoauth.v1.UserService/GetUserListByToken',
            grpcoauth_dot_v1_dot_user__pb2.GetUserListByTokenRequest.SerializeToString,
            grpcoauth_dot_v1_dot_user__pb2.GetUserListByTokenResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
