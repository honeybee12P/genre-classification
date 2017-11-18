import requests
import validators
import pandas as pd
import bs4
from bs4 import BeautifulSoup

page = requests.get("http://www.songlyrics.com/musicgenres.php")

soup = BeautifulSoup(page.content,'html.parser')

genre_link = []
for i in soup.find_all(class_='td-item td-text-big'):
    genre_link.append(tuple([i.get_text().encode('utf-8'),i.find('a').get('href').encode('utf-8')]))


genres = ['Folk','Rock','R&B;','Hip Hop/Rap','Pop','Jazz']

#print genre_link

new_genre_link = []
for i in genre_link:
    if(i[0] in genres):
        new_genre_link.append(i)

new_genre_link = new_genre_link[:-3]

#print new_genre_link

pop_page = requests.get("http://www.songlyrics.com/pop-lyrics.php")

new_genre_link[2] = list(new_genre_link[2])
new_genre_link[2][0] = 'R&B'
new_genre_link[2] = tuple(new_genre_link[2])
new_genre_link[3] = list(new_genre_link[3])
new_genre_link[3][0] = 'Hip-Hop'
new_genre_link[3] = tuple(new_genre_link[3])

#print new_genre_link

soup = BeautifulSoup(pop_page.content,'html.parser')

album_link = []
flag = 0
for table in soup.find_all(class_='tracklist'):
    if(flag==1):
        for i in table.find_all(class_="td-item td-last"):
            print (i)
            print ('\n')
            album_link.append(tuple(['pop',i.find_all('span')[-1].get_text().encode('utf-8'),i.find('a').get('title').encode('utf-8'),i.find('a').get('href').encode('utf-8')]))
    flag += 1


#print album_link

# album_link[0][2].split('Album')[0].replace(' ','')

# req = requests.get(album_link[0][3])

# pop = BeautifulSoup(req.content, 'html.parser')

# song_link = []
# table = pop.find(class_='tracklist')

# for i in table.find_all('tr'):
#     song_link.append(tuple([i.find('a').get('title'),i.find('a').get('href')]))

# song_link[1][0].split('Lyrics')[0]

# #print song_link

# firstlyrics = requests.get(song_link[0][1])

# lyrics = BeautifulSoup(firstlyrics.content, 'html.parser')

# lyric = lyrics.find(id='songLyricsDiv').get_text()

# #print lyric

# pop_matrix = []
# for i in album_link:
#     req = requests.get(i[:][3])
#     pop = BeautifulSoup(req.content,'html.parser')
#     table = pop.find(class_='tracklist')
#     song_link = []
#     for k in table.find_all('tr'):
#         song_link.append(tuple([k.find('a').get('title'),k.find('a').get('href')]))
#     for l in song_link:
#         lyrics = requests.get(l[:][1])
#         print l[1]
#         # if validators.url(l[:][1]) == True:
# 	       #  lyr = BeautifulSoup(lyrics.content,'html.parser')
# 	       #  lyric = lyr.find(id='songLyricsDiv').get_text()
# 	       #  if(len(lyric)>300):
# 	       #      row = []
# 	       #      row.append('pop')
# 	       #      row.append(i[:][1])
# 	       #      row.append(i[:][2].split('Album')[0])
# 	       #      row.append(l[:][0].split('Lyrics')[0])
# 	       #      row.append(lyric)
# 	       #      pop_matrix.append(row)



# #pop_d = pd.DataFrame(pop_matrix,columns=['Genre','Artist','Album','Song','Lyrics'])

# #print pop_d