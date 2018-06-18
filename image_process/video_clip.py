from moviepy.editor import VideoFileClip, concatenate_videoclips

def videoClipper(path, t1):
	video = VideoFileClip(path)
	print (video.fps)
	clip = video.subclip(t1, t1+1)
	print(clip)
	return clip

def clipToMp4(clip, outputPath):#name of subclip
	clip.write_videofile(outputPath, temp_audiofile="temp-audio.m4a", remove_temp=True, codec="libx264", audio_codec="aac")


clip1 = videoClipper('../web/public/test2.mkv', 26)
# clip2 = videoClipper('../web/public/test2.mkv', 31)#Seungri
clip3 = videoClipper('../web/public/test2.mkv', 63)
clip4 = videoClipper('../web/public/test2.mkv', 64)
clip5 = videoClipper('../web/public/test2.mkv', 102)
# clip6 = videoClipper('../web/public/test2.mkv', 110)#TOP
# clip7 = videoClipper('../web/public/test2.mkv', 111)#TOP
# clip8 = videoClipper('../web/public/test2.mkv', 132)#Daesung
clip9 = videoClipper('../web/public/test2.mkv', 149)
clip10 = videoClipper('../web/public/test2.mkv', 154)
clip11 = videoClipper('../web/public/test2.mkv', 232)

final_clip = concatenate_videoclips([clip1,clip3,clip4,clip5,clip9,clip10,clip11])
final_clip.write_videofile("test_2_gd.mp4", temp_audiofile="temp-audio.m4a", remove_temp=True, codec="libx264", audio_codec="aac")