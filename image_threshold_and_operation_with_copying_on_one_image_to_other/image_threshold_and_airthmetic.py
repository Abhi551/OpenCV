## threshold function is used usually on grayscale images , if the value of pixel is greater than given 
## threshold values than it is other converted into white or black pixel depending on the function passed

## cv.threshold( grayscale_image , pixel , MaxVal , func)

## function takes the values  as
#  1. cv2.THRESH_BINARY
#  2. cv2.THRESH_BINARY_INV
#  3. cv2.THRESH_TRUNC
#  4. cv2.THRESH_TOZERO
#  5. cv2.THRESH_TOZERO_INV

import cv2
import numpy as np 

var_img = cv2.imread('mainlogo.png' , cv2.IMREAD_COLOR)
grayscale = cv2.cvtColor( var_img , cv2.COLOR_BGR2GRAY)

## converting the grayscale using different threshold functions

ret1 , thresh1 = cv2.threshold(grayscale , 235 , 255 , cv2.THRESH_BINARY )
ret2 , thresh2 = cv2.threshold(grayscale , 231 , 255 , cv2.THRESH_BINARY_INV )
ret3 , thresh3 = cv2.threshold(grayscale , 231 , 255 , cv2.THRESH_TRUNC)
ret4 , thresh4 = cv2.threshold(grayscale , 231 , 255 , cv2.THRESH_TOZERO)
ret5 , thresh5 = cv2.threshold(grayscale , 231 , 255 , cv2.THRESH_TOZERO_INV)
cv2.imshow('img' , grayscale)
cv2.imshow('img1' , thresh1 )
cv2.imshow('img2' , thresh2 )
cv2.imshow('img3' , thresh3 )
cv2.imshow('img4' , thresh4 )
cv2.imshow('img5' , thresh5 )
cv2.waitKey(0)
cv2.destroyAllWindows()

## Airthmetic Operations on images
## we can apply many Operations on images such as addition , subtraction , weighted addition and 
## bitwise operations ,etc

import cv2
import numpy as np 

var_img1 = cv2.imread('3D-Matplotlib.png' , cv2.IMREAD_COLOR)
var_img2 = cv2.imread( 'mainsvmimage.png' , cv2.IMREAD_COLOR)


##
'important'
## addition using openCV and numpy are totally different 
## in OpenCV we have 
##					>> 250+10 = 260 anything above 255 is converted to 255

## in numpy we have 
##				    >> 250+10 = 260 which becomes as 4 =260%256

## as in example

add_img = var_img1 + var_img2

## simlarly we can show for cv2.add()

add_img1 = cv2.add(var_img1 , var_img2)


## now when we cheack the result pixel wise we get the value correct
print ('var_img1',var_img1[200 , 200])
print ('var_img1',var_img2[200 , 200])
print ('add_img',add_img[200 , 200])
print ('add_img',add_img1[200, 200])

##
'image blending'
## using the weighted mean for calculation
## images are added using the following equation

## g(x) =a*f_1(x)+(1-a)*f_2(x)
## where a belongs to [0,1]

## cv2.addWeighted(img1 , a , img2 ,1-a ,gamma )
## gamma is the measurement of light
add_img3 = cv2.addWeighted(var_img1 , 0.3 , var_img2 , .7 , 0)

cv2.imshow('weight' , add_img3)
cv2.imshow('image' ,add_img)
cv2.imshow('add_img' ,add_img1)
cv2.waitKey(0)
cv2.destroyAllWindows()

