import matplotlib.pyplot as plt 
import numpy as np 
import cv2


## using the opencv library
var_img = cv2.imread('watch.jpg',cv2.IMREAD_COLOR)
cv2.imshow('my.jpg' , var_img)

key =  cv2.waitKey(0)

if key == 27 : ### for ESC
	cv2.destroyAllWindows()
elif  key == ord('s'):
	cv2.imwrite('img.jpg',var_img)
	cv2.destroyAllWindows()


## using the matplotlib 
var_img = cv2.imread('watch.jpg',cv2.IMREAD_GRAYSCALE)
plt.imshow(var_img,cmap='gray')
## removing the scale of graphs on plot
plt.xticks([])
plt.yticks([])
plt.show()


