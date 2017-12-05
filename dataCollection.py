import requests
import validators
import pandas as pd
import bs4
import urlparse
import urllib
from bs4 import BeautifulSoup

def is_absolute(url):
    return bool(urlparse.urlparse(url).netloc)

songLyrics = requests.get("http://www.songlyrics.com/musicgenres.php")

songLyricsScrapped = BeautifulSoup(songLyrics.content,'html.parser')

genreLink = []
for i in songLyricsScrapped.find_all(class_='td-item td-text-big'):
    if i.find('a').get('href').encode('utf-8').startswith('http://'):
        continue
    else:
        genreLink.append(tuple([i.get_text().encode('utf-8'),i.find('a').get('href').encode('utf-8')]))

genres = ['Folk','Rock','R&B;','Hip Hop/Rap','Pop','Jazz', 'Country', 'Acoustic', 'Alternative', 'Christian', 'Dance',  'Latin', 'Blues', 'Electronic',
 'Funk', 'Jazz', 'Pop', 'Soul', 'Soundtrack', 'Adult Contemporary','Classical', 'Reggae',  'World','New Age',  'African', 'Ska', 'Avant-Garde', "Children's Music",
 'Holiday',  'Comedy', 'Musical', 'Vocal', 'Instrumental', 'Oldies']


genreLinkNew = []
for i in genreLink:
    if(i[0] in genres):
        genreLinkNew.append(i)

genreLinkNew = genreLinkNew[:-3]
genreLinkNew[2] = list(genreLinkNew[2])
genreLinkNew[2][0] = 'R&B'
genreLinkNew[2] = tuple(genreLinkNew[2])
genreLinkNew[3] = list(genreLinkNew[3])
genreLinkNew[3][0] = 'Hip-Hop'
genreLinkNew[3] = tuple(genreLinkNew[3])

def songScrapper():
    songMatrix = []
    for i in genreLinkNew:
        genrePage = requests.get('http://www.songlyrics.com/'+i[1])
        soup = BeautifulSoup(genrePage.content,'html.parser')
        albumLink = []
        flag = 0
        for table in soup.find_all(class_='tracklist'):
            if(flag==1):
                for j in table.find_all(class_="td-item td-last"):
                    albumLink.append(tuple([i[0],j.find_all('span')[-1].get_text().encode('utf-8'),j.find('a').get('title').encode('utf-8'),j.find('a').get('href').encode('utf-8')]))
                    
            flag += 1
        
        for k in albumLink:
            req = requests.get(k[:][3])
            pop = BeautifulSoup(req.content,'html.parser')
            table = pop.find(class_='tracklist')
            songLink = []
            for l in table.find_all('tr'):
                if l.find('a') is None:
                    continue
                else:
                    songLink.append(tuple([l.find('a').get('title').encode('utf-8'),l.find('a').get('href').encode('utf-8')]))

            for m in songLink:
                if(m[:][1][0]=='/'):
                    lyrics = requests.get('http://www.songlyrics.com/'+m[:][1])
                else:
                    lyrics = requests.get(m[:][1])
                lyr = BeautifulSoup(lyrics.content,'html.parser')
                if lyr.find(id='songLyricsDiv') is None:
                    continue
                else:
                    lyric = lyr.find(id='songLyricsDiv').get_text()
                if(len(lyric)>300):
                    eachRow = []
                    eachRow.append(k[0])
                    eachRow.append(k[:][1])
                    eachRow.append(k[:][2].split('Album')[0])
                    eachRow.append(m[:][0].split('Lyrics')[0])
                    eachRow.append(lyric)
                    songMatrix.append(eachRow)
    return songMatrix

songMatrix = songScrapper()

songLyricsData = pd.DataFrame(songMatrix,columns=['genre','artist','album','song','lyrics'])

songLyricsData = songLyricsData.drop_duplicates('song')

songLyricsData.to_csv("/Users/kruthikavishwanath/Documents/Fall 2017/NLP/genre-classification/song.csv", encoding='utf-8', index=False)