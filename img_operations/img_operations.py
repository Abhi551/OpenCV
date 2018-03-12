## Some basic points about the frames and images
## every video is made up of from the collections of frames
## Each frame is made up of pixels stored in rows and columns within frame and picture
## each pixel have a coordinate location and is coprised   

import matplotlib
import numpy as np 
import cv2 
 
var_img = cv2.imread('watch.jpg' , cv2.IMREAD_COLOR)

## creating a rectangle in the image
cv2.rectangle( var_img , (91,32) , (208,110) ,(255,255,255) ,3 )
## color or pixel values at the coordinates [50,50]
print (var_img[50,50])

## ROI  this specifies the region of image in figure

watch = var_img[32:110 ,91:208]

## copying the image to new loaction in original image 
## but it is very important to the length of coordinates should be same
var_img[0:78,0:117] =watch

cv2.imshow('watch',watch)
cv2.imshow('img' , var_img)

cv2.waitKey(0)
cv2.destroyAllWindows()