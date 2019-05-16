from pytube import YouTube

def first_one():
    print("Enter the video link")
    link = input()

    yt = YouTube(link)  # get the link
    videos = yt.streams.first()     # gets the first stream

    print("Donwloading Please Wait...")
    destination = '/Users/Jovan/Desktop/YoutubeDownloader'
    videos.download(destination)    # download the stream to a destination

    print("\n" + yt.title + "\nHas Been successfully downloaded" + "\n")

if __name__ == '__main__':
    first_one()
