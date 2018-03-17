import cv2
import numpy as  np 


## 1. accessing pixel values and modify them 

var_img = cv2.imread('messi5.jpg')

## accessing pixel value for co-ordinate location (100,100)
print (var_img[100,100])

## for particular channel in BGR , we specify the channel number

print ('blue = ' , var_img[100,100,0])
print ('green = ' , var_img[100 , 100 , 1] )
print ('red = ' , var_img[100 , 100 , 2]) 

## shape & size of image 
## we work with cv2 in numpy ,

print (var_img.shape)
print (var_img.size)
print (var_img.dtype)

## we are already aware of object detection using HSV

hsv_image =  cv2.cvtColor(var_img , cv2.COLOR_BGR2HSV)
gray_image = cv2.cvtColor(var_img , cv2.COLOR_BGR2GRAY)

cv2.imshow('hsv' , hsv_image)
cv2.imshow('gray_image' , gray_image)

#cv2.rectangle(var_img , (331 , 287) , (393 , 337) , (0 , 0 , 255) , 1 )
x=393-331
y=337-287

#var_img[0:y , 0:x] = var_img[287:337 , 331:393] 
#cv2.imshow('image' , var_img)

## 2. Splitting and Merging Image Channels 

## split BGR images to single planes 
b,g,r = cv2.split(var_img)
print (b,g,r)

## basic indexing in numpy 
print (var_img[:,:,0])

## making third index in numpy zero , i.e. red is set to be zero
## try to use numpy indexing
## this makes sure that any change in new_img doesn't effec var_img
new_img =var_img.copy()
new_img[:,:,2]=0
cv2.imshow('new_img' , new_img)

## 3. making borders for images (padding)

## its just making the borders around the image or frame but it is mostly 
## used in convolution operation and zero padding 

## cv2.copyMakeBorder(src , top , bottom , left , right , borderType , value)
## top , bottom , left , right = integer values , i.e. border width number of pixels in corresponding direction
## value is used only when borderType is cv2.BORDER_CONST

replicate = cv2.copyMakeBorder( var_img , 20 ,20 , 30 , 30 , borderType = cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(var_img , 20 , 20 , 30 ,30 , cv2.BORDER_REFLECT_101)
constant = cv2.copyMakeBorder(var_img , 20 , 20 , 30 , 30 ,cv2.BORDER_CONSTANT , value = (0,0,255))
wrap = cv2.copyMakeBorder(var_img , 20 , 20 , 30 , 30 , cv2.BORDER_WRAP)

cv2.imshow('replicate' , replicate)
cv2.imshow('wrap' , wrap)
cv2.imshow('reflect' , reflect)
cv2.imshow('constant' , constant)

cv2.waitKey(0)
cv2.destroyAllWindows()


