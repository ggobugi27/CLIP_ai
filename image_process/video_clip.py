from moviepy.editor import VideoFileClip, concatenate_videoclips

def videoClipper(path, t1):
	video = VideoFileClip(path)
	print (video.fps)
	clip = video.subclip(t1, t1+1)
	print(clip)
	return clip

def clipToMp4(clip, outputPath):#name of subclip
	clip.write_videofile(outputPath, temp_audiofile="temp-audio.m4a", remove_temp=True, codec="libx264", audio_codec="aac")
