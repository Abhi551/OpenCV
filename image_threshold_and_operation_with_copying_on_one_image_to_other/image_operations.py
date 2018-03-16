import numpy as  np 
import cv2

## some operations in the images 
'very important for extracting a part from image'

## Bitwise operations include AND , OR , NOT and XOR operations . They will be highly useful while extracting
## a ROI , especiall when our ROI is non rectangular in shape 

img1 = cv2.imread('3D-Matplotlib.png' , cv2.IMREAD_COLOR)
img2 = cv2.imread('mainlogo.png' , cv2.IMREAD_COLOR)
img3 = cv2.imread('3D-Matplotlib.png' ,cv2.IMREAD_COLOR)

## cv2 uses numpy for image operations and manipulations , so we can also use
## numpy.shape(img2) both will give the same result for img2
## Now when we are dealing with the BGR images we have height , width , channels = img2.shape 
## and in case of for binary images img2.shape only have 2 dimensions height , width
print (np.shape(img2))

#ROI is found out using the img2.shape
rows , cols , channels = img2.shape

ROI = img1[0:rows , 0:cols]

## creating  a mask of logo and create its inverse mask
## by converting them into grayscale image
## by this we have only one pixel value insteqad of BGR values
## which helps in better manipulation of image
grayscale = cv2.cvtColor(img2 , cv2.COLOR_BGR2GRAY)

## using threshold(ref_image ,  threshvalue , qqconvert_to_value )

## converting all those which are greater than 220  to zero 
## and rest to 255
ret , mask = cv2.threshold(grayscale , 220 , 255 , cv2.THRESH_BINARY_INV)

##ret1 , mask1 = cv2.threshold(grayscale , 220 , 255 , cv2.THRESH_BINARY)
## mask_inv gives the same value as the mask1

mask_inv = cv2.bitwise_not(mask)

cv2.imshow('mask' , mask)

## we pasted mask_inv in ROI , where mask_inv is the inverted grayscale area from threshold
## here image with white background is used to retain the ROI

img1_bg = cv2.bitwise_and(ROI , ROI , mask = mask_inv)

cv2.imshow('img1_bg' , img1_bg)

## we pasted mask onto the mainlogo image 
## here image with black background and white logo is used to retain the logo
img1_fg = cv2.bitwise_and(img2 , img2 , mask = mask)

## finally combinning the 2 images to give our ROI with our desired image
## adding the img1_fg and img1_bg which gives the our desired image of logo in ROI


dst = cv2.add(img1_fg , img1_bg)

cv2.imshow('dst' , dst)
img1[0:rows , 0:cols]= dst
cv2.imshow('jdf' , img1)

cv2.waitKey(0)
cv2.destroyAllWindows()


