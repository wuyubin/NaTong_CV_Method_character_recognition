# -*- coding: utf-8 -*-
import cv2
import numpy as np
from find_obj import filter_matches, explore_match
from matplotlib import pyplot as plt


def getSift():
    '''''
    得到并查看sift特征
    '''
    # 读取图像
    img = cv2.imread(
        r"E:\lenovo_exercitation\natong_work\natong_product\natong_product_picture_grabcut\962215080911800020_gc\00000265_0000000000A90AFB.bmp",
        1)
    # 转换为灰度图
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 创建sift的类
    sift = cv2.xfeatures2d.SURF_create()
    # 在图像中找到关键点 也可以一步计算#kp, des = sift.detectAndCompute
    kp = sift.detect(gray, None)
    print (type(kp), type(kp[0]))
    # Keypoint数据类型分析 http://www.cnblogs.com/cj695/p/4041399.html
    print(kp[0].pt)
    # 计算每个点的sift
    des = sift.compute(gray, kp)
    print (type(kp), type(des))
    # des[0]为关键点的list，des[1]为特征向量的矩阵
    print (type(des[0]), type(des[1]))
    print (des[0], des[1])
    # 可以看出共有885个sift特征，每个特征为128维
    print (des[1].shape)
    # 在灰度图中画出这些点
    img = cv2.drawKeypoints(gray, kp, 0)
    # cv2.imwrite('sift_keypoints.jpg',img)
    plt.imshow(img), plt.show()


def matchSift():
    '''''
    匹配sift特征
    '''
    img1 = cv2.imread(r"E:\lenovo_exercitation\natong_work\naton"
                      r"g_product\grabcut_folder\853117000372320013_gc_skew_mf\00000684_000000000119C94C.bmp",0)  # queryImage
    img2 = cv2.imread(r"E:\lenovo_exercitation\natong_work\naton"
                      r"g_product\grabcut_folder\13033022900009_gc_skew_mf\00000006_0000000000322D19.bmp", 0) # trainImage
    # sift = cv2.SIFT()
    # sift = cv2.xfeatures2d.SIFT_create()
    sift = cv2.xfeatures2d.SURF_create()
    kp1, des1 = sift.detectAndCompute(img1, None)
    kp2, des2 = sift.detectAndCompute(img2, None)
    # 蛮力匹配算法,有两个参数，距离度量(L2(default),L1)，是否交叉匹配(默认false)
    bf = cv2.BFMatcher()
    # 返回k个最佳匹配
    matches = bf.knnMatch(des1, des2, k=2)
    print(matches)
    # cv2.drawMatchesKnn expects list of lists as matches.
    # opencv2.4.13没有drawMatchesKnn函数，需要将opencv2.4.13\sources\samples\python2下的common.py和find_obj文件放入当前目录，并导入
    p1, p2, kp_pairs = filter_matches(kp1, kp2, matches)
    explore_match('find_obj', img1, img2, kp_pairs)  # cv2 shows image
    cv2.waitKey()
    cv2.destroyAllWindows()


# def matchSift3():
#     '''''
#     匹配sift特征
#     '''
#     img1 = cv2.imread(r"E:\lenovo_exercitation\natong_work\natong_product\natong_product_"
#                       r"picture_grabcut\962215080911800020_gc\00000265_0000000000A90AFB.bmp", 0)  # queryImage
#     img2 = cv2.imread(r"E:\lenovo_exercitation\natong_work\natong_product\natong_product_"
#                       r"picture_grabcut\853213062009600034_gc\00000700_00000000011BF4DE.bmp", 0)  # trainImage
#     # sift = cv2.SIFT()
#     sift = cv2.xfeatures2d.SURF_create()
#     kp1, des1 = sift.detectAndCompute(img1, None)
#     kp2, des2 = sift.detectAndCompute(img2, None)
#     # 蛮力匹配算法,有两个参数，距离度量(L2(default),L1)，是否交叉匹配(默认false)
#     bf = cv2.BFMatcher()
#     # 返回k个最佳匹配
#     matches = bf.knnMatch(des1, des2, k=2)
#     # cv2.drawMatchesKnn expects list of lists as matches.
#     # opencv3.0有drawMatchesKnn函数
#     # Apply ratio test
#     # 比值测试，首先获取与A 距离最近的点B（最近）和C（次近），只有当B/C
#     # 小于阈值时（0.75）才被认为是匹配，因为假设匹配是一一对应的，真正的匹配的理想距离为0
#     good = []
#     for m, n in matches:
#         if m.distance < 0.75 * n.distance:
#             good.append([m])
#     img3 = cv2.drawMatchesKnn(img1, kp1, img2, kp2, good[:10], None, flags=2)
#     # cv2.drawm
#     plt.imshow(img3), plt.show()
matchSift()
# getSift()
