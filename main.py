from pytube import *
import datetime
import math

path = 'Download'

def main():
    text = input('Search or Copy link: ')
    if 'https' in text:
        detail(text)
        senaraiyt()
        download()
    else:
        cari(text)

def detail(ytlink,):
    global yt
    yt = YouTube(ytlink)
    print("Title: ", yt.title) #Title of video
    print("Author: ", yt.author)
    print("Number of views: ", yt.views) #Number of views of video
    second = yt.length
    minute = str(datetime.timedelta(seconds=second))
    print("Length of video: ", minute) #Length of the video

def cari(mencari):
    yts = Search(mencari)
    print(len(yts.results))
    for x in yts.results:
        print("Title: {}\nView: {}\nLink: {}\n".format(x.title, x.views,x.watch_url,))

def senaraiyt():
    global senarai
    senarai = yt.streams
    for video in senarai:
        print("Resolution: {}\nProgressive: {}\nType: {}\nItag: {}\nSize: {:.2f} MB\n".format(video.resolution,video.is_progressive,video.type,video.itag, size(video.itag)))

def size(i_tag):
    SQ_itag = senarai.get_by_itag(i_tag)
    b_size= SQ_itag.filesize
    mb_size = b_size/math.pow(1024,2)
    # print("Size dia {:.2f} MB".format(mb_size))
    return mb_size

def download():
    i_tag = int(input("Input itag to download: "))
    while True:
        try:
            yd = senarai.get_by_itag(i_tag)
            yd.download(path)
            print('Download Siap')
            break
        except:
            print('Salah itag')
            download()
            break

main()