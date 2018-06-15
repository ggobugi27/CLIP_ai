import faceYoutube as fy
import captureFace as cf


def getImages(url, name, seconds) : 
	fy.download(url, name)
	cf.captureFace(name, seconds)


getImages('https://www.youtube.com/watch?v=EVaV7AwqBWg', 'WAN.mp4', 10)