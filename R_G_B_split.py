
import cv2
import numpy

def get_red(img):
    redImg = img[:,:,2]
    return redImg

def get_green(img):
    greenImg = img[:,:,1]
    return greenImg

def get_blue(img):
    blueImg = img[:,:,0]
    return blueImg

if __name__ == '__main__':
    img = cv2.imread(r"D:\Python_all\pythonholder\practice_project\character_recognition\test_image\test\test03\middle_result.jpg",1)

    img = cv2.resize(img, (678, 444))
    cv2.imshow('p',img)
    # b, g, r = cv2.split(img)
    # cv2.imshow("Blue 1", b)
    # cv2.imshow("Green 1", g)
    # cv2.imshow("Red 1", r)
    b = get_blue(img)
    g = get_green(img)
    r = get_red(img)
    cv2.imshow("Blue 2", b)
    cv2.imshow("Green 2", g)
    cv2.imshow("Red 2", r)
    cv2.waitKey(0)
    cv2.destroyAllWindows()