from PIL import Image
from matplotlib import pyplot as plt
import numpy as np
import cv2
#load cascade classifier training file for lbpcascade 
lbp_face_cascade = cv2.CascadeClassifier('lbpcascade_frontalface.xml')  
 
#load test image 
test2 = cv2.imread('../vid_cap/TVXQ/frame6030.jpg') 
 
 #just making a copy of image passed, so that passed image is not changed 
img_copy = test2.copy()          

#convert the test image to gray image as opencv face detector expects gray images
gray = cv2.cvtColor(img_copy, cv2.COLOR_BGR2GRAY)          

#let's detect multiscale (some images may be closer to camera than others) images
faces = lbp_face_cascade.detectMultiScale(gray, 1.1, 5)       

#go over list of faces and draw them as rectangles on original colored img
for (x, y, w, h) in faces:
  cv2.rectangle(img_copy, (x, y), (x+w, y+h), (0, 255, 0), 2)              

# return img_copy


faces_detected_img = img_copy
#convert image to RGB and show image 
a = cv2.cvtColor(faces_detected_img, cv2.COLOR_BGR2RGB)
pil_image = Image.fromarray(a)
pil_image.show()