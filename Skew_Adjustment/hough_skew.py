# coding = 'utf-8'
# Python program to illustrate HoughLine
# method for line detection
import cv2
import numpy as np
import math


# 定义旋转rotate函数
def rotate(image, angle, center=None, scale=1.0):
    # 获取图像尺寸
    (h, w) = image.shape[:2]
    # 若未指定旋转中心，则将图像中心设为旋转中心
    if center is None:
        center = (w / 2, h / 2)
    # 执行旋转
    M = cv2.getRotationMatrix2D(center, angle, scale)
    rotated = cv2.warpAffine(image, M, (w, h))
    # 返回旋转后的图像
    return rotated

# Reading the required image in
# which operations are to be done.
# Make sure that the image is in the same
# directory in which this python program is
img = cv2.imread(r"E:\lenovo_exercitation\natong_work\natong_product\natong_product_picture_grabcut"
                 r"\13022315000008_gc\00000008_00000000001CF546.bmp", 1)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# Apply edge detection method on the image
edges = cv2.Canny(gray,50,150,apertureSize = 3)
# This returns an array of r and theta values
lines = cv2.HoughLines(edges, 1, np.pi/180, 30)
print(lines)
# The below for loop runs till r and theta values
# are in the range of the 2d array
for r,theta in lines[0]:
    # Stores the value of cos(theta) in a
    a = np.cos(theta)
    # Stores the value of sin(theta) in b
    b = np.sin(theta)
    # x0 stores the value rcos(theta)
    x0 = a*r
    # y0 stores the value rsin(theta)
    y0 = b*r
    # x1 stores the rounded off value of (rcos(theta)-1000sin(theta))
    x1 = int(x0 + 1000*(-b))
    # y1 stores the rounded off value of (rsin(theta)+1000cos(theta))
    y1 = int(y0 + 1000*(a))
    # x2 stores the rounded off value of (rcos(theta)+1000sin(theta))
    x2 = int(x0 - 1000*(-b))
    # y2 stores the rounded off value of (rsin(theta)-1000cos(theta))
    y2 = int(y0 - 1000*(a))

    jiaodu = math.atan((y2-y1)/(x2-x1))*180/math.pi
    # print(jiaodu)
    # cv2.line draws a line in img from the point(x1,y1) to (x2,y2).
    # (0,0,255) denotes the colour of the line to be
    #drawn. In this case, it is red.
    cv2.line(img,(x1,y1), (x2,y2), (0,0,255),2)

rotated = rotate(img, jiaodu)

cv2.imshow('result',rotated)


# All the changes made in the input image are finally
# written on a new image houghlines.jpg
# cv2.imwrite('houghlines3.jpg', img)
cv2.imshow('src',img)

cv2.waitKey(0)
cv2.destroyAllWindows()