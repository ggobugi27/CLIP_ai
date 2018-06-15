from PIL import Image
import cv2
import numpy as np

from matplotlib import pyplot as plt
# import matplotlib

# img = cv2.imread('../vid_cap/TVXQ/frame7020.jpg',0)
# show_img = Image.fromarray(img)
# img2 = img.copy()
# template = cv2.imread('template.jpg',0)
# show_template = Image.fromarray(template)
# show_template.show()
# w, h = template.shape[::-1]

# All the 6 methods for comparison in a list
methods = ['cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

template = cv2.imread('../faces/BTS/face%d.jpg' % (1248), 0)
# print ('../faces/BTS/frame%d.jpg'%6768)
# i = 90
# while (i <= 2070):
    # i = i + 90
img = cv2.imread('../faces/BTS/face%d.jpg' %(1440), 0)
img2 = img.copy()
w, h = template.shape[::-1]
for meth in methods:
    img = img2.copy()
    method = eval(meth)

    # Apply template Matching
    res = cv2.matchTemplate(img,template,method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)

    cv2.rectangle(img,top_left, bottom_right, 255, 2)
    # cv2.imshow('image', img)
    # show_img = Image.fromarray(res)
    # show_img.show()
    # cv2.imshow('image', show_img)
    plt.subplot(121),plt.imshow(res,cmap = 'gray')
    plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(img,cmap = 'gray')
    plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
    plt.suptitle(meth)
    plt.show()