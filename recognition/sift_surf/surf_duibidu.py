
# -*- coding: utf-8 -*-
import cv2
import numpy as np
from find_obj import filter_matches, explore_match
from matplotlib import pyplot as plt

def matchSift():
    '''''
    匹配sift特征
    '''
    img1 = cv2.imread(r"E:\lenovo_exercitation\natong_work\naton"
                      r"g_product\grabcut_folder\962215042606600003_gc_skew_mf\00000259_0000000000A7CF24.bmp",
                      0)  # queryImage
    img2 = cv2.imread(r"E:\lenovo_exercitation\natong_work\naton"
                      r"g_product\grabcut_folder\962215042606600005_gc_skew_mf\00000245_0000000000A4BA9A.bmp",
                      0)  # trainImage
    # sift = cv2.SIFT()
    # sift = cv2.xfeatures2d.SIFT_create()
    sift = cv2.xfeatures2d.SURF_create()
    kp1, des1 = sift.detectAndCompute(img1, None)
    kp2, des2 = sift.detectAndCompute(img2, None)
    # 蛮力匹配算法,有两个参数，距离度量(L2(default),L1)，是否交叉匹配(默认false)
    bf = cv2.BFMatcher()
    # 返回k个最佳匹配
    matches = bf.knnMatch(des1, des2, k=2)

    num = 0
    result = 0
    for m, n in matches:
        if m.distance < 0.75 * n.distance:
            # result += m.distance*m.distance
            result += (m.distance-n.distance)*(m.distance-n.distance)
            num += 1
    if num > 0:
        result /= num
    # return result

    print(result)
    # cv2.drawMatchesKnn expects list of lists as matches.
    # opencv2.4.13没有drawMatchesKnn函数，需要将opencv2.4.13\sources\samples\python2下的common.py和find_obj文件放入当前目录，并导入
    p1, p2, kp_pairs = filter_matches(kp1, kp2, matches)
    explore_match('find_obj', img1, img2, kp_pairs)  # cv2 shows image
    cv2.waitKey()
    cv2.destroyAllWindows()

matchSift()
# getSift()
