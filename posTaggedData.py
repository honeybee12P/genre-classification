import pandas as pd
import nltk
import numpy as np
from collections import Counter
from collections import defaultdict

songs = pd.read_csv('/Users/kruthikavishwanath/Documents/Fall 2017/NLP/genre-classification/clean.csv')
corpus = songs
#HipHop = songs['lyrics']
#LyricsHipHop= list(HipHop.lyrics)
#corpus= list(HipHop)
#print songs

# HipHop = songs[songs['genre']] 
# LyricsHipHop=list(HipHop.lyrics)
# #print LyricsHipHop
# corpus = (LyricsHipHop)

# Pop = songs[songs['genre']=='Pop'] 
# LyricsPop=list(Pop.lyrics)
# corpus.append(LyricsPop)


# Rock = songs[songs['genre']=='Rock'] 
# LyricsRock=list(Rock.lyrics)

# corpus.append(LyricsRock)

# Christian = songs[songs['genre']=='Christian'] 
# LyricsChristian=list(Christian.lyrics)
# corpus.append(LyricsChristian)

# HipHopRap = songs[songs['genre']=='Hip Hop/Rap'] 
# LyricsHipHopRap =list(HipHopRap.lyrics)
# corpus.append(LyricsHipHopRap)


# Dance = songs[songs['genre']=='Dance'] 
# LyricsDance =list(Dance.lyrics)
# corpus.append(LyricsDance)

#print corpus
tags=[]
# Pop
# Rock
# Christian
# Hip Hop/Rap
# Dance
#print corpus
#print type(corpus)
for each in corpus.iterrows():
	#print each[1].lyrics
	text = nltk.word_tokenize(each[1].lyrics)
	t = nltk.pos_tag(text)
	if each[1].genre == 'Hip-Hop':
		t.append((0, 'genre'))
		tags.append(t)
	if each[1].genre == 'Pop':
		t.append((1, 'genre'))
		tags.append(t)
	if each[1].genre == 'Rock':
		t.append((2, 'genre'))
		tags.append(t)
	if each[1].genre == 'Christian':
		t.append((3, 'genre'))
		tags.append(t)
	if each[1].genre == 'Hip Hop/Rap':
		t.append((4, 'genre'))
		tags.append(t)
	if each[1].genre == 'Dance':
		t.append((5, 'genre'))
		tags.append(t)

	#tags.append(  tuple([each[1].genre ,nltk.pos_tag(text)]))

#print tags[0]
#print tags

z=[]

for each in tags:
	
	genre = 0
	for tag in each:
		if tag[1] == 'genre':
			genre = tag[0]
	counts = Counter(tag[1] for tag in each if tag[1] != 'genre')
	counts.update({'genre' : genre})
	#print counts
	z.append(dict(counts))
# 	#z.update( {each[0] : dict(counts)})

#print z
PosTags = {}
for i in range (0,len(z)):
	PosTags[i] = z[i]
# print PosTags
dt=pd.DataFrame.from_dict(PosTags, orient="index")
dt.to_csv("/Users/kruthikavishwanath/Documents/Fall 2017/NLP/genre-classification/PosTagsRock1.csv")
