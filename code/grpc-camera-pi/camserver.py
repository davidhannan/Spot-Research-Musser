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

#inp = input()







app = Flask(__name__)
imcap = cv2.VideoCapture(0)
imcap.set(3, 640) # set width as 640
imcap.set(4, 480) # set height as 480

faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
@app.route('/')
def index():
    return inp
def gen(video):
    while True:
        success, img = imcap.read()
        imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(imgGray, 1.3, 5) 
        for (x, y, w, h) in faces:
            img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255,   0), 3)
            coords = str(x) + ", " + str(y) + ", " + str(w) + ", " + str(h)
            
            message = message_pb2.msg(message=coords)
            response = stub.getMsg(message)
            print(response.message)
        #cv2.imshow('face_detect', img)
        ret, jpeg = cv2.imencode('.jpg', img)
        frame = jpeg.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
@app.route('/video_feed')
def video_feed():
    global video
    return Response(gen(imcap),
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

