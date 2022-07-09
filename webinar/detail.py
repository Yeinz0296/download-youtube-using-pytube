from pytube import YouTube
import datetime

link = "https://youtu.be/aiBz74rkksI"
yt = YouTube(link)

saat = yt.length
duration = str(datetime.timedelta(seconds=saat))
print("Title: ", yt.title)
print("Views: ", yt.views)
print("Length: ", duration)

SQ = yt.streams.filter()

for x in SQ:
    print("Resolution: {} \n Type: {}\n itag: {} \n".format(x.resolution, x.type, x.itag))