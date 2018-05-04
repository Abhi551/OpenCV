import cv2
import numpy as np
import sys
for i in range(2):
    try :
        img = "img"
        var_img = cv2.imread("IMG_3082_cropped.png")
        #var_img = cv2.imread("IMG_3060.JPG")


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

        
        start , end  = 0 , 0
        
        ## starting for front to encounter the first occurance of 255 in threshold image
        for i in range(width) :
                if 255 in threshold_img[i] :
                    if 255 in threshold_img[i+10]:
                        start = i
                    else:
                        pass
                    break
        print (start)
        
        ## starting from back to encounter the first occurance of 255 in threshold image
        for j in range(width-1 , 0 , -1):
            if 255 in threshold_img[j]:
                    if 255 in threshold_img[i+10]:
                        end = j
                        print ("j is ",j)
                    else :
                        pass
                    break
        print(end)
    

        ## getting the final Region Of Image 

        ROI = dilation[start : end , 0 : height]
        cv2.imshow(str(img)+"_ROI.JPG" , ROI)

        print (str(img))
        '''
        if "png" in str(img):
            cv2.imwrite(str(img)+"_save.png" , ROI)
        else :
            cv2.imwrite(str(img)+"_save.JPG" , ROI)
        '''
        
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
    except Exception as e:
        print (e)

