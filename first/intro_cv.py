import cv2
import numpy as np 
import matplotlib.pyplot as plt 

## cv2 uses BGR and aplha format , where alpha is opaqueness
## matplotlib uses coventional RGB format for image


## other options are IMREAD_COLOR , also can be seen as  1
## other options are IMREAS_UNCHANGED , also can be seen as -1
## IMREAD_GREYSCALE as 0

## using cv2 to read and show image 

img=cv2.imread('watch.jpg',cv2.IMREAD_GRAYSCALE)
cv2.imshow('my',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

img=cv2.imread('watch.jpg',cv2.IMREAD_COLOR)
cv2.imshow('my',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


im_var=cv2.imread('watch.jpg',cv2.IMREAD_UNCHANGED)
cv2.imshow('new',im_var)
cv2.waitKey(0)
cv2.destroyAllWindows()


## using matplotlib to show the image

img = cv2.imread('watch.jpg',cv2.IMREAD_GRAYSCALE)
plt.imshow(img,cmap='gray',interpolation='bicubic')

## to remove the x axis and y axis 
plt.xticks([])
plt.yticks([])

## plotting can also be done on the image by usual parameters
plt.show()


## saving the image

var_img =  cv2.imread('watch.jpg',cv2.IMREAD_COLOR)
cv2.imshow('my.jpg' , var_img)
cv2.waitKey(0)
cv2.imwrite('first.jpg',var_img)
cv2.destroyAllWindows()