import glob 
import cv2
import numpy as np
import sys

filename = input("Enter the file name in which images are present = ")

for img in glob.glob(filename+'/*.JPG'):
    try :
        var_img = cv2.imread(img)

        ## as size of image is too large for visualization , so reducing its size
        small_img = cv2.resize(var_img , None , fx = .25 , fy = .25 , interpolation = cv2.INTER_AREA )
        #cv2.imshow(str(img) , small_img)


        ## changing the image to grayscale image for threshold operation
        grayscale_img = cv2.cvtColor(small_img , cv2.COLOR_BGR2GRAY)
        cv2.imshow(str(img)+'_gray' , grayscale_img)


        ## using threshold to differ between the bacterial strip and and the background        
        retval , threshold_img = cv2.threshold(grayscale_img , 120 , 255 , cv2.THRESH_BINARY)
        cv2.imshow(str(img)+'_threshold' , threshold_img)


        ## changing all the in small_img area to black where threshold_img is black
        small_img[ threshold_img == 0] = 0

        cv2.imshow(str(img)+'_result' , small_img)

        ## using morphological operations 
        ## for removal of noise in image by performing erosion followed by dilation , using "opening" in cv2  

        kernel = np.ones((3,3) ,  np.float32)
        dilation = cv2.morphologyEx(small_img , cv2.MORPH_OPEN , kernel)

    

        ## cropping the resultant image

        ## getting the width and shape of image 

        width , height  = threshold_img.shape 


        ## starting for front to encounter the first occurance of 255 in threshold image
        for i in range(width) :
                if 255 in threshold_img[i]:
                    start = i
                    break
        
        ## starting from back to encounter the first occurance of 255 in threshold image
        for j in range(width-1 , 0 , -1):
            if 255 in threshold_img[j]:
                end = j
                break


        ## getting the final Region Of Image 

        ROI = dilation[start : end , 0 : height]
        cv2.imshow(str(img)+"_ROI" , ROI)
        
        print (str(img))

        ## saving the final Region Of Image
        #cv2.imwrite('save_'+str(img) , ROI)


        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
    except Exception as e:
        print (e)

