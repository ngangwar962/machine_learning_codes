from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import svm
import numpy as np
ftp=open("E:/F_drive/p3_projects/classifier1/compare.txt")
x=[]
y=[]
arr=[]
arr1=[]
res=[]
arrt=[]
d={}
m={}
for line in ftp:
    arr.append(line.split("|"))
for j in range(1,len(arr)):
    if len(arr[j])==7:
       x.append(arr[j][3])
       y.append(int(arr[j][6]))
vectorizer=TfidfVectorizer()
matrix=vectorizer.fit_transform(x)
mat=matrix.todense()
print(len(x))
"""for i in range(0,len(x)):
    d=0
    st=str(mat[i])
    st.append(str(mat[i].split()))
    for i in st:
        d+=float(i)
    res.append(d)
print(res)"""
"""print(len(st))"""
for j in range(0,len(mat)):
    c=0
    m1=matrix[j, :].toarray()
    for i in range(0,13937):
        c+=m1[0][i]
    d[c]=x[j]
m=sorted(d)
p=m[0:32]
st=""
for j in p:
    for k in d:
        if j==k:
            st=st+d[k]
print(st)
#for j in range(0,len(matrix)):
    