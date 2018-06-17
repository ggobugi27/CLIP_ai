import faceYoutube as fy
import captureFace as cf


def getImages(url, name, seconds) : 
	fy.download(url, name)
	cf.captureFace(name + '.mkv', seconds)

getImages('https://www.youtube.com/watch?v=iIPH8LFYFRk', 'era', 3)
