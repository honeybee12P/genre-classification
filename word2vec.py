import gensim
import pandas as pd
import nltk
import numpy as np
from nltk.corpus import brown
songs = pd.read_csv('/Users/kruthikavishwanath/Documents/Fall 2017/NLP/genre-classification/clean.csv')
Lyrics=list(songs['lyrics'])

corpus=(Lyrics)

sentencesData=[] 
Tokens=[]
for i in range(len(corpus)):
    g=corpus[i].split()
    sentencesData.append(set(g))
    Tokens.append((g))
sentencesBrown = brown.sents()   
for i in range(len(sentencesBrown)):
    sentencesData.append(set(sentencesBrown[i]))


model = gensim.models.Word2Vec(sentencesData, size=50,window=5,min_count=5)

vocab=model.wv.vocab
vocab=(set(vocab))

word2vecTokens=[] 
i=0;
for g in Tokens: 
    vc=[] 
    for s in g:
        if (s in vocab):
            vc.append(model.wv[s])
    word2vecTokens.append(vc) 

g=[]
for i in range (len(word2vecTokens)):
    g.append(np.sum(word2vecTokens[i], axis=0)/len(word2vecTokens[i]))

columns=[]
index=[]
for k in range(0,80000):
    index.append(k)
for i in range(1,51):
    columns.append("w2v_"+str(i))
df_ = pd.DataFrame(columns=columns)
df_ = df_.fillna(0)

for x in range (len(g)):
    try:
        if(type(g[x])==float):
            g[x]=[0]*50
        g[x]=g[x].tolist()
    except:
        print(x)

for x in range (len(g)):
    try:
        if(type(g[x])==float):
            g[x]=[0]*50
    except:
        print(x)
dar=pd.DataFrame(g,columns=columns)
dar.head()

dar.to_csv("/Users/kruthikavishwanath/Documents/Fall 2017/NLP/genre-classification/w2vDataFinal.csv",index=False)