#encoding = 'utf-8'
import cv2
import matplotlib.pyplot as plt

img = cv2.imread(r"D:\Python_all\pythonholder\practice_project\character_recognition\test_image\test\test02\mid_filter_result.jpg",0)
img = cv2.resize(img,(384,216))
# cv2.namedWindow("Image")
# cv2.imshow("Image", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# cv2.Threshold(img, ret, 137, 255, cv2.CV_THRESH_TRUNC)


ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
ret,thresh4 = cv2.threshold(img,30,255,cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(img,200,255,cv2.THRESH_TOZERO_INV)
titles = ['img','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img,thresh1,thresh2,thresh3,thresh4,thresh5]
for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()