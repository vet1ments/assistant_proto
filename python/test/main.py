from grpclib.client import Channel
import grpcoauth.v1.user_grpc as pb2_grpc
import grpcoauth.v1.user_pb2 as pb2
import asyncio
import typing as t
async def main():
    async with Channel('127.0.0.1', 9000) as channel:
        client = pb2_grpc.UserServiceStub(channel)
        res = await client.GetUser(pb2.GetUserRequest(id="abc1234567894561235qqqq"))
        print(type(res.user.id))

if __name__ == '__main__':
    asyncio.run(main())