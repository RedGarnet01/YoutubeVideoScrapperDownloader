from pytube import YouTube

SAVE_PATH = "/Users/Jovan/Movies"
# links = open('links.txt','r')


def bulk_load():

    links = open('links.txt', 'r')
    for l in links:
        get_true = True
        while get_true:
            try:
                yt = YouTube(l)
                get_true = False
            except:
                print("Connection Error")
                continue

        # mp4files = yt.filter(file_extension='mp4').all()
        try:
            print(yt.filename)
            print(mp4files[-1])
        except:
            pass

        # video = yt.get(mp4files[-1].extension,mp4files[-1].resolution)
        try:
            video.download(SAVE_PATH)
        except:
            print("Error, Maybe Duplicate File")
            continue


if __name__ == '__main__':
    bulk_load()
