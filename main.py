from pytubefix import YouTube
from sys import argv

if len(argv) < 2:
    print("Usage: python main.py <YouTube URL>")
    exit(1)

# Get the YouTube video link from command line arguments
link = argv[1]
try:
    yt = YouTube(link)
    print("Title: ", yt.title)
    print("Number of views: ", yt.views)
    yd = yt.streams.get_highest_resolution()
    print("Downloading...")
    yd.download( './downloads' )
    print("Download completed!")
except Exception as e:
    print("Error:", e)