import cv2 
import numpy as  np 
import matplotlib 

## open cv has BGR instead of RGB



var_img =  cv2.imread('java_coffee2.jpg' , cv2.IMREAD_COLOR)


## make line on the image 
## cv2.line( image_refernce , (start_x , start_y) ,(end_x ,  end_y) , (color codes)  , thickness)
cv2.line(var_img , (10,150) ,(150,150) , (0,255,0) , 2)

## make rectangle on the image 
## cv2.rectangle (img_reference , (top_left_coordinate) , (bottom_right_coordinate) , (color_codes) , thickness)
## if we use -1 instead of thickness it fills the rectangle
cv2.rectangle(var_img , (150 , 100) , (300 , 400) , (255 , 255 , 0) , 3)

## cv2.circle(image_ref , (centre_coordinates) , radius , (color) , thickness)
## simlaraly if we use -1 in thickness circle is filled with the color
cv2.circle(var_img , (300 , 200) , (50) , (0 , 0 , 255) , -1)

cv2.circle(var_img  , (150 ,150) , (50) , (0 , 0 , 0) , 5)


cv2.imshow('img', var_img )
cv2.waitKey(0)
cv2.destroyAllWindows()


## create a black image

img = np.zeros((512,512,3) , np.uint8)

## making an ellipse
## cv2.ellipse( reference_image , (center) , (length_major_axis , length_minor_axis) , rotating_angle , 
##                                 start_angle , end_angle , (color) , thickness)
cv2.ellipse(img , (256,256) , (100,50) , 45, 0 , 360 , (255,255,255) , -1)


## making a ploygon
## pts is a numpy array such that it has rows of 2*1
## cv2.polylines(img , [pts] , True , (color) ,thickness)
## if we place third argument to be False then we don't get closed shape of the figure
pts=np.array([[10,5],[20,10],[59,0],[1,56]],np.int32)
pts=pts.reshape((-1,1,2))
cv2.polylines(img , [pts] , True, (255,255,255) , 5)



## putting the text inside the image
## specify the font type in font using cv2.FONT_HERSHEY_SIMPLEX
## cv.putText(reference_image , (coordinates) , font , size , (color) , thickness , lineType)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img , 'OpenCV' , (50,150) ,font , 2 ,(255 , 255 ,255) , 2 , cv2.LINE_8 )

cv2.imshow('img',img)

cv2.waitKey(0)
cv2.destroyAllWindows()

## summing up

var_img =  cv2.imread('java_coffee2.jpg' , cv2.IMREAD_GRAYSCALE)

#making a line
cv2.line(var_img , (100,100) ,(300,300) ,(255,0,0) , 3)
#making a rectangle
cv2.rectangle(var_img , (50,50) , (350,350) , (0,250,250) , 3)
#making a circle
cv2.circle(var_img ,(150,150) , 150 , (0,250,255) , 5)
#making an ellipse
cv2.ellipse(var_img ,(200,200) , (150,50) , 90 , 0 , 360 ,(255 , 0 , 0) , 4)
#making a polygon
pts = np.array([[1,25],[56,14],[78,23],[259,215],[100,156]] , np.int32) 
pts = pts.reshape(-1,1,2)
cv2.polylines(var_img , [pts] , True , (25,255,0) ,5)
#adding the text to image
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(var_img , '2ND PART' ,(250,250) ,  font , 3 , (255,251,0) , 3 ,cv2.LINE_AA)
cv2.imshow('img',var_img)
cv2.waitKey(0)
cv2.destroyAllWindows()