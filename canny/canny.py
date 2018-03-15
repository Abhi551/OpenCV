## canny edge detector 
## it is used to find edges



## canny algorithm includes 4 stage algorithm 

## 1. Noise Reduction 
## this step includes to remove the noises and blurs to make the image smooth 
## using 5*5 kernel of Gaussian Filter

## 2. Finding the intensity Gradient of image 
## we filter the image by using sobel filter in both x (G_x) , y (G_y) direction
## thus we calculate Gradient Intensity = ((G_x*G_x)+(G_y*G_y))**.5
## gradient direction   =  tan^-1(G_y/G_x)

## 3. Non Maximum Suspension 
## all those pixels which aren't local max are supressed , i.e. put to zero 
## from tan^-1(G_y/G_x) we calculate the direction of gradient and we try to find the 
## local maxima in the direction of gradient , if local maxima is found then , it is 
## considered for another level , otherwise put to  0

## 4. Hystersis Thresholding 
## this is final stage and it decides that whether or not edges are really edges or not 
## we provide to threshold values , one is MaxThresh and other is MinThresh
## any edge with Gradient intensity greater than MaxThresh is "sure edge " while lower than Gradient intensity is 
## not if any edge lies between the two , then we decide it by seeing its intensity , if edge is connected to  
## "sure  edge " else it is not edge 

## cv2.Canny(image , output , threshold1 , threshold2 , aperturesize , L2gradient )

import cv2 
import numpy  as np 

var_img  = cv2.imread('messi5.jpg' , cv2.IMREAD_COLOR)
gray  = cv2.imread('messi5.jpg' , 0)
edge = cv2.Canny(var_img , 100 ,200)
gray_edge = cv2.Canny(gray , 100 ,200)

cv2.imshow("image" ,  var_img)
cv2.imshow('gray' , gray)
cv2.imshow("canny" , edge)
cv2.imshow('gray_canny' , gray_edge)

cv2.waitKey(0)
cv2.destroyAllWindows()


cap = cv2.VideoCapture(0)

while 1:

    ret , frame = cap.read()

    canny = cv2.Canny(frame , 100 ,100)

    kernel = np.ones((5,5) , np.float32)
    
    cv2.imshow('frame' , frame)
    cv2.imshow('canny' , canny)
    


    k =  cv2.waitKey(7) & 0xFF
    if k == 27:
        break 

cap.release()
cv2.destroyAllWindows()
