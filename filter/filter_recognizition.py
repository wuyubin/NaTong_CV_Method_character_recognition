import cv2
import matplotlib.pyplot as plt
import numpy as np

def salt(img, n):
    for k in range(n):
        i = int(np.random.random() * img.shape[1]);
        j = int(np.random.random() * img.shape[0]);
        if img.ndim == 2:
            img[j,i] = 255
        elif img.ndim == 3:
            img[j,i,0]= 255
            img[j,i,1]= 255
            img[j,i,2]= 255
    return img




img = cv2.imread(r"D:\Python_all\pythonholder\practice_project\character_recognition\test_image\test\test03\mid_grabcut_result.jpg",0)
# img = cv2.resize(img,(384,216))
#高斯滤波
lbimg=cv2.GaussianBlur(img,(3,3),1.8)
#中值滤波
img = salt(img, 500)
middle = cv2.medianBlur(img, 5)
# cv2.imwrite(r"D:\Python_all\pythonholder\practice_project\character_recognition\test_image\test\test03\ middle.jpg", middle, params=None)
img = cv2.resize(img,(680,480))
lbimg = cv2.resize(lbimg,(680,480))


middle = cv2.resize(middle,(680,480))
cv2.imshow('src',img)
cv2.imshow('dst',middle)
cv2.waitKey()
cv2.destroyAllWindows()







