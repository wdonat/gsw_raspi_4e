from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

camera = PiCamera()
camera.resolution = (640, 480)
rawCapture = PiRGBArray(camera)

time.sleep(0.1)

camera.capture(rawCapture, format='bgr')
image = rawCapture.array

cv2.imshow('Camera', image)
cv2.waitKey(0)

