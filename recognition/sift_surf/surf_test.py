# -*- coding: UTF-8 -*-
import os
import cv2
# import numpy as np
# from find_obj import filter_matches, explore_match
# from matplotlib import pyplot as plt

def matchSift(path1,path2):
    '''''
    匹配sift特征
    '''
    img1 = cv2.imread(path1,0)  # queryImage
    img2 = cv2.imread(path2,0)  # queryImage
    # sift = cv2.SIFT()
    sift = cv2.xfeatures2d.SIFT_create()
    # sift = cv2.xfeatures2d.SURF_create()
    kp1, des1 = sift.detectAndCompute(img1, None)
    kp2, des2 = sift.detectAndCompute(img2, None)
    # 蛮力匹配算法,有两个参数，距离度量(L2(default),L1)，是否交叉匹配(默认false)
    bf = cv2.BFMatcher()
    # 返回k个最佳匹配
    matches = bf.knnMatch(des1, des2, k=2)

    num = 0
    result = 0
    # for m, n in matches:
    #     if m.distance < 0.75 * n.distance:
    #         result += m.distance*m.distance
    #         num += 1
    for m, n in matches:
        result += m.distance*m.distance
        num += 1
    if num > 0:
        result /= num
    return result

min = 100000;
# 遍历指定目录，显示目录下的所有文件名
filepath = "E:\\lenovo_exercitation\\natong_work\\natong_product\\grabcut_folder"
pathDir = os.listdir(filepath)
for allDir in pathDir:
    allDir__ = '\\'+allDir
    filepath_min = os.path.join('%s%s' % (filepath, allDir__))
    # print (filepath_save)            # child.decode('gbk')  # .decode('gbk')是解决中文显示乱码问题
    pathdir_min = os.listdir(filepath_min)

    for alldir_min in pathdir_min:
        alldir_min__ = '\\' + alldir_min
        filepath_final = os.path.join('%s%s' % (filepath_min, alldir_min__))

        # print(filepath_final)
        read_path = filepath_final
        path2 = 'E:\\lenovo_exercitation\\natong_work\\natong_product\\grabcut_folder\\13033022900009_gc_skew_mf\\00000000_00000000003058E9.bmp'
        result = matchSift(read_path,path2)
        if 0 < result < min:
            min = result;
            classname = allDir+'\\'+alldir_min
            print(min)
            print(classname)
result = classname+'---'+str(min)
print(result)





