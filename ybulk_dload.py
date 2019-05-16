from pytube import YouTube

SAVE_PATH = '/Users/Jovan/Movies'
text_file = 'links.txt'

def bulk_load():
    links = open(text_file, 'r')
    s = 1
    for l in links:
        get_true = True     # this will check that there is a youtube link, if there is then its True and will continue
        while get_true:
            try:
                yt = YouTube(l)     # gets the first link in the text file
                videos = yt.streams.first()     # gets the video from the file
                get_true = False
            except:
                print("Connection Error")
                continue

        # this will put a number infront of the video title
        try:
            print(str(s) + ". " + str(yt.title))
            s += 1
        except:
            pass

        # this will download the video to the select path
        try:
            videos.download(SAVE_PATH)
        except:
            print("Error, Maybe Duplicate File")
            continue

if __name__ == '__main__':
    bulk_load()
