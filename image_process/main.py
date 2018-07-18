import faceYoutube as fy
import captureFace as cf
import sys 
import warnings

warnings.filterwarnings('ignore')
arg1 = sys.argv[1] #value1, youtube url
arg2 = sys.argv[2] #value2, name of directory
arg3 = float(sys.argv[3]) #value3, fram capture interval in seconds

def getImages(url, name, seconds) : 
	fy.download(url, 'public/'+name)
	return cf.captureFace('public/'+name + '.mkv', seconds)#assume video is mkv (Refactor later)