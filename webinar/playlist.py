from pytube import Playlist

ytl = "https://www.youtube.com/watch?v=AZhkjkLsh_o&list=UUovw7Ksx437NHFgGvg_tX2A&ab_channel=Ohara"
ytp = Playlist(ytl)

path = ("ohara")

for video in ytp.videos:
    #print("Title: {} \n View: {}\n Lenght: {}\n".format(video.title,video.views,video.length))
    video.streams.get_lowest_resolution().download(path)