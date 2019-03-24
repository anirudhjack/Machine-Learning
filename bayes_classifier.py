#The following program is in python3
import numpy as np
import scipy as sp
import csv
import math
#Enter the test vectors
print("Enter the test vectors:")
x1=int(input())
x2=int(input())
#read the csv files
with open('Y.csv') as yfile:
    ycsv=csv.reader(yfile)
    ycsv=list(ycsv)
#csv file to array
for i in range(len(ycsv)):
    ycsv[i]=[float(j) for j in ycsv[i]]
y=ycsv
y=np.transpose(y)

#read the csv files
with open('X.csv') as xfile:
    xcsv=csv.reader(xfile)
    xcsv=list(xcsv)
#csv file to array
for i in range(len(xcsv)):
    xcsv[i]=[float(j) for j in xcsv[i]]
x=xcsv

#merge three arrays
g=np.vstack((x,y))
g=np.transpose(g)
#declare means
mean11=0
mean21=0
mean12=0
mean22=0
#n1->no of y with value 1,n2->no of y with value -1
n1=0
n2=0
#calculating the means
for i in range(1000):
    if g[i][2]==1:
        n1=n1+1
        mean11=mean11+g[i][0]
        mean21=mean21+g[i][1]
    else:
        n2=n2+1
        mean12=mean12+g[i][0]
        mean22=mean22+g[i][1]

mean11=mean11/n1
mean12=mean12/n1
mean21=mean21/n2
mean22=mean22/n2

#declaring variances
var11=0
var21=0
var12=0
var22=0

#calculating the variances
for i in range(1000):
    if g[i][2]==1:
        var11=var11+(g[i][0]-mean11)**2
        var21=var21+(g[i][1]-mean21)**2
    else:
        var12=var12+(g[i][0]-mean12)**2
        var22=var22+(g[i][1]-mean22)**2

var11=var11/n1
var21=var21/n1
var12=var12/n2
var22=var22/n2
#calculating the posterior probabilities
exp11=-((x1-mean11)**2)/(2*var11)
exp21=-((x2-mean21)**2)/(2*var21)
exp12=-((x1-mean12)**2)/(2*var12)
exp22=-((x2-mean22)**2)/(2*var22)

y11=(1/np.sqrt(2*math.pi*(var11)))*((math.e)**exp11)
y21=(1/np.sqrt(2*math.pi*(var21)))*((math.e)**exp21)
y12=(1/np.sqrt(2*math.pi*(var12)))*((math.e)**exp12)
y22=(1/np.sqrt(2*math.pi*(var22)))*((math.e)**exp22)

#calculating the likelihood probabilities
p1=(y11*y21)*(n1/(n1+n2))
p2=(y12*y22)*(n2/(n1+n2))
#comparing the likelihood probabilities
if p1>p2:
    print("This test vector belongs to 1")
else :
    print("This test vector belongs to -1")
