## code for detection 
import cv2
import numpy as np 

img = cv2.imread('detect.jpg')
print (img.shape[::-1])
## resizing the image
## img =  cv2.resize(img , None , fx = .7 , fy = .7)

## template images for the given image
temp = cv2.imread('template.jpg' , 0)
## temp = cv2.resize( temp , None , fx = .7 , fy =.7)

## saving the width and height if template images
width , height = temp.shape[::-1]
## converting to Gray Scale 
img_gray = cv2.imread('detect.jpg' , 0)


## only one method for Matching the template images
## function for templating matching 

methods = ["cv2.TM_CCOEFF_NORMED"]
for method in methods:
	result = cv2.matchTemplate(img_gray , temp , eval(method) )
	img = cv2.imread('detect.jpg')
	threshold = float(raw_input("Enter the percentage for threshold for %s " %(method)))
	
	## checking the condition for template matching and locating coordinates in grayscaled image
	loc = np.where( result >= threshold)
	for point in zip(*loc[::-1]):
		## marking the matched templates 
		cv2.rectangle( img , point , (point[0]+width , point[1]+height) , (0,255,255))
	cv2.imshow('new image' , img)
cv2.imshow(' gray image ' , img_gray )
cv2.imshow(' template image ' , temp )
cv2.waitKey(0)
cv2.destroyAllWindows()

## the method is inefficeint for same rotated or scaled image 

## rotating the template image for new results

center , scale = (width/2 , height/2) , 1.0
img = cv2.imread('detect.jpg' )
img_gray = cv2.imread('detect.jpg' , 0)
new_temp = cv2.getRotationMatrix2D(center , 180 , scale = 1.0 )
rotate  =  cv2.warpAffine(temp , new_temp , (width , height))
## now match the templates in original image
result = cv2.matchTemplate(img_gray , rotate , cv2.TM_CCOEFF_NORMED)
loc = np.where(result >= threshold)
for points in zip(*loc[::-1]):
	cv2.rectangle(img , points , (points[0]+width , points[1]+height) , (0,255,255))

cv2.imshow("rotated image" , rotate)
cv2.imshow("new image " , img)
cv2.waitKey(0)
cv2.destroyAllWindows()

## using different methods for template matching in openCV
## but we wont't be able to recognize multiple object

methods =['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
         'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
img =  cv2.imread('messi5.jpg')

for method in methods :
	## preserving the original images
	img2 = img.copy()
	img2 = cv2.cvtColor(img2 , cv2.COLOR_BGR2GRAY)
	## template image
	temp = cv2.imread("messi_temp.jpg" , 0)
	## matching the template with copied image
	result =  cv2.matchTemplate(img2 , temp , eval(method))
	## taking min , max values and min max local values
	min_val , max_val , min_loc , max_loc = cv2.minMaxLoc(result)
	if method in ["cv2.TM_SQDIFF" , "cv2.TM_SQDIFF_NORMED"]:
		top_left = min_loc
	else :
		top_left = max_loc

	bottom_right = (top_left[0] + width , top_left[1] + height )
	cv2.rectangle(img, top_left , bottom_right , (0 , 255 , 255) , 2)

	cv2.imshow('image' , img)
	cv2.imshow('template' , temp)
	cv2.waitKey(0)
	cv2.destroyAllWindows()


## use of min max scaling in templating matching