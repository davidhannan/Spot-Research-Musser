code directory

currently the "grpc-camera-pi" directory contains a program which detects faces in the raspberry pi camera feed and displays the output in a webpage. It then sends the x, y, h, w values of where the face is in the frame over grpc to a receiver program in "grpc receiver"


"grpc-receiver" directory contains a program that connects to a program that can send grpc and it will receive the messages that are sent. I have been using this to connect to the camera web app and test grpc functions.

"grpc-message-test" contains the first grpc program I wrote that simply sends a grpc to a server.

"grpc example" contains the example grpc code provided from the grpc repo
