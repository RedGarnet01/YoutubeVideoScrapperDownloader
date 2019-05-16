from pytube import YouTube


def yt_download():
    print("Enter the video link")
    link = input()

    yt = YouTube(link)  # get the link
    videos = yt.streams.first()
    # videos = yt.streams.all()    # extract the link

    # sort the videos out
    # s = 1
    # for v in videos:
    #     print(str(s) + ". " + str(v))
    #     s += 1
    #
    # print("Enter the nuber of the video: ")
    # n = int(input())
    # vid = videos[n-1]

    print("Donwloading Please Wait...")
    destination = '/Users/Jovan/Desktop/YoutubeDownloader'
    videos.download(destination)

    print("\n" + yt.title + "\nHas Been successfully downloaded" + "\n")

if __name__ == '__main__':
    yt_download()
