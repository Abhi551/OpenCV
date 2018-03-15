import cv2
import numpy as np 

var_img = cv2.imread('bookpage.jpg')

## any pixel value above 12 is converted into 255 
ret , img1 = cv2.threshold(var_img , 12 , 255 , cv2.THRESH_BINARY )

## grayscaled
grayscale = cv2.cvtColor(var_img , cv2.COLOR_BGR2GRAY)
ret , img2 = cv2.threshold( grayscale , 12 , 255 , cv2.THRESH_BINARY)
gaus =  cv2.adaptiveThreshold(grayscale , 255 ,cv2.ADAPTIVE_THRESH_GAUSSIAN_C , cv2.THRESH_BINARY , 115 , 1)
cv2.imshow('gaus',gaus)
cv2.imshow('gray' , grayscale)
cv2.imshow('threshol2' , img2)
cv2.imshow('img' , var_img)
cv2.imshow('threshold' , img1)
cv2.waitKey(0)
cv2.destroyAllWindows()