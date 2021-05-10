import cv2
import numpy as np
#import imutils

video ="resources/redv1.mp4"
cap = cv2.VideoCapture(video)

myColors = []
myColorVal = [[255,0,0]]
myPoints =[]


def getContours(img):
    contours,heirarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    x,y,w,h =0,0,0,0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area <500 :
            peri = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            x,y,w,h = cv2.boundingRect(approx)
    return x,y,w,h



def findColor (img,myColor,myColVal):
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    count =0
    newPoints=[]
    for color in myColor:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV,lower,upper)
        x,y,w,h = getContours(mask)
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),1)





while True:
    succ,img = cap.read()
    cv2.imshow("Video",img)
    findColor(img,myColors,myColorVal)

    if cv2.waitKey(100) & 0xff ==ord("q"):
        break