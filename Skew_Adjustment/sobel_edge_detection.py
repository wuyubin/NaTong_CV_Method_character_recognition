# coding=utf-8
import cv2
import numpy as np

img = cv2.imread(r"E:\lenovo_exercitation\natong_work\natong_product\natong_product_picture_grabcut"
                 r"\962215080911800020_gc\00000268_0000000000A974D4.bmp", 1)
#16位有符号的数据类型，即cv2.CV_16S
x = cv2.Sobel(img, cv2.CV_16S, 1, 0)
y = cv2.Sobel(img, cv2.CV_16S, 0, 1)
# 转回uint8
absX = cv2.convertScaleAbs(x)
absY = cv2.convertScaleAbs(y)
#将两个方向上的算子计算结果加起来。
dst = cv2.addWeighted(absX, 0.5, absY, 0.5, 0)

# cv2.imshow("src",img)
# cv2.imshow("absX", absX)
# cv2.imshow("absY", absY)

cv2.imshow("Result", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()