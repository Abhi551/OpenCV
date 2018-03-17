from skimage.exposure import rescale_intensity
import numpy as np 
import cv2



def convolution(image , kernel):

	var_img = cv2.imread(image , 0)

	height ,  width = var_img.shape
	k_height , k_width = kernel.shape


	pad = int(k_width/2)

	output_image = np.zeros((height,width))
	new_image = cv2.copyMakeBorder(var_img , pad , pad , pad , pad , borderType = cv2.BORDER_REPLICATE)

	for i in range(pad , height):
		for j in range(pad , width):
			out = (new_image[i-pad:i+pad+1,j-pad:j+pad+1]*kernel).sum()
			output_image[i,j] = out

	output_image = rescale_intensity(output_image , in_range=(0,255))

	return (output_image)






print ("different types of image filters are ")

kernel = np.ones((7,7),np.float32)/49.0

image = convolution('messi5.jpg' , kernel)
cv2.imshow('blur',image)

kernel =  np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])

image = convolution('messi5.jpg' , kernel)
cv2.imshow('sharp',image)


kernel = np.array((
	[-1, 0, 1],
	[-2, 0, 2],
	[-1, 0, 1]))

image = convolution('messi5.jpg' , kernel)
cv2.imshow('sobelX',image)


kernel = np.array((
	[-1, -2, -1],
	[0, 0, 0],
	[1, 2, 1]))

image =  convolution('messi5.jpg' , kernel)
cv2.imshow('sobelY' ,  image)

kernel = np.array((
	[0, 1, 0],
	[1, -4, 1],
	[0, 1, 0]), dtype="int")

image = convolution('messi5.jpg' , kernel)
cv2.imshow('laplacian' , image)


cv2.waitKey(0)
cv2.destroyAllWindows()