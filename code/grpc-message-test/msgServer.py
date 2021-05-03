import grpc
from concurrent import futures
import time

import message_pb2
import message_pb2_grpc

import message

class MessageServicer(message_pb2_grpc.MessengerServicer):

    def getMsg(self, request, context):
        response = message_pb2.msg()
        response.message = message.getMsg(request.message)
        print(response.message)
        return response

server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))


message_pb2_grpc.add_MessengerServicer_to_server(MessageServicer(), server)

# listen on port 50051
print('Starting server. Listening on port 50051.')
server.add_insecure_port('[::]:50051')
server.start()

# since server.start() will not block,
# a sleep-loop is added to keep alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)