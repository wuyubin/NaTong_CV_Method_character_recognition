import numpy as np
import cv2
from matplotlib import pyplot as plt
from skimage import data,filters

img = cv2.imread('yuantu.png')
mask = np.zeros(img.shape[:2],np.uint8)

bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)

newmask = cv2.imread('yuantu.png',0)
thresh = filters.threshold_li(newmask)
newmask =(newmask <= thresh)*1.0     #阈值化

# cv2.imshow('aaaaaaaaa',newmask)
# cv2.waitKey(0)

# whereever it is marked white (sure foreground), change mask=1
# whereever it is marked black (sure background), change mask=0
# mask[newmask == 0] = 0
# mask[newmask == 255] = 1
mask[newmask == 0] = 1
mask[newmask == 1] = 0
mask, bgdModel, fgdModel = cv2.grabCut(img,mask,None,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_MASK)
mask = np.where((mask==2)|(mask==0),0,1).astype('uint8')
img = img*mask[:,:,np.newaxis]
plt.imshow(img),plt.colorbar(),plt.show()