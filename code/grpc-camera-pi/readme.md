Raspberry Pi 4 8gb, Pi Camera

Ubuntu server

made a virtualenv for opencv and other dependcies

[install openCV](https://linuxize.com/post/how-to-install-opencv-on-ubuntu-18-04/)

[enable raspistill - optional](https://raspberrypi.stackexchange.com/questions/37359/how-to-use-raspistill-on-ubuntu)

[view video stream in browser with opencv](https://manivannan-ai.medium.com/live-webcam-flask-opencv-python-26a61fee831)

[detect face with opencv](https://towardsdatascience.com/how-to-detect-objects-in-real-time-using-opencv-and-python-c1ba0c2c69c0)

The camserver.py program runs in conjunction with the receiver.py program found in the "grpc receiver" directory. camserver.py runs a flask webserver which displays the feed from the raspberry pi camera. This feed is processed with opencv which detects faces. The x, y, w, h values are then sent to the receiver.py program via grpc. These values could then be used by a program to do something else. This program is more of an exercise in the use of grpc and computer vision.

TODO:

do something with the coordinate values
