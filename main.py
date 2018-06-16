import faceYoutube as fy
import captureFace as cf


def getImages(url, name, seconds) : 
	fy.download(url, name)
	cf.captureFace(name + '.mkv', seconds)


# getImages('https://www.youtube.com/watch?v=BQlsiVWWIx4', 'WAN.mp4', 10)