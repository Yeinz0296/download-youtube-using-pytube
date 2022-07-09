from pytube import YouTube
import math
import datetime

link = "https://youtu.be/aiBz74rkksI"
yt = YouTube(link)
path = "pytube"

saat = yt.length
duration = str(datetime.timedelta(seconds=saat))
print("Title: ", yt.title)
print("Views: ", yt.views)
print("Length: ", duration)

SQ = yt.streams
SQ_itag = SQ.get_by_itag(22)
# SQ_filesize = SQ_itag.filesize
# b_size = SQ_filesize
# mb_size = b_size/math.pow(1024,2)
# print("Size dia {:.2f} MB".format(mb_size))
SQ_itag.download(path)
SQ_itag.on_complete()


# print(SQ)
# for x in SQ:
#     print("Resolution: {} \n Type: {}\n itag: {} \n".format(x.resolution, x.type, x.itag))