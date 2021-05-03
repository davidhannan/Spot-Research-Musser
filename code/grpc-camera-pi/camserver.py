import grpc
from concurrent import futures
import time

import message_pb2
import message_pb2_grpc

import message

from flask import Flask, Response
import cv2

# class MessageServicer(message_pb2_grpc.MessengerServicer):

#     def getMsg(self, request, context):
#         response = message_pb2.msg()
#         response.message = message.getMsg(request.message)
#         print(response.message)
#         return response

# server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))


# message_pb2_grpc.add_MessengerServicer_to_server(MessageServicer(), server)

# # listen on port 50051
# print('Starting server. Listening on port 50051.')
# server.add_insecure_port('[::]:50051')
# server.start()

channel = grpc.insecure_channel('192.168.1.171:50051')

stub = message_pb2_grpc.MessengerStub(channel)

inp = input()

message = message_pb2.msg(message=inp)

response = stub.getMsg(message)

print(response.message)

app = Flask(__name__)
video = cv2.VideoCapture(0)
@app.route('/')
def index():
    return inp
def gen(video):
    while True:
        success, image = video.read()
        ret, jpeg = cv2.imencode('.jpg', image)
        frame = jpeg.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
@app.route('/video_feed')
def video_feed():
    global video
    return Response(gen(video),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2204, threaded=True)

# since server.start() will not block,
# a sleep-loop is added to keep alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)

