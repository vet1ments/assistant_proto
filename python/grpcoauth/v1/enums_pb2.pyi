from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class GrantType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GRANT_TYPE_UNSPECIFIED: _ClassVar[GrantType]
    GRANT_TYPE_AUTHORIZATION_CODE: _ClassVar[GrantType]
    GRANT_TYPE_REFRESH_TOKEN: _ClassVar[GrantType]

class Role(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ROLE_UNSPECIFIED: _ClassVar[Role]
    ROLE_ADMIN: _ClassVar[Role]
    ROLE_USER: _ClassVar[Role]
GRANT_TYPE_UNSPECIFIED: GrantType
GRANT_TYPE_AUTHORIZATION_CODE: GrantType
GRANT_TYPE_REFRESH_TOKEN: GrantType
ROLE_UNSPECIFIED: Role
ROLE_ADMIN: Role
ROLE_USER: Role
