import requests
import pandas as pd
from bs4 import BeautifulSoup

page = requests.get("http://www.metrolyrics.com/artists-1.html")
soup = BeautifulSoup(page.content,'html.parser')

page_link = []
page_link.append("http://www.metrolyrics.com/artists-1.html")
p = True
while p:
	p_link = soup.find(class_='pagination')
	try:
		li = p_link.find_all('a')[-1].get('href')
	except:
		break

	try:
		page = requests.get(li)
		soup = BeautifulSoup(page.content,'html.parser')
		page_link.append(li)
	except:
		break

data = []
for i in page_link:
    page = requests.get("%s"%i)
    soup = BeautifulSoup(page.content,'html.parser')
    song_data = soup.find(class_='songs-table')
    tbodys = song_data.find('tbody')
    for i in tbodys.find_all('tr'):
        data.append(tuple([i.find('td').find('a').get('href').encode('utf-8'),i.find('td').find('a').get_text().replace(" Lyrics","").encode('utf-8'),i.find_all('td')[-2].get_text().encode('utf-8')]))


new_data = []
for i in data:
    if(i[2]!='Other' and i[2]!=''):
        new_data.append(i)


from collections import Counter
c = Counter()
li = []
for i in new_data:
    li.append(i[2])
c.update(li)

#print c

data = []
for i in new_data:
	if(i[2] in ['Hip-Hop','Pop','Rock','Electronic','Metal','R&B']):
		data.append(i)


for i in data:
    print i

song_data = []
for i in range(0,5):
	page = requests.get(data[i][0])
	soup = BeautifulSoup(page.content,'html.parser')
	table = soup.find(class_='songs-table compact')
	t_body = table.find('tbody')
	for j in t_body.find_all('tr'):
		row = []
		row.append(j.find_all('td')[1].find('a').get('href'))
		row.append(data[i][1])
		row.append(j.find_all('td')[1].find('a').get_text().split('Lyrics')[0].replace('\n','').rstrip())
		row.append(data[i][2])
		song_data.append(row)

#print song_data[0]

lyrics_data = []
for i in song_data:
	row = []
	page = requests.get(i[0])
	soup = BeautifulSoup(page.content,'html.parser')
	lyrics = soup.find(id='lyrics-body-text')
	row.append(i[3])
	row.append(i[1])
	row.append(i[2])
	row.append(lyrics.get_text().strip('\n'))
	
	lyrics_data.append(row)

print len(lyrics_data)

df = pd.DataFrame(lyrics_data,columns=['genre','artist','song','lyrics'])


df.to_csv("/Users/kruthikavishwanath/Documents/Fall 2017/NLP/genre-classification/metrolyrics_songs.csv", encoding='utf-8', index=False)

