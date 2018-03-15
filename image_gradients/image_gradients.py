## high pass filter , in contrast to LPF , sharpens the image .

## sobel and scharr are used to for image detection

## for sobel read 
## https://docs.opencv.org/2.4/modules/imgproc/doc/filtering.html?highlight=sobel#sobel
## SOBEL , sobel operators combine Gaussian smoothing and differentiation , so the result
## is more or less resitant to the noise .
## Most often the functioni is called with 
## for x-image derivative = (xorder = 1 , yorder = 0 , ksize = 3) or 
## for y-image derivative = (xorder = 0 , yorder = 1 , ksize = 3)

## there is special case when ksize = CV_SCHARR(-1) , that corresponds to 3*3 scharr filter , 
## which gives better result than 3*3 sobel

## sobel(src , dst , xorder , yorder , apertureSize = 3)
## or 
## sobel(src , ddepth , dx , dy , ksize , scale , delta , borderType)

## ksize = 1,3,5 or 7 
## ddepth = output image depth


import cv2 
import numpy as np 

var_img = cv2.imread('sudoku.jpg' , 1)
gray = cv2.cvtColor(var_img , cv2.COLOR_BGR2GRAY)

cv2.imshow('image' , var_img)
cv2.imshow('gray' , gray)

## ddepth have datatype in it and take values such as :
## cv2.CV_8U
## cv2.CV_16U
## cv2.CV_32F
## cv2.CV_64F

sobelx = cv2.Sobel(gray , ddepth = cv2.CV_64F, dx = 1 , dy = 0 , ksize = 3)

sobely = cv2.Sobel(gray , ddepth = cv2.CV_64F , dx = 0 , dy =1 , ksize = 3)
## use ksize = -1 , to use cv2.CV_SCHARR(-1) , as explained above

cv2.imshow('sobely' , sobely)
cv2.imshow('sobelx' , sobelx)

## simlarly use scharr 
## cv2.Scharr have same argument as cv2.Sobel
scharrx = cv2.Scharr(gray , ddepth = cv2.CV_64F , dx =1 , dy =0 )
scharry = cv2.Scharr(gray , ddepth = cv2.CV_64F , dx =0 , dy =1)

cv2.imshow('scharrx' , scharrx)
cv2.imshow('scharry' , scharry)


## using laplacian filter , it is better to use laplacian filter
## laplacian (src , dst , ddepth , ksize  , scale )
## ksize must be odd number
## use higher data type to detect more number of edges
laplacian = cv2.Laplacian(gray , cv2.CV_64F , ksize = 5 )
cv2.imshow('laplacian' , laplacian)
    
l_img = cv2.imread('l.png' , cv2.IMREAD_COLOR)

out1 = cv2.Sobel(l_img , cv2.CV_8U , 1  , 0 , ksize = 5)
out2 = cv2.Sobel(l_img , cv2.CV_64F , 1 , 0 , ksize = 5)
absolute = np.absolute(out2)
absolute_8u = np.uint8(absolute)

cv2.imshow('out1' , out1)
cv2.imshow('out2' ,absolute_8u)
cv2.waitKey(0)
cv2.destroyAllWindows()

## Laplacian Operator or filters are used to find areas with rapid 
## change  in images i.e. edges 
## it is common and preferred to use Gaussian filter before using laplacian filter , 
## since derivative filter are very sensitive to noises 


cap = cv2.VideoCapture(0)
while 1:
    ret , frame = cap.read()
    sobelx =  cv2.Sobel(frame , cv2.CV_64F , dx = 1 , dy = 0 , ksize = 3)
    sobely =  cv2.Sobel(frame , cv2.CV_64F , dx = 0 , dy = 1 , ksize =3)
    laplacian = cv2.Laplacian(frame , cv2.CV_64F , ksize = 3)
    lap1 = cv2.Laplacian(frame , cv2.CV_64F , ksize = 5)
    k = cv2.waitKey(1) & 0xFF
    cv2.imshow('frame' , frame)
    cv2.imshow('laplacain' , laplacian)
    cv2.imshow('lap2' , lap1)
    cv2.imshow("sobelx" , sobelx)
    cv2.imshow("sobely" , sobely)
    if  k == 27:
        break
cap.release()
cv2.destroyAllWindows()