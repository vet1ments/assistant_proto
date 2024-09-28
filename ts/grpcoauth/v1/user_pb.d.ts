import * as jspb from 'google-protobuf'

import * as buf_validate_validate_pb from '../../buf/validate/validate_pb'; // proto import: "buf/validate/validate.proto"
import * as google_api_annotations_pb from '../../google/api/annotations_pb'; // proto import: "google/api/annotations.proto"
import * as google_protobuf_empty_pb from 'google-protobuf/google/protobuf/empty_pb'; // proto import: "google/protobuf/empty.proto"


export class User extends jspb.Message {
  getId(): string;
  setId(value: string): User;

  getName(): string;
  setName(value: string): User;

  getPhoneNumber(): string;
  setPhoneNumber(value: string): User;

  getNickname(): string;
  setNickname(value: string): User;

  getThumbnail(): string;
  setThumbnail(value: string): User;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): User.AsObject;
  static toObject(includeInstance: boolean, msg: User): User.AsObject;
  static serializeBinaryToWriter(message: User, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): User;
  static deserializeBinaryFromReader(message: User, reader: jspb.BinaryReader): User;
}

export namespace User {
  export type AsObject = {
    id: string,
    name: string,
    phoneNumber: string,
    nickname: string,
    thumbnail: string,
  }
}

export class GetAccessTokenInfoResponse extends jspb.Message {
  getId(): string;
  setId(value: string): GetAccessTokenInfoResponse;

  getExpiresIn(): number;
  setExpiresIn(value: number): GetAccessTokenInfoResponse;

  getAppId(): string;
  setAppId(value: string): GetAccessTokenInfoResponse;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAccessTokenInfoResponse.AsObject;
  static toObject(includeInstance: boolean, msg: GetAccessTokenInfoResponse): GetAccessTokenInfoResponse.AsObject;
  static serializeBinaryToWriter(message: GetAccessTokenInfoResponse, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAccessTokenInfoResponse;
  static deserializeBinaryFromReader(message: GetAccessTokenInfoResponse, reader: jspb.BinaryReader): GetAccessTokenInfoResponse;
}

export namespace GetAccessTokenInfoResponse {
  export type AsObject = {
    id: string,
    expiresIn: number,
    appId: string,
  }
}

export class GetUserMeResponse extends jspb.Message {
  getId(): string;
  setId(value: string): GetUserMeResponse;

  getName(): string;
  setName(value: string): GetUserMeResponse;

  getPhoneNumber(): string;
  setPhoneNumber(value: string): GetUserMeResponse;

  getNickname(): string;
  setNickname(value: string): GetUserMeResponse;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetUserMeResponse.AsObject;
  static toObject(includeInstance: boolean, msg: GetUserMeResponse): GetUserMeResponse.AsObject;
  static serializeBinaryToWriter(message: GetUserMeResponse, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetUserMeResponse;
  static deserializeBinaryFromReader(message: GetUserMeResponse, reader: jspb.BinaryReader): GetUserMeResponse;
}

export namespace GetUserMeResponse {
  export type AsObject = {
    id: string,
    name: string,
    phoneNumber: string,
    nickname: string,
  }
}

export class UserLogoutResponse extends jspb.Message {
  getId(): string;
  setId(value: string): UserLogoutResponse;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UserLogoutResponse.AsObject;
  static toObject(includeInstance: boolean, msg: UserLogoutResponse): UserLogoutResponse.AsObject;
  static serializeBinaryToWriter(message: UserLogoutResponse, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UserLogoutResponse;
  static deserializeBinaryFromReader(message: UserLogoutResponse, reader: jspb.BinaryReader): UserLogoutResponse;
}

export namespace UserLogoutResponse {
  export type AsObject = {
    id: string,
  }
}

