import youtube_dl

def download(url, fileName):#String
	ydl_opts = {'outtmpl': fileName}
	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
	    ydl.download([url])
	    