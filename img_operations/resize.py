import cv2 
import numpy as np


var_img = cv2.imread('messi_face.jpg')
## cv2.resize( source , size , fx , fy , interpolation )

## to shrink we use cv2.INTER_AREA
## to magnify the image we use cv2.INTER_LINEAR or cv2.INTER_CUBIC
small_img = cv2.resize(var_img , None , fx =2 , fy=2  , interpolation = cv2.INTER_CUBIC)

cv2.imshow('var_img' , var_img)
cv2.imshow('small_img' , small_img)

cv2.waitKey(0)

cv2.destroyAllWindows()
