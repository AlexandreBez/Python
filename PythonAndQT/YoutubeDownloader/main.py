from pytube import YouTube

from pytube import YouTube
yt = YouTube("https://www.youtube.com/watch?v=77-eidLP8zc")
yt = yt.get('mp4', '720p')
yt.download();