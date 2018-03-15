import numpy as  np 
import cv2

## if not using webcam 
## use img whenever frame is used 
## not use while loop

cap = cv2.VideoCapture(0)

while True :
    ret , frame = cap.read()
    hsv = cv2.cvtColor(frame , cv2.COLOR_BGR2HSV)
    
    lower_red = np.array([150,150,0])
    upper_red = np.array([185,255,255])

    mask = cv2.inRange(hsv , lower_red , upper_red)
    res =cv2.bitwise_and(frame , frame , mask = mask)
    cv2.imshow('frame' , frame)
    cv2.imshow('mask' , mask)
    cv2.imshow('res' , res)
    k = cv2.waitKey(5) & 0xFF
    if k==27:
        break
cv2.destroyAllWindows()
cap.release()
