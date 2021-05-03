code directory

currently the "grpc-camera-pi" directory contains a program which runs a web app that shows the camera feed from the raspberry pi. This program can also receive grpc messages as well. With some slight modification it can send grpc message.

"grpc-receiver" directory contains a program that connects to a program that can send grpc and it will receive the messages that are sent. I have been using this to connect to the camera web app and test grpc functions.

"grpc-message-test" contains the first grpc program I wrote that simply sends a grpc to a server.

"grpc example" contains the example grpc code provided from the grpc repo
