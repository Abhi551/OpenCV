import cv2

load_img = cv2.imread("1.jpg")
img = cv2.resize(load_img,(360,480))

cv2.imshow("new",img)
cv2.waitKey(0)