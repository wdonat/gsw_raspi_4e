import cv2
from picamera.array import PiRGBArray
from picamera import PiCamera
from gpiozero import Button
import time

button = Button(24)
camera = PiCamera()
camera.resolution = (800, 608)
rawCapture = PiRGBArray(camera)

mouth_cascade = cv2.CascadeClassifier('haarcascade_mcs_mouth.xml')

moustache = cv2.imread('moustache.png')
rows, cols, _ = moustache.shape

moustache2gray = cv2.cvtColor(moustache, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(moustache2gray, 10, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

    
while True:
    button.wait_for_press()
    camera.capture(rawCapture, format='bgr')
    cap = rawCapture.array
    cv2.imwrite('face.jpg', cap)
    image = cv2.imread('face.jpg')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    mouths = mouth_cascade.detectMultiScale(gray, 1.5, 15)

    for (x, y, w, h) in mouths:
        roi = image[y-rows+10:y+10, x-5:x+cols-5]
        cv2.imshow('mouth', roi)

        face_bg = cv2.bitwise_and(roi, roi, mask = mask)
        moustache_fg = cv2.bitwise_and(moustache, moustache, mask = mask_inv)
        dst = cv2.add(face_bg, moustache_fg)
        image[y-rows+10:y+10, x-5:x+cols-5] = dst

    cv2.imshow('Photobooth', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    time.sleep(0.1)

    
        
