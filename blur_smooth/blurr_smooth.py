## for more ref
## https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_filtering/py_filtering.html#filtering
## while object detecting many times we need to remove the blurs for better detections
## for blurs and smoothing we use LPF , LOW PASS FILTER

import cv2 
import numpy  as np 

## applying custom made filters to images
## blur the images with various low pass filters

## we use cv2.filter2D() to convolve a kernel with an image
## where a kernel , is a small matrix
## at every point or pixel in kernel there will be a different value of color so we take there average and replace the center 
## pixel with average

## this gives 2D convulation of image 
var_img = cv2.imread('images.jpg' , 1)
kernel1 = np.ones((3,3) , np.float32)/9
kernel2 = np.ones((4,4) , np.float32)/25
dst1 = cv2.filter2D(var_img , -1 , kernel1)
dst2 = cv2.filter2D(var_img , -1 , kernel2)

cv2.imshow('kernel1' ,  dst2)
cv2.imshow('kernel2' , dst1)
cv2.imshow('img' , var_img)



cv2.waitKey(0)
cv2.destroyAllWindows()


## for image smoothening  , it can be achived by convolving the image with a low pass filter kernel
## it is used to remove high frequency content from images as edges and noises
## there are mainly 4 types of blur techniques in OpenCV

import cv2 
import numpy as np 

var_img = cv2.imread('images.jpg' , 1)
noise_img =  cv2.imread('noise.png' , 1)
noise_img2 = cv2.imread('noise2.png' ,1)
## in general in any blur technique , the parameters are (img_reference , kernel_size)
blur_img1 = cv2.blur(var_img , (5,5))
blur_img2 = cv2.blur(noise_img , (5,5))
blur_img3 = cv2.blur(noise_img2 , (5,5))

cv2.imshow('image1' , var_img)
cv2.imshow('image2' , noise_img)
cv2.imshow('image3' , noise_img2)

cv2.imshow('blur1' , blur_img1)
cv2.imshow('blur2' , blur_img2)
cv2.imshow('blur3' , blur_img3)

## 2nd is gaussian blur
## Gaussian noise is statistical noise having a probability distribution function 
## equal to normal distribution function , which is know as Gaussian distribution
## kernel_size should have only odd numbers in it
## we also define sigmaX and sigmaY , at least sigmaX has to be defined and sigmaY=sigmaX
gaussian_blur1 = cv2.GaussianBlur(var_img , (3,3) , 1)
gaussian_blur2 = cv2.GaussianBlur(noise_img , (3,3) ,1)
gaussian_blur3 = cv2.GaussianBlur(noise_img2 , (3,3) ,1)
cv2.imshow('gaussian_blur1' , gaussian_blur1)
cv2.imshow('gaussian_blur2' , gaussian_blur2)
cv2.imshow('gaussian_blur3' , gaussian_blur3)


## 3rd is median blur
## medianBlur(image , ksize)
## ksize is odd number only
## really useful and strong in case of salt and peper noise

median_blur1 = cv2.medianBlur(noise_img , 5 )
#median_blur2 = cv2.medianBlur(noise_img , 5 )
#median_blur3 = cv2.medianBlur(noise_img , 7 )
median_blur2 = cv2.medianBlur(noise_img2 , 3)


cv2.imshow('median1' , median_blur1)
cv2.imshow('median2' , median_blur2)

## dont really get that filter 
## 4th is bilateral blur
## cv2.bilateralFilter() is highly  effective in noise removal while maintaing edges
## but operation is slower than other filters

bi_blur1 = cv2.bilateralFilter(noise_img , 9 ,75 ,75)
bi_blur2 = cv2.bilateralFilter(noise_img2 , 9 ,75 , 75)

cv2.imshow('bilateral2' , bi_blur2)
cv2.imshow('bilateral1',bi_blur1)

cv2.waitKey(0)
cv2.destroyAllWindows()


import cv2 
import numpy as np 

cap = cv2.VideoCapture(0)

while 1:

    ret , frame = cap.read()
    ## convert fram to hsv for object detection
    hsv = cv2.cvtColor(frame , cv2.COLOR_BGR2HSV)
    #cv2.imshow('hsv' , hsv)

    lower_range = np.array([110 , 115  , 40])
    upper_range = np.array([130 , 190 ,  85])
    '''
    lower_range = np.array([90 , 230  , 250])
    upper_range = np.array([110 , 255 , 255])
    '''

    mask = cv2.inRange(hsv ,  lower_range , upper_range)

    result = cv2.bitwise_and(frame , frame , mask=mask)

    ## make the kernel
    kernel = np.ones((10,10) , np.float32)/100

    ## smothed 
    smoothed = cv2.filter2D(result , -1 , kernel )

    ## applying blur to video

    blur = cv2.blur(result , (5,5))

    ## apply gaussian blur in the video 

    gaussian_blur = cv2.GaussianBlur(result , (15,15) , 1)
    median_blur = cv2.medianBlur(result , 15)
    cv2.imshow('gaussian' , gaussian_blur)
    cv2.imshow('blur' , blur)
    cv2.imshow('result' , result)
    cv2.imshow('smoothed' , smoothed)    
    cv2.imshow('median' , median_blur)
    ## not able to do bilateral blur
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()