import pandas as pd
import nltk as nk
import numpy as np
import ftfy
import nltk
import re
from nltk.corpus import stopwords

metro_lyrics = pd.read_csv("/Users/kruthikavishwanath/Documents/Fall 2017/NLP/genre-classification/metrolyrics_songs.csv")
song_lyrics = pd.read_csv("/Users/kruthikavishwanath/Documents/Fall 2017/NLP/genre-classification/song.csv", encoding='utf8', engine='python')
del (song_lyrics['album'])
whole_data = metro_lyrics.append(song_lyrics)
data = pd.DataFrame(whole_data,columns=['genre','artist','song','lyrics'])

for index, row in data.iterrows():
    if row['lyrics'] is None or row['song'] is None or row['genre'] == 'Latin' :
        data.drop(index, inplace=True)

def StopStem(df):
	stop = set(stopwords.words('english'))	
	df['lyrics'] = df['lyrics'].apply( lambda x: ' '.join([word for word in x.split() if word not in (stop)]))
	df["lyrics"] = df['lyrics'].str.replace('[^\w\s]','')
	return df

songs = StopStem(data)

 

def remove_brackets(text):
    new_text = re.sub(r'\(.*?\)','',text)
    new_text = re.sub(r'\[.*?\]','',text)
    return new_text


def ReBr(df):
        df['lyrics'] = df['lyrics'].apply(remove_brackets)
        return df

def Chorus(df):
    words = ['Chorus','Verse1','Verse2','Verse']
    df['lyrics'] = df['lyrics'].apply(lambda x: ' '.join([word for word in x.split() if word not in words]))
    return df


songs = ReBr(songs)
songs = Chorus(songs)

songs.to_csv("/Users/kruthikavishwanath/Documents/Fall 2017/NLP/genre-classification/clean.csv", encoding='utf-8', index=False)
