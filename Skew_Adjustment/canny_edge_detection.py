import numpy
import argparse
import cv2

image = cv2.imread(r"E:\lenovo_exercitation\natong_work\natong_product\natong_product_picture_grabcut"
                 r"\962215080911800020_gc\00000268_0000000000A974D4.bmp", 1)
# cv2.imshow("Original", image)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# cv2.imshow("Gray", gray)
# 30 and 150 is the threshold, larger than 150 is considered as edge,
# less than 30 is considered as not edge
canny = cv2.Canny(gray, 30, 150)
canny = numpy.uint8(numpy.absolute(canny))
# display two images in a figure
cv2.imshow("Edge detection by Canny", numpy.hstack([gray, canny]))
# cv2.imwrite("1_edge_by_canny.jpg", numpy.hstack([gray, canny]))
# cv2.imwrite("1_edge_by_canny.jpg", canny)

if (cv2.waitKey(0) == 27):
    cv2.destroyAllWindows()