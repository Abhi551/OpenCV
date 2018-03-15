import numpy as np 
import cv2 

## 0 for basic web cam
## to capture a video we create VideoCapture object , its argument can either be index or  name of the video file

cap =cv2.VideoCapture(0)

while 1 : 

    # cap.read() returns the Boolean value , if frame is read correctly then  True
    # otherwise false
    ret , frame = cap.read()

    ## converting the video to grayscale

    gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)

    cv2.imshow('grayscale' , gray)
    cv2.imshow('frame' , frame)

    k =  cv2.waitKey(1) & 0xFF
    ## if ESC key is pressed webcam is stopped 
    if k==27:
        break

# its very important to release the capture
cap.release()
cv2.destroyAllWindows()


## capturing the video file that has already been the device 

#cap
video_file =  input("Enter the name of the file that you want to read")

try :
    cap =cv2.VideoCapture(video_file)
except Exception as e:
    print (e)

while 1 :

    ret , frame = cap.read()

    grayscale =  cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)

    cv2.imshow('grayscale' , grayscale)
    cv2.imshow('img' , frame)

    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()



## saving the image 
## just use cv2.imwrite('filename' ,  file)

img = cv2.imread('images.jpg' ,  cv2.IMREAD_COLOR)

grayscale =  cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)

cv2.imshow('img1' ,  img)
cv2.imshow('img2' , grayscale)

## this saves the grayscale image as new_img.jpg

cv2.imwrite('new_img.jpg' ,grayscale)

## this is used for ESC to be used as command

k = cv2.waitKey(0) & 0xFF == 27
cv2.destroyAllWindows()


## saving the video 
## fourcc is defined as four character code used to identify the type of data format 
cap = cv2.VideoCapture(0)

## define the fourcc codec and a cv2.VideoWriter object 
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi' ,  fourcc , 20 , (640 , 480) )
while 1:

    ret , frame = cap.read()

    ## now change the video captured to grayscale 
    grayscale = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
    ## now change the video captured to HSV
    hsv = cv2.cvtColor(frame ,  cv2.COLOR_BGR2HSV)

    ## show the new type of videos
    cv2.imshow('grayscale' , grayscale)
    cv2.imshow('hsv' , hsv)

    out.write(frame)

    ## saving the videos
    k = cv2.waitKey(1) & 0xFF

    if k==27:
        break;

cap.release()
out.release()
cv2.destroyAllWindows()