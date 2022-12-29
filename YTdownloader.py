from pytube import YouTube
'''
from sys import argv
link= argv[1]
yt =Youtube(link)
print("Title",yt.title)
print("View",yt.views)
yd= yt.streams.get_highest_resolution()
'''
def Download(link):
  youtubeObject= YouTube(link)
  youtubeObject =youtubeObject.streams.get_highest_resolution()
  try:
    youtubeObject.download()
  except:
    print("There has been an error in downloading your youtube video ")
  print("This download is completed! YAY!")

link=input("Put your Youtube link here! URL: ")
Download(link)
