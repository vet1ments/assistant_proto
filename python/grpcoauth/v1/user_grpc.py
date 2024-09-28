# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: grpcoauth/v1/user.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import buf.validate.validate_pb2
import google.api.annotations_pb2
import google.protobuf.empty_pb2
import grpcoauth.v1.user_pb2


class UserServiceBase(abc.ABC):

    @abc.abstractmethod
    async def GetAccessTokenInfo(self, stream: 'grpclib.server.Stream[google.protobuf.empty_pb2.Empty, grpcoauth.v1.user_pb2.GetAccessTokenInfoResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetUserMe(self, stream: 'grpclib.server.Stream[google.protobuf.empty_pb2.Empty, grpcoauth.v1.user_pb2.GetUserMeResponse]') -> None:
        pass

    @abc.abstractmethod
    async def UserLogout(self, stream: 'grpclib.server.Stream[google.protobuf.empty_pb2.Empty, grpcoauth.v1.user_pb2.UserLogoutResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/grpcoauth.v1.UserService/GetAccessTokenInfo': grpclib.const.Handler(
                self.GetAccessTokenInfo,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.protobuf.empty_pb2.Empty,
                grpcoauth.v1.user_pb2.GetAccessTokenInfoResponse,
            ),
            '/grpcoauth.v1.UserService/GetUserMe': grpclib.const.Handler(
                self.GetUserMe,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.protobuf.empty_pb2.Empty,
                grpcoauth.v1.user_pb2.GetUserMeResponse,
            ),
            '/grpcoauth.v1.UserService/UserLogout': grpclib.const.Handler(
                self.UserLogout,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.protobuf.empty_pb2.Empty,
                grpcoauth.v1.user_pb2.UserLogoutResponse,
            ),
        }


class UserServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.GetAccessTokenInfo = grpclib.client.UnaryUnaryMethod(
            channel,
            '/grpcoauth.v1.UserService/GetAccessTokenInfo',
            google.protobuf.empty_pb2.Empty,
            grpcoauth.v1.user_pb2.GetAccessTokenInfoResponse,
        )
        self.GetUserMe = grpclib.client.UnaryUnaryMethod(
            channel,
            '/grpcoauth.v1.UserService/GetUserMe',
            google.protobuf.empty_pb2.Empty,
            grpcoauth.v1.user_pb2.GetUserMeResponse,
        )
        self.UserLogout = grpclib.client.UnaryUnaryMethod(
            channel,
            '/grpcoauth.v1.UserService/UserLogout',
            google.protobuf.empty_pb2.Empty,
            grpcoauth.v1.user_pb2.UserLogoutResponse,
        )
