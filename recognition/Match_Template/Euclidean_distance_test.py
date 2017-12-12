import cv2
import numpy as np

def get_EuclideanDistance(x,y):
    myx = np.array(x)
    myy = np.array(y)
    return np.sqrt(np.sum((myy-myx)*(myy-myx)))
def findpic(img, findimg, h, fh, w, fw):
    minds = 1e8
    mincb_h = 0
    mincb_w = 0
    for now_h in range(0,h-fh):
        for now_w in range(0,w-fw):
            my_img = img[now_h:now_h+fh, now_w:now_w+fw, :]
            my_finding = findimg
            dis = get_EuclideanDistance(my_img, my_finding)
            if dis<minds:
                mincb_h = now_h
                mincb_w = now_w
                minds = dis
    findpt = mincb_w, mincb_h
    cv2.rectangle(img, findpt, (findpt[0]+fw, findpt[1]+fh), (255, 0, 0))
    return img

def showpiclocation(img,findimg):
    w = img.shape[1]
    h = img.shape[0]
    fw = findimg.shape[1]
    fh = findimg.shape[0]
    return findpic(img, findimg, h, fh, w, fw)

def addnoise(img):
    coutn = 5000
    for k in range(0, coutn):
        xi = int(np.random.uniform(0,img.shape[1]))
        xj = int(np.random.uniform(0,img.shape[0]))
        img[xj, xi, 0] = 255*np.random.rand()
        img[xj, xi, 1] = 255*np.random.rand()
        img[xj, xi, 2] = 255*np.random.rand()

if __name__ =='__main__':
    myimg = cv2.imread(r"E:\lenovo_exercitation\natong_work\natong_product\grabcut_"
                     r"folder\12110125400017_gc_skew_mf\00000029_0000000000272E70.bmp", 1)
    myfindimg = cv2.imread(r"E:\lenovo_exercitation\natong_work\natong_product\grabcut_"
                          r"folder\12110125400017_gc_skew_mf\00000031_00000000002797AD.bmp", 1)
    # myimg = cv2.imread(fn1)
    # myfindimg = cv2.imread(fn2)
    addnoise(myimg)
    myimg = showpiclocation(myimg,myfindimg)
    cv2.imshow('find img3',myimg)
    cv2.imwrite('',myimg)
    cv2.waitKey()
    cv2.destroyAllWindows()