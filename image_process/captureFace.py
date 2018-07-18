import cv2
import math
import numpy as np
import os
import face_recognition
# from detect_face import numFace
from label_image import readFace

import warnings

warnings.filterwarnings('ignore')



def captureFace(videoFile, seconds):  # mp4 file, interval of seconds to be captured
    name = videoFile[0:-4]
    # os.mkdir(name)
    vidcap = cv2.VideoCapture(videoFile)
    success, image = vidcap.read()
    fps = vidcap.get(cv2.CAP_PROP_FPS)
    multiplier = int(round(fps * seconds))
    info = {}
    i = 1  # nth number of frame
    j = 1  # frame
    while success:
        j = j + 1
        # current frame number, rounded b/c sometimes you get frame intervals which aren't integers...this adds a little imprecision but is likely good enough
        frameId = int(round(vidcap.get(1)))
        success, image = vidcap.read()
        if (frameId % multiplier == 0):
            t = frameId/multiplier;
            # print (numFace(image))
            # if (numFace(image)>0):
            face_locations = face_recognition.face_locations(image)
            face_num = len(face_locations)
            if (face_num > 0):
                cv2.imwrite("%s/face%d.jpg" % (name, t), image)
                info[j] = readFace("%s/face%d.jpg" % (name, t))[0:face_num]
                print("frame %d:" % t, readFace("%s/face%d.jpg" % (name, t))[0:face_num])
                i = i + 1
    print('done!')