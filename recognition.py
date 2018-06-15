from PIL import Image
import face_recognition
import cv2

# def numFace(imgFile): 
# 	image = face_recognition.load_image_file(imgFile)
# 	face_locations = face_recognition.face_locations(image)
# 	face_num = len(face_locations)
# 	print("I found {} face(s) in this photograph.".format(len(face_locations)))
# 	return [image, locations, num]


# def saveFace(imgFile, outputPath):
# 	image, locations, num = [numFace(imgFile)]
# 	for face_location in locations:
# 		top, right, bottom, left = face_location
# 	    print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))
# 	    # You can access the actual face itself like this:
# 	    face_image = image[top:bottom, left:right]
# 	    pil_image = Image.fromarray(face_image)
# 	    cv2.imwrite(outputPath, face_image)
# 		    #save faces in a folder
		    # pil_image.show()
# print image
# face_locations = face_recognition.face_locations(image)

# Load the jpg file into a numpy array

# image = face_recognition.load_image_file("biden.jpg")
# image = face_recognition.load_image_file("../videocapture/BTS/frame5040.jpg")
# imageArray = [];
i = 312+24#multiplier from capture
while (i <= 7872):
	image = face_recognition.load_image_file("frames/BTS.mp4/frame%d.jpg" % i)
# # Find all the faces in the image using the default HOG-based model.
# # This method is fairly accurate, but not as accurate as the CNN model and not GPU accelerated.
# # See also: find_faces_in_picture_cnn.py	
	# Image.fromarray(image).show()
	face_locations = face_recognition.face_locations(image)
	face_num = len(face_locations)
	print("I found {} face(s) in this photograph.".format(len(face_locations)), i)
	i = i + 96
	if face_num > 0 : 
		cv2.imwrite("faces/BTS/BTS2/face%d.jpg" % i, image)
		# for face_location in face_locations:

		#     # Print the location of each face in this image
		#    # Print the location of each face in this image
		#     top, right, bottom, left = face_location
		#     print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))

		#     # You can access the actual face itself like this:
		#     face_image = image[top:bottom, left:right]
		#     pil_image = Image.fromarray(face_image)
		#     cv2.imwrite("faces/BTS/face%d.jpg" % i, face_image)
		    #save faces in a folder
		    # pil_image.show()


# pil_image = Image.fromarray(face_image)
#     pil_image.show()