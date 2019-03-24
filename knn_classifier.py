#The following program is in python3
import numpy as np
import scipy as sp
import csv
import math
#Enter the test vectors
print("Enter the test vectors:")
x1=int(input())
x2=int(input())

#Enter the value of K
print("Enter the value of K")
k=int(input())

#read the csv files
with open('Y.csv') as yfile:
    ycsv=csv.reader(yfile)
    ycsv=list(ycsv)

#csv file to array
for i in range(len(ycsv)):
    ycsv[i]=[float(j) for j in ycsv[i]]
y=ycsv
y=np.transpose(y)
y=y[0]

#read the csv files
with open('X.csv') as xfile:
    xcsv=csv.reader(xfile)
    xcsv=list(xcsv)

#csv file to array
for i in range(len(xcsv)):
    xcsv[i]=[float(j) for j in xcsv[i]]
x=xcsv

#declaring the list of distances(unsorted)
distance_list=[]
#listing the Euclidean distance
for i in range(1000):
    s=(x1-x[0][i])**2+(x2-x[1][i])**2
    s=np.sqrt(s)
    distance_list.append(s)

#defining swap function
def swap(arr,j):
    arr[j],arr[j+1]=arr[j+1],arr[j]

#defining bubble sort function
def sort(distance_list):
    for i in range(1000):
        for j in range(0,999-i):
            if distance_list[j]>distance_list[j+1]:
                swap(distance_list,j)
                swap(y,j)

sort(distance_list)
p=0

for i in range(k):
    if y[i]==1.00:
            p=p+1
    else:
          p=p-1

#comparing the values of p
if p>=0:
     print("test vector belongs to class 1")
else :
     print("test vector belongs to class -1")
