#importing all the required libraries

from sklearn import svm
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split as t_split

#reading the csv file from wine.csv

wine=pd.read_csv("wine.csv")
#importing standard scaler and PCA
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
#preparing data to make x and y
x=wine.iloc[:,1:].values
y=wine.iloc[:,0:1].values
scaler=StandardScaler()

#scaling the data of x using the fit transform

scaled_data=scaler.fit_transform(x)
#reducing the data to two columns only i.e. represented by principle components

sklearn_pca=PCA(n_components='mle')

reduced_data=sklearn_pca.fit_transform(x)
#preparing the x_train,x_test,y_train and y_test 
x_train,x_test,y_train,y_test=t_split(reduced_data,y,test_size=0.2)
#applying svm over the wine dataset
lr=svm.SVC(kernel='linear')
lr.fit(x_train,y_train)
#predicting over the wine dataset
pred=lr.predict(x_test)

from sklearn import metrics

#calculating the model accuracy
print("Accuracy:",metrics.accuracy_score(y_test, pred)*100)

#plotting the wine dataset elements values
color=['r','g','b']
plt.scatter(reduced_data[:,0],reduced_data[:,1],label='wine dataset plot',c=color)
plt.title("PCA implementation")
plt.legend()
plt.show()

#printing the classification report and confusion_matrix
from sklearn.metrics import classification_report,confusion_matrix
print(confusion_matrix(y_test,pred))
print(classification_report(y_test,pred))


