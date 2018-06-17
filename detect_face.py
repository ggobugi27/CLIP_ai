# import sys
import cv2

def numFace(imagePath):
	# Get user supplied values
	faceCascade = cv2.CascadeClassifier('img_recognize/haarcascade_frontalface_default.xml')


	# # Read the image
	image = cv2.imread(imagePath)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	# Detect faces in the image

	faces = faceCascade.detectMultiScale(gray, 1.1, 5)
	# faces = faceCascade.detectMultiScale(
	#     gray,
	#     scaleFactor=1.1,
	#     minNeighbors=5,
	#     minSize=(30, 30),
	#     flags = cv2.CV_HAAR_SCALE_IMAGE
	# )
	print(len(faces))
	return len(faces)


# print "Found {0} faces!".format(len(faces))

# # Draw a rectangle around the faces
# 	for (x, y, w, h) in faces:
# 	    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

# 	cv2.imshow("Faces found", image)
# 	cv2.waitKey(0)

# numFace('Sober/face13.jpg')