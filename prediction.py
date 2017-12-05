import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn import linear_model
from sklearn import svm
import warnings
import sklearn.exceptions
warnings.filterwarnings("ignore", category=sklearn.exceptions.UndefinedMetricWarning)

pos_features = pd.read_csv('/Users/kruthikavishwanath/Documents/Fall 2017/NLP/genre-classification/PosTagsRock.csv')
songs = pd.read_csv('/Users/kruthikavishwanath/Documents/Fall 2017/NLP/genre-classification/clean.csv')
a = pos_features[pos_features.columns.difference(['genre'])]
a  = a.fillna(a.median(axis=0))
print a.max()
pos_features_new = (a - a.min())/(a.max()-a.min())
w2v_features = pd.read_csv('/Users/kruthikavishwanath/Documents/Fall 2017/NLP/genre-classification/w2vDataFinal.csv')

# ####################################################POS-FEATURES#############################################
dataPOS = pd.concat([pos_features_new],axis=1)

dataPOS['genre'] = pos_features.genre

dataPOS = dataPOS.reindex(np.random.permutation(dataPOS.index))
#print dataPOS
train,test,train_y,test_y = train_test_split(np.nan_to_num(dataPOS[dataPOS.columns.difference(['genre'])]),dataPOS['genre'],train_size=0.70) 

gdLM = linear_model.LogisticRegression(C=1e5)
gdLM.fit(train,train_y)
pred = gdLM.predict(test)
print("#####################################################POS FEATURES FEATURES ONLY############################################")
print("Logistic Regression Accuracy", accuracy_score(test_y,pred))
print("Logistic Regression F1 Score",f1_score(test_y,pred, average="macro"))
print("Logistic RegressionPrecision Score", precision_score(test_y, pred, average="macro"))
print("Logistic Regression Recall Score", recall_score(test_y, pred, average="macro"))

gdSVM = svm.SVC()
gdSVM.fit(train,train_y)
pred = gdSVM.predict(test)
print("SVM Accuracy", accuracy_score(test_y,pred))
print("SVM F1 Score",f1_score(test_y,pred, average="macro"))
print("SVM Precision Score", precision_score(test_y, pred, average="macro"))
print("SVM Recall Score", recall_score(test_y, pred, average="macro")) 

gdGB = GradientBoostingClassifier(max_depth=20)
gdGB.fit(train,train_y)
pred = gdGB.predict(test)
print("Gradient Boosting Classifier Accuracy", accuracy_score(test_y,pred))
print("Gradient Boosting Classifier F1 Score",f1_score(test_y,pred, average="macro"))
print("Gradient Boosting Classifier Precision Score", precision_score(test_y, pred, average="macro"))
print("Gradient Boosting Classifier Recall Score", recall_score(test_y, pred, average="macro")) 

gdRF = RandomForestClassifier(max_depth=20)
gdRF.fit(train,train_y)
pred = gdRF.predict(test)
print("Random Forest Classifier Accuracy", accuracy_score(test_y,pred))
print("Random Forest Classifier F1 Score",f1_score(test_y,pred, average="macro"))
print("Random Forest Classifier Precision Score", precision_score(test_y, pred, average="macro"))
print("Random Forest Classifier Recall Score", recall_score(test_y, pred, average="macro")) 


dataPOS.to_csv("/Users/kruthikavishwanath/Documents/Fall 2017/NLP/genre-classification/posOnly.csv",index=False)
# ###########################################################################################################

####################################################Word2vec only#############################################
dataVEC = pd.concat([w2v_features],axis=1)

dataVEC['genre'] = pos_features.genre

dataVEC = dataVEC.reindex(np.random.permutation(dataVEC.index))

train,test,train_y,test_y = train_test_split(np.nan_to_num(dataVEC[dataVEC.columns.difference(['genre'])]),dataVEC['genre'],train_size=0.70) 

print("#####################################################WORD2VEC FEATURES ONLY#####################################################")
gdLM = linear_model.LogisticRegression(C=1e5)
gdLM.fit(train,train_y)
pred = gdLM.predict(test)
print("Logistic Regression Accuracy", accuracy_score(test_y,pred))
print("Logistic Regression F1 Score",f1_score(test_y,pred, average="macro"))
print("Logistic RegressionPrecision Score", precision_score(test_y, pred, average="macro"))
print("Logistic Regression Recall Score", recall_score(test_y, pred, average="macro"))

