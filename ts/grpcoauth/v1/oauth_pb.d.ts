import * as jspb from 'google-protobuf'

import * as google_api_annotations_pb from '../../google/api/annotations_pb'; // proto import: "google/api/annotations.proto"
import * as google_protobuf_empty_pb from 'google-protobuf/google/protobuf/empty_pb'; // proto import: "google/protobuf/empty.proto"
import * as grpcoauth_v1_enums_pb from '../../grpcoauth/v1/enums_pb'; // proto import: "grpcoauth/v1/enums.proto"


export class OauthApp extends jspb.Message {
  getRole(): grpcoauth_v1_enums_pb.RoleType;
  setRole(value: grpcoauth_v1_enums_pb.RoleType): OauthApp;

  getId(): string;
  setId(value: string): OauthApp;

  getName(): string;
  setName(value: string): OauthApp;

  getRedirectUri(): string;
  setRedirectUri(value: string): OauthApp;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OauthApp.AsObject;
  static toObject(includeInstance: boolean, msg: OauthApp): OauthApp.AsObject;
  static serializeBinaryToWriter(message: OauthApp, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OauthApp;
  static deserializeBinaryFromReader(message: OauthApp, reader: jspb.BinaryReader): OauthApp;
}

export namespace OauthApp {
  export type AsObject = {
    role: grpcoauth_v1_enums_pb.RoleType,
    id: string,
    name: string,
    redirectUri: string,
  }
}

export class GetTokenRequest extends jspb.Message {
  getGrantType(): string;
  setGrantType(value: string): GetTokenRequest;

  getClientId(): string;
  setClientId(value: string): GetTokenRequest;

  getRedirectUri(): string;
  setRedirectUri(value: string): GetTokenRequest;

  getCode(): string;
  setCode(value: string): GetTokenRequest;

  getClientSecret(): string;
  setClientSecret(value: string): GetTokenRequest;

  getRefreshToken(): string;
  setRefreshToken(value: string): GetTokenRequest;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetTokenRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetTokenRequest): GetTokenRequest.AsObject;
  static serializeBinaryToWriter(message: GetTokenRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetTokenRequest;
  static deserializeBinaryFromReader(message: GetTokenRequest, reader: jspb.BinaryReader): GetTokenRequest;
}

export namespace GetTokenRequest {
  export type AsObject = {
    grantType: string,
    clientId: string,
    redirectUri: string,
    code: string,
    clientSecret: string,
    refreshToken: string,
  }
}

export class GetTokenResponse extends jspb.Message {
  getTokenType(): string;
  setTokenType(value: string): GetTokenResponse;

  getAccessToken(): string;
  setAccessToken(value: string): GetTokenResponse;

  getExpiresIn(): number;
  setExpiresIn(value: number): GetTokenResponse;

  getRefreshToken(): string;
  setRefreshToken(value: string): GetTokenResponse;

  getRefreshTokenExpiresIn(): number;
  setRefreshTokenExpiresIn(value: number): GetTokenResponse;

  getScopeList(): Array<string>;
  setScopeList(value: Array<string>): GetTokenResponse;
  clearScopeList(): GetTokenResponse;
  addScope(value: string, index?: number): GetTokenResponse;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetTokenResponse.AsObject;
  static toObject(includeInstance: boolean, msg: GetTokenResponse): GetTokenResponse.AsObject;
  static serializeBinaryToWriter(message: GetTokenResponse, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetTokenResponse;
  static deserializeBinaryFromReader(message: GetTokenResponse, reader: jspb.BinaryReader): GetTokenResponse;
}

export namespace GetTokenResponse {
  export type AsObject = {
    tokenType: string,
    accessToken: string,
    expiresIn: number,
    refreshToken: string,
    refreshTokenExpiresIn: number,
    scopeList: Array<string>,
  }
}

export class GetAuthorizeCodeRequest extends jspb.Message {
  getClientId(): string;
  setClientId(value: string): GetAuthorizeCodeRequest;

  getRedirectUri(): string;
  setRedirectUri(value: string): GetAuthorizeCodeRequest;

  getResponseType(): string;
  setResponseType(value: string): GetAuthorizeCodeRequest;

  getState(): string;
  setState(value: string): GetAuthorizeCodeRequest;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAuthorizeCodeRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAuthorizeCodeRequest): GetAuthorizeCodeRequest.AsObject;
  static serializeBinaryToWriter(message: GetAuthorizeCodeRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAuthorizeCodeRequest;
  static deserializeBinaryFromReader(message: GetAuthorizeCodeRequest, reader: jspb.BinaryReader): GetAuthorizeCodeRequest;
}

export namespace GetAuthorizeCodeRequest {
  export type AsObject = {
    clientId: string,
    redirectUri: string,
    responseType: string,
    state: string,
  }
}

export class GetAuthorizeCodeResponse extends jspb.Message {
  getCode(): string;
  setCode(value: string): GetAuthorizeCodeResponse;

  getState(): string;
  setState(value: string): GetAuthorizeCodeResponse;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAuthorizeCodeResponse.AsObject;
  static toObject(includeInstance: boolean, msg: GetAuthorizeCodeResponse): GetAuthorizeCodeResponse.AsObject;
  static serializeBinaryToWriter(message: GetAuthorizeCodeResponse, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAuthorizeCodeResponse;
  static deserializeBinaryFromReader(message: GetAuthorizeCodeResponse, reader: jspb.BinaryReader): GetAuthorizeCodeResponse;
}

export namespace GetAuthorizeCodeResponse {
  export type AsObject = {
    code: string,
    state: string,
  }
}

export class CallbackRequest extends jspb.Message {
  getCode(): string;
  setCode(value: string): CallbackRequest;

  getState(): string;
  setState(value: string): CallbackRequest;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CallbackRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CallbackRequest): CallbackRequest.AsObject;
  static serializeBinaryToWriter(message: CallbackRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CallbackRequest;
  static deserializeBinaryFromReader(message: CallbackRequest, reader: jspb.BinaryReader): CallbackRequest;
}

export namespace CallbackRequest {
  export type AsObject = {
    code: string,
    state: string,
  }
}

