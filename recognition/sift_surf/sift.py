import cv2
import numpy as np

# import pdb
# pdb.set_trace()#turn on the pdb prompt

# read image
img = cv2.imread(r"E:\lenovo_exercitation\natong_work\natong_product\natong_product_picture_grabcut\962215080911800020_gc\00000265_0000000000A90AFB.bmp",1)

# img = cv2.imread('D:\privacy\picture\little girl.jpg', cv2.IMREAD_COLOR)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('origin', img)

# SIFT
detector = cv2.xfeatures2d.SIFT_create()
keypoints = detector.detect(gray, None)
img = cv2.drawKeypoints(gray, keypoints, 0)
# img = cv2.drawKeypoints(gray,keypoints,0,flags = cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow('test', img);
cv2.waitKey(0)
cv2.destroyAllWindows()  