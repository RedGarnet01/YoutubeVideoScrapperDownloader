from pytube import YouTube


def choose_one():
    print("Enter the video link")
    link = input()

    yt = YouTube(link)  # get the link
    videos = yt.streams.all()    # extract the link

    # sort the videos out
    s = 1
    for v in videos:
        print(str(s) + ". " + str(v))
        s += 1

    print("Enter the number of the video: ")
    n = int(input())
    vid = videos[n - 1]   # the video that you pick

    print("Donwloading Please Wait...")
    destination = '/Users/Jovan/Desktop/YoutubeDownloader'
    # the video that you pick gets downloaded to your destination
    vid.download(destination)

    print("\n" + yt.title + "\nHas Been successfully downloaded" + "\n")


if __name__ == '__main__':
    choose_one()
