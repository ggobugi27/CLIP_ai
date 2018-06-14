# import cv2
# vidcap = cv2.VideoCapture('videoplayback.mp4')
# success,image = vidcap.read()
# count = 0
# success = True
# while success:
#   cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file      
#   success,image = vidcap.read()
#   print('Read a new frame: ', success)
#   success = False
#   print (count, 'image', image)
#   count += 1

import cv2
import math
import numpy as np

################### Setting up the file ################
videoFile = "TVXQ.mp4"
vidcap = cv2.VideoCapture(videoFile)
success,image = vidcap.read()

#################### Setting up parameters ################

seconds = 3
fps = vidcap.get(cv2.CAP_PROP_FPS) # Gets the frames per second
multiplier = int(round(fps * seconds))

#################### Initiate Process ################

while success:
    frameId = int(round(vidcap.get(1))) #current frame number, rounded b/c sometimes you get frame intervals which aren't integers...this adds a little imprecision but is likely good enough
    success, image = vidcap.read()
    if frameId % multiplier == 0:
        cv2.imwrite("TVXQ/frame%d.jpg" % frameId, image)

vidcap.release()
print "Complete"