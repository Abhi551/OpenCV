import cv2
import numpy as np 

## there are probably 150 color-space conversion  But most widely used are 
## 1. BGR to gray
## 2. BGR to HSV

 ## In HSV , we have Hue Saturation Value , where each value has a defined range
 ## Hue range is [0,179]
 ## Saturation range is [0,255]
 ## Value is [0,255]
var_img = cv2.imread('images.jpg' , cv2.IMREAD_COLOR )
gray_img = cv2.cvtColor(var_img , cv2.COLOR_BGR2GRAY)
hsv_img = cv2.cvtColor(var_img , cv2.COLOR_BGR2HSV)

cv2.imshow('gray' , gray_img)
cv2.imshow('hsv' , hsv_img)

## to save the images 

cv2.imwrite('hsv_save.jpg' , hsv_img)
cv2.imwrite('gray_save.jpg' ,gray_img)

k = cv2.waitKey(1) & 0xFF
if k == 27:
    cv2.destroyAllWindows() 

## object tracking 

## 1. take each frame of the video 
## 2. convert each fram BGR to HSV form
## 3. threshold the HSV image for a range of color , say blue ,of the object that needs to tracked
## 4. Now extract the blue  from the frame 

## intiallizing the webcam
cap = cv2.VideoCapture(0)
'''
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out1 = cv2.VideoWriter('output.avi' , fourcc , 20.0 , (640 , 480))
out2 = cv2.VideoWriter('output_res.avi' , fourcc , 20.0 , (640 , 480))

'''

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out1 = cv2.VideoWriter('output_hsv.avi' , fourcc , 20.0 , (640 , 480) )
out2 = cv2.VideoWriter('output_vid.avi' , fourcc , 20.0 , (640 , 480) )
while 1 :

    ## capturing all the frames
    ret , frame = cap.read()

    ## convert all the frames into HSV format
    hsv = cv2.cvtColor(frame , cv2.COLOR_BGR2HSV)

    ## defining the range of color we want to extract
    lower = np.array([90,35,120])
    upper = np.array([110,60,145])  

    ## thresholding the HSV images to get only green color

    mask = cv2.inRange(hsv , lower , upper)

    ## now using threshold image to extract the green color

    res = cv2.bitwise_and(frame , frame , mask = mask)

    ## saving the videos
    
    #out2.write(frame)
    #out1.write(res)
    cv2.imshow('result' ,res)
    cv2.imshow('hsv' , hsv)
    cv2.imshow('mask' , mask)
    cv2.imshow('frame' , frame)
    k = cv2.waitKey(1) & 0xFF
    if k ==  27:
        break
cap.release()
cv2.destroyAllWindows()