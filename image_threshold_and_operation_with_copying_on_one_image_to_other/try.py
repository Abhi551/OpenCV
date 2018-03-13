import cv2 
import numpy 

img1 = cv2.imread('mainlogo.png' , cv2.IMREAD_COLOR)
img2 = cv2.imread('3D-Matplotlib.png' , cv2.IMREAD_COLOR)

rows , cols , channel = img1.shape

ROI = img2[0:rows , 0:cols]

grayscale = cv2.cvtColor(img1 , cv2.COLOR_BGR2GRAY)

ret ,  mask = cv2.threshold( grayscale , 220 , 255 , cv2.THRESH_BINARY_INV)
mask_inv = cv2.bitwise_not(mask)


## now we have obtained 2 images of mainlogo using gray


## to retain the image

fg = cv2.bitwise_and(img1 , img1 , mask = mask)

## to retain the ROI

bg = cv2.bitwise_and(ROI , ROI , mask =  mask_inv)
res = cv2.add(fg , bg)
'''
cv2.imshow('2',bg)
cv2.imshow('3',fg)'''
cv2.imshow('1',res)
img2[0:rows , 0:cols] = res
cv2.imshow('img' , img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
 