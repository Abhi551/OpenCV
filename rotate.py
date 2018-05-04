## rotation of image
import cv2
import numpy as np

img = cv2.imread('detect.jpg' , 0)
img = cv2.resize(img , None , fx = .7 , fy = .7)

width , height = img.shape[::-1]

## for rotating an image we use function named cv2.getRotationMatrix2D(center , angle , scale)
## center about which rotation is done 
## angle by which image is rotated
## scale 1.0 means shape of image is preserved 

center = (width/2 , height/2)
angles = [ 90 , 180 , 270 ]

for angle in angles:
	new_img = cv2.getRotationMatrix2D( center , angle , scale = 1)
	
	## getting the matrix for rotated image 
	rotated = cv2.warpAffine( img , new_img , (width , height))
	img_name = "img"+str(angle)
	cv2.imshow(img_name , rotated)


cv2.imshow("image" , img)
cv2.waitKey(0)
cv2.destroyAllWindows()

