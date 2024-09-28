# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: grpcoauth/v1/user.proto
# Protobuf Python Version: 5.28.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    2,
    '',
    'grpcoauth/v1/user.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from buf.validate import validate_pb2 as buf_dot_validate_dot_validate__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17grpcoauth/v1/user.proto\x12\x0cgrpcoauth.v1\x1a\x1b\x62uf/validate/validate.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1bgoogle/protobuf/empty.proto\"\xd0\x01\n\x04User\x12%\n\x02id\x18\x01 \x01(\tB\x15\xbaH\x12r\x10\x32\x0e^[a-z0-9]{24}$R\x02id\x12\x1d\n\x04name\x18\x02 \x01(\tB\t\xbaH\x06r\x04\x10\x02\x18\x14R\x04name\x12?\n\x0cphone_number\x18\x03 \x01(\tB\x1c\xbaH\x19r\x17\x32\x15^010[0-9]{4}[0-9]{4}$R\x0bphoneNumber\x12#\n\x08nickname\x18\x04 \x01(\tB\x07\xbaH\x04r\x02\x18\x14R\x08nickname\x12\x1c\n\tthumbnail\x18\x05 \x01(\tR\tthumbnail\"\x1a\n\x04test\x12\x12\n\x04test\x18\x03 \x01(\tR\x04test\"b\n\x1aGetAccessTokenInfoResponse\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x1d\n\nexpires_in\x18\x02 \x01(\x03R\texpiresIn\x12\x15\n\x06\x61pp_id\x18\x03 \x01(\tR\x05\x61ppId\"v\n\x11GetUserMeResponse\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12!\n\x0cphone_number\x18\x03 \x01(\tR\x0bphoneNumber\x12\x1a\n\x08nickname\x18\x04 \x01(\tR\x08nickname\"$\n\x12UserLogoutResponse\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id2\xbc\x02\n\x0bUserService\x12w\n\x12GetAccessTokenInfo\x12\x16.google.protobuf.Empty\x1a(.grpcoauth.v1.GetAccessTokenInfoResponse\"\x1f\x82\xd3\xe4\x93\x02\x19\x12\x17/user/access_token_info\x12V\n\tGetUserMe\x12\x16.google.protobuf.Empty\x1a\x1f.grpcoauth.v1.GetUserMeResponse\"\x10\x82\xd3\xe4\x93\x02\n\x12\x08/user/me\x12\\\n\nUserLogout\x12\x16.google.protobuf.Empty\x1a .grpcoauth.v1.UserLogoutResponse\"\x14\x82\xd3\xe4\x93\x02\x0e\x12\x0c/user/logoutB\xaa\x01\n\x10\x63om.grpcoauth.v1B\tUserProtoP\x01Z:github.com/vet1ments/grpcoauth/go/grpcoauth/v1;grpcoauthv1\xa2\x02\x03GXX\xaa\x02\x0cGrpcoauth.V1\xca\x02\x0cGrpcoauth\\V1\xe2\x02\x18Grpcoauth\\V1\\GPBMetadata\xea\x02\rGrpcoauth::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'grpcoauth.v1.user_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\020com.grpcoauth.v1B\tUserProtoP\001Z:github.com/vet1ments/grpcoauth/go/grpcoauth/v1;grpcoauthv1\242\002\003GXX\252\002\014Grpcoauth.V1\312\002\014Grpcoauth\\V1\342\002\030Grpcoauth\\V1\\GPBMetadata\352\002\rGrpcoauth::V1'
  _globals['_USER'].fields_by_name['id']._loaded_options = None
  _globals['_USER'].fields_by_name['id']._serialized_options = b'\272H\022r\0202\016^[a-z0-9]{24}$'
  _globals['_USER'].fields_by_name['name']._loaded_options = None
  _globals['_USER'].fields_by_name['name']._serialized_options = b'\272H\006r\004\020\002\030\024'
  _globals['_USER'].fields_by_name['phone_number']._loaded_options = None
  _globals['_USER'].fields_by_name['phone_number']._serialized_options = b'\272H\031r\0272\025^010[0-9]{4}[0-9]{4}$'
  _globals['_USER'].fields_by_name['nickname']._loaded_options = None
  _globals['_USER'].fields_by_name['nickname']._serialized_options = b'\272H\004r\002\030\024'
  _globals['_USERSERVICE'].methods_by_name['GetAccessTokenInfo']._loaded_options = None
  _globals['_USERSERVICE'].methods_by_name['GetAccessTokenInfo']._serialized_options = b'\202\323\344\223\002\031\022\027/user/access_token_info'
  _globals['_USERSERVICE'].methods_by_name['GetUserMe']._loaded_options = None
  _globals['_USERSERVICE'].methods_by_name['GetUserMe']._serialized_options = b'\202\323\344\223\002\n\022\010/user/me'
  _globals['_USERSERVICE'].methods_by_name['UserLogout']._loaded_options = None
  _globals['_USERSERVICE'].methods_by_name['UserLogout']._serialized_options = b'\202\323\344\223\002\016\022\014/user/logout'
  _globals['_USER']._serialized_start=130
  _globals['_USER']._serialized_end=338
  _globals['_TEST']._serialized_start=340
  _globals['_TEST']._serialized_end=366
  _globals['_GETACCESSTOKENINFORESPONSE']._serialized_start=368
  _globals['_GETACCESSTOKENINFORESPONSE']._serialized_end=466
  _globals['_GETUSERMERESPONSE']._serialized_start=468
  _globals['_GETUSERMERESPONSE']._serialized_end=586
  _globals['_USERLOGOUTRESPONSE']._serialized_start=588
  _globals['_USERLOGOUTRESPONSE']._serialized_end=624
  _globals['_USERSERVICE']._serialized_start=627
  _globals['_USERSERVICE']._serialized_end=943
# @@protoc_insertion_point(module_scope)
