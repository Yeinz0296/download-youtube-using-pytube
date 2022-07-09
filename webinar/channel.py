from pytube import *

ytl = "https://www.youtube.com/c/Ohara-the-Fox/videos"
ytc =Channel(ytl)

print(ytc.channel_name)
print(len(ytc))