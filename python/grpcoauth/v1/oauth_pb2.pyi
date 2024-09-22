from grpcoauth.v1 import enums_pb2 as _enums_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OauthApp(_message.Message):
    __slots__ = ("role", "id", "name", "redirect_uri")
    ROLE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    REDIRECT_URI_FIELD_NUMBER: _ClassVar[int]
    role: _enums_pb2.RoleType
    id: str
    name: str
    redirect_uri: str
    def __init__(self, role: _Optional[_Union[_enums_pb2.RoleType, str]] = ..., id: _Optional[str] = ..., name: _Optional[str] = ..., redirect_uri: _Optional[str] = ...) -> None: ...

class OauthAppUser(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetOauthAppTokenInfoRequest(_message.Message):
    __slots__ = ("token",)
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    token: str
    def __init__(self, token: _Optional[str] = ...) -> None: ...

class GetOauthAppTokenInfoResponse(_message.Message):
    __slots__ = ("app",)
    APP_FIELD_NUMBER: _ClassVar[int]
    app: OauthApp
    def __init__(self, app: _Optional[_Union[OauthApp, _Mapping]] = ...) -> None: ...

class GetOauthAppUserRequest(_message.Message):
    __slots__ = ("token",)
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    token: str
    def __init__(self, token: _Optional[str] = ...) -> None: ...

class GetOauthAppUserResponse(_message.Message):
    __slots__ = ("user",)
    USER_FIELD_NUMBER: _ClassVar[int]
    user: OauthApp
    def __init__(self, user: _Optional[_Union[OauthApp, _Mapping]] = ...) -> None: ...

class GetOauthAppUserListRequest(_message.Message):
    __slots__ = ("token",)
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    token: str
    def __init__(self, token: _Optional[str] = ...) -> None: ...

class GetOauthAppUserListResponse(_message.Message):
    __slots__ = ("users",)
    USERS_FIELD_NUMBER: _ClassVar[int]
    users: _containers.RepeatedCompositeFieldContainer[OauthApp]
    def __init__(self, users: _Optional[_Iterable[_Union[OauthApp, _Mapping]]] = ...) -> None: ...

class CreateOauthAdminAppRequest(_message.Message):
    __slots__ = ("name", "redirect_uri")
    NAME_FIELD_NUMBER: _ClassVar[int]
    REDIRECT_URI_FIELD_NUMBER: _ClassVar[int]
    name: str
    redirect_uri: str
    def __init__(self, name: _Optional[str] = ..., redirect_uri: _Optional[str] = ...) -> None: ...

class CreateOauthAdminAppResponse(_message.Message):
    __slots__ = ("response", "description")
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    response: _enums_pb2.ResponseType
    description: str
    def __init__(self, response: _Optional[_Union[_enums_pb2.ResponseType, str]] = ..., description: _Optional[str] = ...) -> None: ...

class CreateOauthUserAppRequest(_message.Message):
    __slots__ = ("name", "redirect_uri")
    NAME_FIELD_NUMBER: _ClassVar[int]
    REDIRECT_URI_FIELD_NUMBER: _ClassVar[int]
    name: str
    redirect_uri: str
    def __init__(self, name: _Optional[str] = ..., redirect_uri: _Optional[str] = ...) -> None: ...

class CreateOauthUserAppResponse(_message.Message):
    __slots__ = ("response", "description")
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    response: _enums_pb2.ResponseType
    description: str
    def __init__(self, response: _Optional[_Union[_enums_pb2.ResponseType, str]] = ..., description: _Optional[str] = ...) -> None: ...

class GetAuthorizeCodeRequest(_message.Message):
    __slots__ = ("login_type", "user_info", "code", "state")
    class UserInfo(_message.Message):
        __slots__ = ("email", "pw")
        EMAIL_FIELD_NUMBER: _ClassVar[int]
        PW_FIELD_NUMBER: _ClassVar[int]
        email: str
        pw: str
        def __init__(self, email: _Optional[str] = ..., pw: _Optional[str] = ...) -> None: ...
    LOGIN_TYPE_FIELD_NUMBER: _ClassVar[int]
    USER_INFO_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    login_type: _enums_pb2.LoginType
    user_info: GetAuthorizeCodeRequest.UserInfo
    code: str
    state: str
    def __init__(self, login_type: _Optional[_Union[_enums_pb2.LoginType, str]] = ..., user_info: _Optional[_Union[GetAuthorizeCodeRequest.UserInfo, _Mapping]] = ..., code: _Optional[str] = ..., state: _Optional[str] = ...) -> None: ...

class GetAuthorizeCodeResponse(_message.Message):
    __slots__ = ("code", "state")
    CODE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    code: str
    state: str
    def __init__(self, code: _Optional[str] = ..., state: _Optional[str] = ...) -> None: ...

class GetTokenRequest(_message.Message):
    __slots__ = ("grant_type", "client_id", "redirect_uri", "code", "client_secret", "refresh_token")
    GRANT_TYPE_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    REDIRECT_URI_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    CLIENT_SECRET_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    grant_type: _enums_pb2.GrantType
    client_id: str
    redirect_uri: str
    code: str
    client_secret: str
    refresh_token: str
    def __init__(self, grant_type: _Optional[_Union[_enums_pb2.GrantType, str]] = ..., client_id: _Optional[str] = ..., redirect_uri: _Optional[str] = ..., code: _Optional[str] = ..., client_secret: _Optional[str] = ..., refresh_token: _Optional[str] = ...) -> None: ...

class GetTokenResponse(_message.Message):
    __slots__ = ("token_type", "access_token", "expires_id", "refresh_token", "refresh_token_expires_in", "scope")
    TOKEN_TYPE_FIELD_NUMBER: _ClassVar[int]
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_ID_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TOKEN_EXPIRES_IN_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    token_type: _enums_pb2.TokenType
    access_token: str
    expires_id: int
    refresh_token: str
    refresh_token_expires_in: int
    scope: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, token_type: _Optional[_Union[_enums_pb2.TokenType, str]] = ..., access_token: _Optional[str] = ..., expires_id: _Optional[int] = ..., refresh_token: _Optional[str] = ..., refresh_token_expires_in: _Optional[int] = ..., scope: _Optional[_Iterable[str]] = ...) -> None: ...