gdSVM = svm.SVC()
gdSVM.fit(train,train_y)
pred = gdSVM.predict(test)
print("SVM Accuracy", accuracy_score(test_y,pred))
print("SVM F1 Score",f1_score(test_y,pred, average="macro"))
print("SVM Precision Score", precision_score(test_y, pred, average="macro"))
print("SVM Recall Score", recall_score(test_y, pred, average="macro")) 

gdGB = GradientBoostingClassifier(max_depth=20)
gdGB.fit(train,train_y)
pred = gdGB.predict(test)
print("Gradient Boosting Classifier Accuracy", accuracy_score(test_y,pred))
print("Gradient Boosting Classifier F1 Score",f1_score(test_y,pred, average="macro"))
print("Gradient Boosting Classifier Precision Score", precision_score(test_y, pred, average="macro"))
print("Gradient Boosting Classifier Recall Score", recall_score(test_y, pred, average="macro")) 

gdRF = RandomForestClassifier(max_depth=20)
gdRF.fit(train,train_y)
pred = gdRF.predict(test)
print("Random Forest Classifier Accuracy", accuracy_score(test_y,pred))
print("Random Forest Classifier F1 Score",f1_score(test_y,pred, average="macro"))
print("Random Forest Classifier Precision Score", precision_score(test_y, pred, average="macro"))
print("Random Forest Classifier Recall Score", recall_score(test_y, pred, average="macro")) 


dataVEC.to_csv("/Users/kruthikavishwanath/Documents/Fall 2017/NLP/genre-classification/vecOnly.csv",index=False)
###########################################################################################################


####################################################pos+Word2vec only#############################################
dataPV = pd.concat([pos_features,w2v_features],axis=1)

dataPV['genre'] = pos_features.genre

dataPV = dataPV.reindex(np.random.permutation(dataPV.index))

train,test,train_y,test_y = train_test_split(np.nan_to_num(dataPV[dataPV.columns.difference(['genre'])]),dataPV['genre'],train_size=0.70) 

gdLM = linear_model.LogisticRegression(C=1e5)
gdLM.fit(train,train_y)
pred = gdLM.predict(test)
print("#####################################################POS FEATURES + WORD2VEC FEATURES#####################################################")
print("Logistic Regression Accuracy", accuracy_score(test_y,pred))
print("Logistic Regression F1 Score",f1_score(test_y,pred, average="macro"))
print("Logistic RegressionPrecision Score", precision_score(test_y, pred, average="macro"))
print("Logistic Regression Recall Score", recall_score(test_y, pred, average="macro"))

gdSVM = svm.SVC()
gdSVM.fit(train,train_y)
pred = gdSVM.predict(test)
print("SVM Accuracy", accuracy_score(test_y,pred))
print("SVM F1 Score",f1_score(test_y,pred, average="macro"))
print("SVM Precision Score", precision_score(test_y, pred, average="macro"))
print("SVM Recall Score", recall_score(test_y, pred, average="macro")) 

gdGB = GradientBoostingClassifier(max_depth=20)
gdGB.fit(train,train_y)
pred = gdGB.predict(test)
print("Gradient Boosting Classifier Accuracy", accuracy_score(test_y,pred))
print("Gradient Boosting Classifier F1 Score",f1_score(test_y,pred, average="macro"))
print("Gradient Boosting Classifier Precision Score", precision_score(test_y, pred, average="macro"))
print("Gradient Boosting Classifier Recall Score", recall_score(test_y, pred, average="macro")) 

gdRF = RandomForestClassifier(max_depth=20)
gdRF.fit(train,train_y)
pred = gdRF.predict(test)
print("Random Forest Classifier Accuracy", accuracy_score(test_y,pred))
print("Random Forest Classifier F1 Score",f1_score(test_y,pred, average="macro"))
print("Random Forest Classifier Precision Score", precision_score(test_y, pred, average="macro"))
print("Random Forest Classifier Recall Score", recall_score(test_y, pred, average="macro")) 


dataPV.to_csv("/Users/kruthikavishwanath/Documents/Fall 2017/NLP/genre-classification/vecOnly.csv",index=False)
###########################################################################################################


