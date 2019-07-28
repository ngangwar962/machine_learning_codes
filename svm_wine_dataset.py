#importing all the required libraries

from sklearn import svm
import pandas as pd
from sklearn import datasets
import numpy as np
from sklearn.model_selection import train_test_split as t_split

#reading the dataset from the csv the file wine.csv

wine=pd.read_csv("wine.csv")

#fetching data into the x and y variables 
#where x contains the data and y contains the targer variables

x=wine.iloc[:,1:].values
y=wine.iloc[:,0:1].values

#splitting the data in test and train data 

x_train,x_test,y_train,y_test=t_split(x,y,test_size=0.20)

#applying svm over the dataset

lr=svm.SVC(kernel='linear')

#fitting the data into the model
lr.fit(x_train,y_train)

#predicting over the test data

pred=lr.predict(x_test)
from sklearn import metrics
print("Accuracy=",metrics.accuracy_score(y_test,pred)*100)


