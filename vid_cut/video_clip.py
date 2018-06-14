from moviepy.editor import VideoFileClip, concatenate_videoclips
# import moviepy.editor



myclip1 = VideoFileClip("../vid_cap/BTS.mp4")
myclip2 = VideoFileClip("../vid_cap/TVXQ.mp4")
# Note that these clips will have an fps (frame per second) attribute, which will be transmitted if you do small modifications of the clip, and will be used by default in write_videofile, write_gif, etc. For instance:

print (myclip2.fps) # prints for instance '30'
# Now cut the clip between t=10 and 25 secs. This conserves the fps.
myclip2 = myclip1.subclip(10, 25)
myclip2.write_videofile("BTS2.mp4") # the gif will have 30 fps