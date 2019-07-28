from sklearn import svm
import numpy as np
from sklearn.neighbors import NearestNeighbors
from sklearn import neighbors
#knn=neighbors.KNeighborsClassifier(n_neighbors=120)
d1={}
ftp=open("E:/F_drive/p3_projects/classifier1/tweeter.txt")
text1=[]
for j in ftp:
    text1.append(j.split("\t"))
for k in range(0,len(text1)):
    d1[text1[k][0]]=int(text1[k][1])
arr=[]
lr_model=svm.SVC()
fp=open("E:/F_drive/p3_projects/classifier1/compare.txt")
d={}
text=[]
x=[]
arr=[]
arr1=[]
pred=[]
for line in fp:
        text.append(line.split("|"))
for j in range(1,len(text)):
    if len(text[j])==7:
       d[text[j][3]]=int(text[j][6])
       arr.append(text[j][3])
arr1=np.array(arr)
x=np.reshape(arr1,(-1,1))
y=d.values()
c=0
for j in d:
    arr2=[]
    count=0
    arr2.append(j.split(" "))
    for k in arr2:
        for l in k:
            for i in d1:
                if l==i:
                   count+=d1[i]
    del arr2
    if count==d[j]:
       c+=1
print("Accuracy=",((float(c)/len(d))*100))
"""#x=d.keys()
#y=d.values()
#knn.fit(x,y)
pred=knn.predict(x)"""
'''test_x=[]
test_y=[]
count=0
train_x=[]
train_y=[]
for i in d:
    if(count<1000):
        test_x.append(i)
        test_y.append(d[i])
    else:
        train_x.append(i)
        train_y.append(d[i])
    count+=1
    if(count==1000):
        break;
lr_model.fit(train_x,train_y)
pred=lr_model.predict(test_x)
print(pred)'''
"""print(d.keys())
print(d.values())"""