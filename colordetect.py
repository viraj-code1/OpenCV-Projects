import cv2
import numpy as np
def empty():
    pass
#color of image

cv2.namedWindow("trackbar")
cv2.resizeWindow("trackbar",640,240)
cv2.createTrackbar("Hue Min","trackbar",67,179,empty)
cv2.createTrackbar("Hue Max","trackbar",89,179,empty)
cv2.createTrackbar("Sat Min","trackbar",15,255,empty)
cv2.createTrackbar("Sat Max","trackbar",255,255,empty)
cv2.createTrackbar("Val Min","trackbar",0,255,empty)
cv2.createTrackbar("Val Max","trackbar",255,255,empty)

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10,20)

while True:
    _,img = cap.read()

    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    h_min = cv2.getTrackbarPos("Hue Min", "trackbar")
    h_max = cv2.getTrackbarPos("Hue Max", "trackbar")
    s_min = cv2.getTrackbarPos("Sat Min", "trackbar")
    s_max = cv2.getTrackbarPos("Sat Max", "trackbar")
    v_min = cv2.getTrackbarPos("Val Min", "trackbar")
    v_max = cv2.getTrackbarPos("Val Max", "trackbar")
    print(h_min, s_max)
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = cv2.inRange(imgHSV,lower,upper)
    imgres = cv2.bitwise_and(img,img,mask=mask)


    #cv2.imshow("imagehsv", imgHSV)
    cv2.imshow("image", img)
    cv2.imshow("mask", mask)
    cv2.imshow("imgres",imgres)
    cv2.waitKey(1000)
