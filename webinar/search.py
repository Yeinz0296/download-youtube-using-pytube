from pytube import Search

cari = input('Search: ')
yts = Search(cari)

for video in yts.results:
    print("Title: {}\nView: {}\nLink: {}\n".format(video.title, video.views,video.watch_url,))