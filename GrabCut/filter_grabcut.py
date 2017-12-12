# -*- coding: UTF-8 -*-
import os
import cv2
import numpy as np
from matplotlib import pyplot


def salt(img, n):
    for k in range(n):
        i = int(np.random.random() * img.shape[1]);
        j = int(np.random.random() * img.shape[0]);
        if img.ndim == 2:
            img[j, i] = 255
        elif img.ndim == 3:
            img[j, i, 0] = 255
            img[j, i, 1] = 255
            img[j, i, 2] = 255
    return img

# 遍历指定目录，显示目录下的所有文件名
filepath = "E:\\lenovo_exercitation\\natong_work\\natong_product\\natong_product_picture"
pathDir = os.listdir(filepath)
for allDir in pathDir:
    allDir__ = '\\'+allDir
    filepath_min = os.path.join('%s%s' % (filepath, allDir__))
    # print (filepath_min)            # child.decode('gbk')  # .decode('gbk')是解决中文显示乱码问题
    pathdir_min = os.listdir(filepath_min)
    # # 保存路径
    # filepath_min = filepath_min + "_new"
    # isExists = os.path.exists(filepath_min)
    # # 判断结果
    # if not isExists:
    #     # 如果不存在则创建目录
    #     os.makedirs(filepath_min)
    for alldir_min in pathdir_min:
        alldir_min__ = '\\' + alldir_min

        filepath_final = os.path.join('%s%s' % (filepath_min, alldir_min__))

        # print(filepath_final)
        read_path = filepath_final
        img = cv2.imread(read_path,1)

        #中值滤波
        # img = cv2.resize(img,(384,216))
        # 高斯滤波
        # lbimg = cv2.GaussianBlur(img, (3, 3), 1.8)
        # 中值滤波
        img01 = salt(img, 500)
        middle_img = cv2.medianBlur(img01, 5)

        # #grabcut
        # mask = np.zeros(img.shape[:2], np.uint8)
        # bgdModel = np.zeros((1, 65), np.float64)
        # fgdModel = np.zeros((1, 65), np.float64)
        #
        # # rect = (249,1049,3840-249,2160-1049)#划定区域37451673
        # rect = (1, 1, 3839, 2159)  # 划定待分割区域37451673
        # cv2.grabCut(middle_img, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)  # 函数返回值为mask,bgdModel,fgdModel
        # mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')  # 0和2做背景
        #
        # img_final = middle_img * mask2[:, :, np.newaxis]  # 使用蒙板来获取前景区域


        #grabcut
        filepath_min_save = filepath_min + "_new\\" + alldir_min
        # print(filepath_min_save)
        # cv2.imshow(middle_img)
        gc = grab()
        gc.grab_cut(middle_img, filepath_min_save)



        # #保存
        # filepath_min_save = filepath_min + "_new\\"+alldir_min
        # # print(filepath_min_save)
        # cv2.imwrite(filepath_min_save,img_final, params=None)
