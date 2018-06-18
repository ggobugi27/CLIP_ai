import faceYoutube as fy
import captureFace as cf
import sys 
import warnings

warnings.filterwarnings('ignore')
arg1 = sys.argv[1] #value1
arg2 = sys.argv[2] #value2
arg3 = float(sys.argv[3]) #value3


def getImages(url, name, seconds) : 
	fy.download(url, 'public/'+name)
	return cf.captureFace('public/'+name + '.mkv', seconds)

getImages(arg1, arg2, arg3)

# getImages("https://www.youtube.com/watch?v=9jTo6hTZmiQ", 'test1', 1)