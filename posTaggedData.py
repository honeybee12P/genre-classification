import pandas as pd
import nltk
import numpy as np
from collections import Counter
from collections import defaultdict

songs = pd.read_csv('/Users/kruthikavishwanath/Documents/Fall 2017/NLP/genre-classification/clean.csv')
corpus = songs

tags=[]

for each in corpus.iterrows():
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

z=[]

for each in tags:
	
	genre = 0
	for tag in each:
		if tag[1] == 'genre':
			genre = tag[0]
	counts = Counter(tag[1] for tag in each if tag[1] != 'genre')
	counts.update({'genre' : genre})
	z.append(dict(counts))

PosTags = {}
for i in range (0,len(z)):
	PosTags[i] = z[i]

dt=pd.DataFrame.from_dict(PosTags, orient="index")

dt.to_csv("/Users/kruthikavishwanath/Documents/Fall 2017/NLP/genre-classification/PosTagsRock.csv")