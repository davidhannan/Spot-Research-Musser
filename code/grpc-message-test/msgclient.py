import grpc

import message_pb2
import message_pb2_grpc

#set address to address of pi on network
channel = grpc.insecure_channel('192.168.1.239:50051')

stub = message_pb2_grpc.MessengerStub(channel)

inp = input()

message = message_pb2.msg(message=inp)

response = stub.getMsg(message)

print(response.message)