from pytube import YouTube
import requests
import bs4
import os


print('Please enter the save path\n' + 'example: /Volumes/U/Youtbe\n' +
      'example: /Users/Jovan/Movies')

SAVE_PATH = input()     # /Users/Jovan/Movies

print('Folder name')
FOLDER_NAME = input()  # TestFolder

SAVE_FOLDER_PATH = os.makedirs(SAVE_PATH + "/" + FOLDER_NAME + "/")

print('Enter the name of the text file')
text_file = input()     # test

linkFile = open(SAVE_PATH + '/' + FOLDER_NAME +
                '/' + text_file + '.txt', 'w+')

print('Paste URL of YouTube Video Page')
url = input()


def youtube_scraper():

    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    # will find a list of stings
    video_div = soup.find_all('div', class_="yt-lockup-content")
    for i in video_div:
        get_true = True
        while get_true:

            link_content = linkFile.write('https://www.youtube.com' +
                                          i.h3.a['href'] + '\n')

            get_true = False
    linkFile.close()


def bulk_load():
    links = open(SAVE_PATH + '/' + FOLDER_NAME + '/' + text_file + '.txt', 'r')
    for l in links:
        gett_true = True
        while gett_true:
            try:
                yt = YouTube(l)
                videos = yt.streams.first()
                gett_true = False
            except:
                print("Connection Error")
                continue

            try:
                print("Donwloading Please Wait...")
                videos.download(SAVE_PATH + '/' + FOLDER_NAME)
                print("\n" + yt.title + "\nHas Been successfully downloaded" + "\n")
            except:
                print('Error, Maybe Duplicate File')
                continue

# link_content = linkFile.write(i.h3.a.text + '\n' +
#                               'https://www.youtube.com' +
#                               i.h3.a['href'] + '\n' + '*' * 50
#                               + '\n\n')

# a_text = i.h3.a.text
# print(a_text)
# link_href = 'https://www.youtube.com' + i.h3.a['href']
# print(link_href)

# for l in linkFile:
#     link_content = linkFile.write(link_href)


if __name__ == '__main__':
    youtube_scraper()
    bulk_load()
