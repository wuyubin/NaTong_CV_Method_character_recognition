import numpy as np
import cv2
from matplotlib import pyplot as plt

import base64
img = cv2.imread(r"F:\natong\natong_data_augmentation\natong_data_augment\12110126300023\00000074_00000000008C3860.bmp_0_6275.jpg",1)

mask = np.zeros(img.shape[:2],np.uint8)

bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)



# rect = (249,1049,3840-249,2160-1049)#划定区域37451673
rect = (1,1,3839,2159)#划定待分割区域37451673


# cv2.grabCut(img,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)#函数返回值为mask,bgdModel,fgdModel
cv2.grabCut(img,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_MASK)#函数返回值为mask,bgdModel,fgdModel
mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')#0和2做背景

img = img*mask2[:,:,np.newaxis]#使用蒙板来获取前景区域

# cv2.imwrite(r"D:\Python_all\pythonholder\practice_project\character_recognition\test_image\test\test02\guass_grabcut_result_huidu.jpg", img, params=None)

img = cv2.resize(img,(678,444))
cv2.imshow('p',img)
cv2.waitKey(0)