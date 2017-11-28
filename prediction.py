import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

pos_features = pd.read_csv('/Users/kruthikavishwanath/Documents/Fall 2017/NLP/genre-classification/PosTagsRock1.csv')
songs = pd.read_csv('/Users/kruthikavishwanath/Documents/Fall 2017/NLP/genre-classification/clean.csv')
#print pos_features.columns.difference(['genre'])
a = pos_features[pos_features.columns.difference(['genre'])]
#a.replace('?', np.NaN)
#a = a.fillna(0)


a  = a.fillna(a.median(axis=0))

#print a



pos_features_new = (a - a.mean())/(a.max()-a.min())
#print songs.head()
#print pos_features_new
w2v_features = pd.read_csv('/Users/kruthikavishwanath/Documents/Fall 2017/NLP/genre-classification/w2vDataFinal.csv')

data = pd.concat([w2v_features,pos_features_new],axis=1)

data['genre'] = pos_features.genre
#print data['genre']
data = data.reindex(np.random.permutation(data.index))

#print data

train,test,train_y,test_y = train_test_split(np.nan_to_num(data[data.columns.difference(['genre'])]),data['genre'],train_size=0.67)

# train = train.fillna(train.mean())
# test = test.fillna(test.mean())

# train = train.values.reshape(train.size,1)
# train = train.astype(np.float64, copy=False)

# test = test.values.reshape(test.size,1)
# test = test.astype(np.float64, copy=False)

# train_y = train_y.values.reshape(train_y.size,1)
# train_y = train_y.astype(np.float64, copy=False)

# test_y = test_y.values.reshape(test_y.size,1)
# test_y = test_y.astype(np.float64, copy=False)

#print train

print np.isnan(train).any()
print np.isnan(test).any() 
print np.isnan(train_y).any()
print np.isnan(test_y).any()
#from collections import Counter
#c = Counter()
#c.update(train_y)

#print train_y

from sklearn.ensemble import GradientBoostingClassifier

gd = GradientBoostingClassifier(max_depth=20)
gd.fit(train,train_y)
pred = gd.predict(test)
print (accuracy_score(test_y,pred))

data.to_csv("/Users/kruthikavishwanath/Documents/Fall 2017/NLP/genre-classification/combined.csv",index=False)