## apart from few functions of thresholding we also have other types of thresholding such as 
## 1. Adaptive Thresholding 
## 2. Otsu's Binarization


## adaptive thresholding 
## previously we used a global valiue as the threshold value for the threshold but in adaptive , a different algorithm  is used
## as the global doesn't work for the image with different lightining condition in  diferenr areas 
## In , Adaptive we use different thresholds for different regions for same image which gives better results for image with
## different lighting condition

## cv2.adaptiveThreshold(src , maxValue , adaptiveMethod , thresholdtype , blocksize  , C)

## adaptiveMethod 
##      1. cv2.ADAPTIVE_THRESH_MEAN_C() = threshold value is the mean of neighbourhood
##      2. cv2.ADAPTIVE_THRESH_GAUSSIAN_C() = threshold value is the weighted sum of neighbourhood values , where weighted sum
##                                            are a gaussian window

## block size = size of neighbourhood

## C = a constant which is subtracted from the mean or weighted mean calculated

import cv2 
import numpy as np 

var_img = cv2.imread('exp.jpg' , 0)

## gloabal thresholding
ret , img1 = cv2.threshold(var_img , 12 , 255 , cv2.THRESH_BINARY)

cv2.imshow('original',var_img)

## adaptiveThresholding
##img2 = cv2.adaptiveThreshold(var_img , 255 , cv2.ADAPTIVE_THRESH_MEAN_C , cv2.THRESH_BINARY , 115 , 2)
##th2 = cv2.adaptiveThreshold(var_img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
##           cv2.THRESH_BINARY,11,2)

th_mean = cv2.adaptiveThreshold(var_img , 255 , cv2.ADAPTIVE_THRESH_MEAN_C , cv2.THRESH_BINARY , 11 ,2)
th_mean1 = cv2.adaptiveThreshold(var_img,255,cv2.ADAPTIVE_THRESH_MEAN_C , cv2.THRESH_BINARY, 25 , 3)
gauss_mean = cv2.adaptiveThreshold(var_img , 255 ,cv2.ADAPTIVE_THRESH_GAUSSIAN_C , cv2.THRESH_BINARY , 11 , 2 )
gauss_mean1 = cv2.adaptiveThreshold(var_img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 25, 3)


cv2.imshow('new' , img1)
cv2.imshow('gauss' , gauss_mean)
cv2.imshow('mean' , th_mean)
cv2.imshow('mean1' , th_mean1)
cv2.imshow('gauss1' , gauss_mean1)
cv2.waitKey(0)
cv2.destroyAllWindows()