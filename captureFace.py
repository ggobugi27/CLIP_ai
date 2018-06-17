import cv2
import math
import numpy as np
import os
import face_recognition
from detect_face import numFace 
from label_image import readFace

def captureFace(videoFile, seconds):#mp4 file, interval of seconds to be captured
	name = videoFile.split('.')[0]
	# if not os.pathexists(name): 
	os.mkdir(name)
	vidcap = cv2.VideoCapture(videoFile)# for face_location in face_locations:
	success,image = vidcap.read()
	fps = vidcap.get(cv2.CAP_PROP_FPS)
	multiplier = int(round(fps * seconds))
	i = 1
	while success: 
		frameId = int(round(vidcap.get(1))) #current frame number, rounded b/c sometimes you get frame intervals which aren't integers...this adds a little imprecision but is likely good enough
		success, image = vidcap.read()
		if (frameId % multiplier == 0):
			# print (numFace(image))
			# if (numFace(image)>0):
			face_locations = face_recognition.face_locations(image)
			face_num = len(face_locations)
			print (face_num)
			if (face_num > 0): 
				print ("%s/face%d.jpg"%(name, i))
				# savedPath = re.complie("%s/face%d.jpg" % (name, i))
				# print(savedPath, 'savedPath')
				cv2.imwrite("%s/face%d.jpg"%(name, i), image)
				# print("in frame%d"%i, readFace("%s/face%d.jpg" % (name, i)))
				i=i+1
