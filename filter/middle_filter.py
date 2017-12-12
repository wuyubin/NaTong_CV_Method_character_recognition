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
    filepath_save = os.path.join('%s%s' % ('E:\\lenovo_exercitation\\natong_work\\natong_product\\grabcut_folder', allDir__))
    filepath_save = filepath_save + '_mf'
    # print (filepath_save)            # child.decode('gbk')  # .decode('gbk')是解决中文显示乱码问题
    pathdir_min = os.listdir(filepath_min)
    # # 保存路径
    # isExists = os.path.exists(filepath_save)
    # # 判断结果
    # if not isExists:
    #     # 如果不存在则创建目录
    #     os.makedirs(filepath_save)

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


        # filepath_min_save = filepath_min + "_new\\" + alldir_min
        # print(filepath_min_save)
        # cv2.imshow(middle_img)



        # #保存
        filepath_min_save = filepath_save + "\\"+alldir_min
        print(filepath_min_save)
        cv2.imwrite(filepath_min_save,middle_img, params=None)
