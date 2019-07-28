from sklearn import svm
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
from sklearn import neighbors
from sklearn.neighbors import NearestNeighbors
ftp=open("E:/F_drive/p3_projects/classifier1/compare.txt")
text=[]
arrx=[]
arry=[]
pred=[]
pred1=[]
for line in ftp:
    text.append(line.split("|"))
for j in range(1,2500):
    if len(text[j])==7:
       arrx.append(text[j][3])
       arry.append(int(text[j][6]))
bow=CountVectorizer()
matrix=bow.fit_transform(arrx)
mat=matrix.todense()
knn=neighbors.KNeighborsClassifier(n_neighbors=3)
knn.fit(mat,arry)
pred=knn.predict(mat)
correct=0
for i in range(0,len(pred)):
    if pred[i]==arry[i]:
        correct+=1
print("accuracy using knn =",((float(correct)/len(pred))*100))
lr_model=svm.SVC()
lr_model.fit(mat,arry)
pred1=lr_model.predict(mat)
print(len(pred1))
c=0
for i in range(0,len(pred1)):
    if pred1[i]==arry[i]:
       c+=1
print("accuracy using svm =",((float(c)/len(pred1))*100))

"""x=matrix
knn.fit(x,arry)
pred=knn.predict(x)
print(x)"""
"""arr1=np.array(arr)
x=np.reshape(arr1,(-1,1))
y=d.values()
bagx=[]
bagy=[]
bow=CountVectorizer()
for j in range(0,500):
bagx.append(x[j])"""
"""if d[j]>=1:
         bagy.append(int(1))
    else:
         bagy.append(int(0))"""
#matrix=bow.fit_transform(arr1[j] for j in range(0,500))
"""matrix=bow.fit_transform(arrx)
mat=matrix.todense()
print(mat)
print(mat.shape)
lr_model.fit(mat,bagy)
#print(bow.vocabulary_.keys())
pred=lr_model.predict(bagx)
print(pred)
print(pred.shape)
#pred=lr_model.predict(mat)
c=0"""
"""for j in d:
    arr2=[]
    count=0
    arr2.append(j.split(" "))
    for k in arr2:
        for l in k:
            for i in d1:
                if l==i:
                   a=np.array(d1[i])
    del arr2
    if count==d[j]:
       print(count,"->",d[j])
       c+=1
print("Accuracy=",((float(c)/len(d))*100))"""
"""#x=d.keys()
#y=d.values()
#knn.fit(x,y)
#pred=knn.predict(x)
lr_model.fit(d.keys(),d.values())"""



