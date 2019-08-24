import cv2
import numpy as np

cap=cv2.VideoCapture(1)

while True:
    ret,frame=cap.read()
    h=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    l=np.array([0,70,50])
    u=np.array([10,255,255])
    m=cv2.inRange(h,l,u)
    r=cv2.bitwise_and(frame,frame,mask=m)
    cv2.imshow('result',r)
    cv2.imshow('original',frame)
    cv2.imshow('mask',m)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()

