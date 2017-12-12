import cv2
import numpy as np

def get_EuclideanDistance(x,y):
    myx = np.array(x)
    myy = np.array(y)
    return np.sqrt(np.sum((myy-myx)*(myy-myx)))

#00000031_00000000002797AD
if __name__ =='__main__':
    myimg = cv2.imread(r"E:\lenovo_exercitation\natong_work\natong_product\grabcut_"
                     r"folder\12110125400017_gc_skew_mf\00000029_0000000000272E70.bmp", 0)
    myfindimg = cv2.imread(r"E:\lenovo_exercitation\natong_work\natong_product\grabcut_"
                          r"folder\14011112190280_gc_skew_mf\00000191_000000000039D03A.bmp", 0)
    dis = get_EuclideanDistance(myimg, myfindimg)
    print(dis)