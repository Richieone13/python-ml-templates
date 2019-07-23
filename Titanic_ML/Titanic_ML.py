# -*- coding: utf-8 -*-
#"""
#Created on Fri May 17 16:21:34 2019

#@author: RWong
#"""

import pandas as pd

train = pd.read_csv("train.csv")


#Cleaning the data
def add_age(cols):
    Age = cols[0]
    Pclass = cols[1]
    if pd.isnull(Age):
        return int(train[train["Pclass"] == Pclass]["Age"].mean())
    else:
        return Age
    
    
train["Age"] = train[["Age", "Pclass"]].apply(add_age,axis=1)

train.drop("Cabin",inplace=True,axis=1)

train.dropna(inplace=True)

pd.get_dummies(train["Sex"])

sex = pd.get_dummies(train["Sex"],drop_first=True)

embarked = pd.get_dummies(train["Embarked"],drop_first=True)
pclass = pd.get_dummies(train["Pclass"],drop_first=True)

train = pd.concat([train,pclass,sex,embarked],axis=1)

#Remove the columns in the trained database
train.drop(["PassengerId","Pclass","Name","Sex","Ticket","Embarked"],axis=1,inplace=True)

#Now we can start the Algorithm ML
X = train.drop("Survived",axis=1)
y = train["Survived"]

from sklearn.model_selection import train_test_split #Check if these modules change
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 101)

from sklearn.linear_model import LogisticRegression
logmodel = LogisticRegression()
logmodel.fit(X_train,y_train)

predictions = logmodel.predict(X_test)
from sklearn.metrics import classification_report
print(classification_report(y_test, predictions))


from sklearn.metrics import confusion_matrix
print(confusion_matrix(y_test, predictions))



