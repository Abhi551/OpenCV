import cv2
import numpy as np 
import matplotlib

## for interacting with webcam
## all the video making and destroying takes place through cv2
## customizations are usually done using cap defined as 
## cap =  cv2.VideoCapture()
'''
cap = cv2.VideoCapture(0)

while True:
    
    ret , frame = cap.read()

    ##once we start the web cam all editing is done through frames

    gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)

    cv2.imshow('GRAY' , gray)
    cv2.imshow('VIDEO',frame)

    if cv2.waitKey(1) & 0xFF==ord('q') :
        break;


cap.release()
cv2.destroyAllWindows()
'''

 ## saving the file 


capture = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('Output.avi', fourcc , 20 , (640 , 480))

while True :
    ret , frame = capture.read()
    gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)

    cv2.imshow('1',gray)
    cv2.imshow('2',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
out.release()
cv2.destroyAllWindows()

    

