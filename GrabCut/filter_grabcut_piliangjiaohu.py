# -*- coding: UTF-8 -*-
import os
import cv2
import numpy as np
from matplotlib import pyplot

BLUE = [255,0,0]        # rectangle color
RED = [0,0,255]         # PR BG
GREEN = [0,255,0]       # PR FG
BLACK = [0,0,0]         # sure BG
WHITE = [255,255,255]   # sure FG

DRAW_BG = {'color' : BLACK, 'val' : 0}
DRAW_FG = {'color' : WHITE, 'val' : 1}
DRAW_PR_FG = {'color' : GREEN, 'val' : 3}
DRAW_PR_BG = {'color' : RED, 'val' : 2}

# setting up flags
rect = (0,0,1,1)
drawing = False         # flag for drawing curves
rectangle = False       # flag for drawing rect
rect_over = False       # flag to check if rect drawn
rect_or_mask = 100      # flag for selecting rect or mask mode
value = DRAW_FG         # drawing initialized to FG
thickness = 3           # brush thickness

def onmouse(event,x,y,flags,param):
    global img,img2,drawing,value,mask,rectangle,rect,rect_or_mask,ix,iy,rect_over

    # Draw Rectangle
    if event == cv2.EVENT_RBUTTONDOWN:
        rectangle = True
        ix,iy = x,y

    elif event == cv2.EVENT_MOUSEMOVE:
        if rectangle == True:
            img = img2.copy()
            cv2.rectangle(img,(ix,iy),(x,y),BLUE,2)
            rect = (ix,iy,abs(ix-x),abs(iy-y))
            rect_or_mask = 0

    elif event == cv2.EVENT_RBUTTONUP:
        rectangle = False
        rect_over = True
        cv2.rectangle(img,(ix,iy),(x,y),BLUE,2)
        rect = (ix,iy,abs(ix-x),abs(iy-y))
        rect_or_mask = 0
        print (" Now press the key 'n' a few times until no further change \n")

    # draw touchup curves

    if event == cv2.EVENT_LBUTTONDOWN:
        if rect_over == False:
            print ("first draw rectangle \n")
        else:
            drawing = True
            cv2.circle(img,(x,y),thickness,value['color'],-1)
            cv2.circle(mask,(x,y),thickness,value['val'],-1)

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.circle(img,(x,y),thickness,value['color'],-1)
            cv2.circle(mask,(x,y),thickness,value['val'],-1)

    elif event == cv2.EVENT_LBUTTONUP:
        if drawing == True:
            drawing = False
            cv2.circle(img,(x,y),thickness,value['color'],-1)
            cv2.circle(mask,(x,y),thickness,value['val'],-1)

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
filepath = "E:\\lenovo_exercitation\\natong_work\\natong_product\\grabcut_folder"
pathDir = os.listdir(filepath)
for allDir in pathDir:
    allDir__ = '\\'+allDir
    filepath_save = os.path.join('%s%s' % ("E:\\lenovo_exercitation\\natong_work\\natong_product\\natong_product_picture_grabcut", allDir__))
    filepath_save = filepath_save+'_gc'
    filepath_min = os.path.join('%s%s' % (filepath, allDir__))
    # print (filepath_save)            # child.decode('gbk')  # .decode('gbk')是解决中文显示乱码问题
    pathdir_min = os.listdir(filepath_min)
    # # 保存路径
    # filepath_min = filepath_min + "_gc"
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

        # 高斯滤波
        # lbimg = cv2.GaussianBlur(img, (3, 3), 1.8)
        # 中值滤波
        img01 = salt(img, 500)
        middle_img = cv2.medianBlur(img01, 5)

        filepath_min_save = filepath_save +"\\"+ alldir_min
        #grabcut
        # Loading images
        img = middle_img
        img = cv2.resize(img, (678, 444))
        img2 = img.copy()  # a copy of original image
        mask = np.zeros(img.shape[:2], dtype=np.uint8)  # mask initialized to PR_BG
        output = np.zeros(img.shape, np.uint8)  # output image to be shown

        # input and output windows
        cv2.namedWindow('output')
        cv2.namedWindow('input')
        cv2.setMouseCallback('input', onmouse)
        cv2.moveWindow('input', img.shape[1] + 10, 90)

        # print(" Instructions : \n")
        # print(" Draw a rectangle around the object using right mouse button \n")
        flag = 1
        while (flag):

            cv2.imshow('output', output)
            cv2.imshow('input', img)
            k = 0xFF & cv2.waitKey(1)

            # key bindings
            if k == 27:  # esc to exit
                break
            elif k == ord('0'):  # BG drawing
                # print(" mark background regions with left mouse button \n")
                value = DRAW_BG
            elif k == ord('1'):  # FG drawing
                # print(" mark foreground regions with left mouse button \n")
                value = DRAW_FG
            elif k == ord('2'):  # PR_BG drawing
                value = DRAW_PR_BG
            elif k == ord('3'):  # PR_FG drawing
                value = DRAW_PR_FG
            elif k == ord('s'):  # save image
                bar = np.zeros((img.shape[0], 5, 3), np.uint8)
                res = np.hstack((img2, bar, img, bar, output))
                isExists = os.path.exists(filepath_min_save)
                # 判断结果
                if not isExists:
                    # 如果不存在则保存
                    cv2.imwrite(filepath_min_save, output)
                    print(filepath_min_save)

                # cv2.imwrite('grabcut_output_combined.png', res)
                # print(" Result saved as image \n")
                flag = 0
            elif k == ord('r'):  # reset everything
                # print("resetting \n")
                rect = (0, 0, 1, 1)
                drawing = False
                rectangle = False
                rect_or_mask = 100
                rect_over = False
                value = DRAW_FG
                img = img2.copy()
                mask = np.zeros(img.shape[:2], dtype=np.uint8)  # mask initialized to PR_BG
                output = np.zeros(img.shape, np.uint8)  # output image to be shown
            elif k == ord('n'):  # segment the image
                # print(""" For finer touchups, mark foreground and background after pressing keys 0-3
                # and again press 'n' \n""")
                if (rect_or_mask == 0):  # grabcut with rect
                    bgdmodel = np.zeros((1, 65), np.float64)
                    fgdmodel = np.zeros((1, 65), np.float64)
                    cv2.grabCut(img2, mask, rect, bgdmodel, fgdmodel, 1, cv2.GC_INIT_WITH_RECT)
                    rect_or_mask = 1
                elif rect_or_mask == 1:  # grabcut with mask
                    bgdmodel = np.zeros((1, 65), np.float64)
                    fgdmodel = np.zeros((1, 65), np.float64)
                    cv2.grabCut(img2, mask, rect, bgdmodel, fgdmodel, 1, cv2.GC_INIT_WITH_MASK)

            mask2 = np.where((mask == 1) + (mask == 3), 255, 0).astype('uint8')
            output = cv2.bitwise_and(img2, img2, mask=mask2)

        cv2.destroyAllWindows()




        # #保存
        # filepath_min_save = filepath_min + "_new\\"+alldir_min
        # # print(filepath_min_save)
        # cv2.imwrite(filepath_min_save,img_final, params=None)
