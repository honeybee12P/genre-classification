import requests
import validators
import pandas as pd
import bs4
import urlparse
import urllib
from bs4 import BeautifulSoup

def is_absolute(url):
    return bool(urlparse.urlparse(url).netloc)

page = requests.get("http://www.songlyrics.com/musicgenres.php")

soup = BeautifulSoup(page.content,'html.parser')

genre_link = []
for i in soup.find_all(class_='td-item td-text-big'):
    if i.find('a').get('href').encode('utf-8').startswith('http://'):
        continue
    else:
        genre_link.append(tuple([i.get_text().encode('utf-8'),i.find('a').get('href').encode('utf-8')]))

genres = ['Folk','Rock','R&B;','Hip Hop/Rap','Pop','Jazz', 'Country', 'Acoustic', 'Alternative', 'Christian', 'Dance',  'Latin', 'Blues', 'Electronic',
 'Funk', 'Jazz', 'Pop', 'Soul', 'Soundtrack', 'Adult Contemporary','Classical', 'Reggae',  'World','New Age',  'African', 'Ska', 'Avant-Garde', "Children's Music",
 'Holiday',  'Comedy', 'Musical', 'Vocal', 'Instrumental', 'Oldies']


new_genre_link = []
for i in genre_link:
    if(i[0] in genres):
        new_genre_link.append(i)

new_genre_link = new_genre_link[:-3]
new_genre_link[2] = list(new_genre_link[2])
new_genre_link[2][0] = 'R&B'
new_genre_link[2] = tuple(new_genre_link[2])
new_genre_link[3] = list(new_genre_link[3])
new_genre_link[3][0] = 'Hip-Hop'
new_genre_link[3] = tuple(new_genre_link[3])

def song_scrapper():
    song_matrix = []
    for i in new_genre_link:
        genre_page = requests.get('http://www.songlyrics.com/'+i[1])
        soup = BeautifulSoup(genre_page.content,'html.parser')
        album_link = []
        flag = 0
        for table in soup.find_all(class_='tracklist'):
            if(flag==1):
                for j in table.find_all(class_="td-item td-last"):
                    album_link.append(tuple([i[0],j.find_all('span')[-1].get_text().encode('utf-8'),j.find('a').get('title').encode('utf-8'),j.find('a').get('href').encode('utf-8')]))
                    
            flag += 1
        
        for k in album_link:
            req = requests.get(k[:][3])
            pop = BeautifulSoup(req.content,'html.parser')
            table = pop.find(class_='tracklist')
            song_link = []
            for l in table.find_all('tr'):
                if l.find('a') is None:
                    continue
                else:
                    song_link.append(tuple([l.find('a').get('title').encode('utf-8'),l.find('a').get('href').encode('utf-8')]))

            for m in song_link:
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
                    row = []
                    row.append(k[0])
                    row.append(k[:][1])
                    row.append(k[:][2].split('Album')[0])
                    row.append(m[:][0].split('Lyrics')[0])
                    row.append(lyric)
                    song_matrix.append(row)
    return song_matrix

matrix = song_scrapper()

data = pd.DataFrame(matrix,columns=['genre','artist','album','song','lyrics'])

d = data

d = d.drop_duplicates('song')

d.to_csv("/Users/kruthikavishwanath/Documents/Fall 2017/NLP/genre-classification/song.csv", encoding='utf-8', index=False)