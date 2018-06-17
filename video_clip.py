from moviepy.editor import VideoFileClip, concatenate_videoclips

def videoClipper(path, t1, t2):
	video = VideoFileClip(path)
	print (video.fps)
	clip = video.subclip(t1, t2)
	return clip

def clipToMp4(clip, outputPath):#name of subclip
	clip.write_videofile(outputPath)

clip = videoClipper('../vid_cap/BTS.mp4', 50, 100)
# clipToMp4(clip, 'BTS3.mp4')