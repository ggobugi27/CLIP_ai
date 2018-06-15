zimport cv2
import math
import numpy as np
import os

def captureVid(videoFile, seconds, outputPath):#mp4 file, seconds to be captured 
	os.mkdir('frames/%s'%videoFile)
	vidcap = cv2.VideoCapture(videoFile)
	success,image = vidcap.read()
	fps = vidcap.get(cv2.CAP_PROP_FPS)
	multiplier = int(round(fps * seconds))	
	while success: 
		frameId = int(round(vidcap.get(1))) #current frame number, rounded b/c sometimes you get frame intervals which aren't integers...this adds a little imprecision but is likely good enough
		success, image = vidcap.read()
		if frameId % multiplier == 0:
		    print(("%s/%s/frame%d.jpg" % (outputPath, frameId)))
		    cv2.imwrite("%s/%s/frame%d.jpg" % (outputPath, videoFile, frameId), image)
	return {'fps': fps, 'multiplier': multiplier}