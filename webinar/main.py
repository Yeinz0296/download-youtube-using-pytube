from pytube import YouTube
import datetime
import math

link = "https://www.youtube.com/watch?v=aiBz74rkksI&ab_channel=Masyhur"
ytl = YouTube(link)
path = 'webinar'

saat = ytl.length
duration = str(datetime.timedelta(seconds=saat))

print("Title: ", ytl.title)
print("Views: ", ytl.views)
print("Lenght: ", duration)
print("Author: ", ytl.author)

yts = ytl.streams

# for video in yts:
#     print("Resoltuion: {}\nItag: {}\nType: {}\nProgressive: {}\n".format(video.resolution, video.itag, video.type, video.is_progressive))

ytd = yts.get_by_itag(22)
ytd.download(path)
b_filesize = ytd.filesize
mb_filesize = b_filesize/math.pow(1024,2)
print('Siap Download {:.2f} MBytes'.format(mb_filesize))




