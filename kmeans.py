import numpy as np
import matplotlib.pyplot as plt
import random as rd
train=[]
c1=[]
c2=[]
c3=[]
for i in range(30):
	r=[]
	a=rd.uniform(1,10)
	b=rd.uniform(1,10)
	r.append(a)
	r.append(b)
	train.append(r)
rd.seed(0)
x1=rd.uniform(1,10)
y1=rd.uniform(1,10)
c1.append(x1)
c1.append(y1)
x2=rd.uniform(1,10)
y2=rd.uniform(1,10)
c2.append(x2)
c2.append(y2)
x3=rd.uniform(1,10)
y3=rd.uniform(1,10)
c3.append(x3)
c3.append(y3)
q1=[]
q2=[]
q3=[]
sum1=0
sum2=0
for k in range(100):
	p1=[]
	p2=[]
	p3=[]
	for i in range(len(train)):
		#comparing the distances
		d1=(c1[0]-train[i][0])**2+(c1[1]-train[i][1])**2
		d2=(c2[0]-train[i][0])**2+(c2[1]-train[i][1])**2
		d3=(c3[0]-train[i][0])**2+(c3[1]-train[i][1])**2
		if min(d1,d2,d3)==d1:
			p1.append(train[i])
		elif min(d1,d2,d3)==d2:
			p2.append(train[i])
		else:
			p3.append(train[i])
		
	#update centroid1:
	for j in range(len(p1)):
		sum1=sum1+p1[j][0]
	c1[0]=sum1/len(p1)
	sum1=0
	for j in range(len(p1)):
		sum2=sum2+p1[j][1]
	c1[1]=sum2/len(p1)
	sum2=0
	#update centroid2:
	for j in range(len(p2)):
		sum1=sum1+p2[j][0]
	c2[0]=sum1/len(p2)
	sum1=0
	for j in range(len(p2)):
		sum2=sum2+p2[j][1]
	c2[1]=sum2/len(p2)
	sum2=0
	#update centriod3:
	for j in range(len(p3)):
		sum1=sum1+p3[j][0]
	c3[0]=sum1/len(p3)
	sum1=0
	for j in range(len(p3)):
		sum2=sum2+p3[j][1]
	c3[1]=sum2/len(p3)
	sum2=0
	if k==99:
		q1=p1
		q2=p2
		q3=p3


clx1=[]
cly1=[]
clx2=[]
cly2=[]
clx3=[]
cly3=[]

for j in range(len(q1)):
	clx1.append(q1[j][0])
for j in range(len(q1)):
	cly1.append(q1[j][1])
for j in range(len(q2)):
	clx2.append(q2[j][0])
for j in range(len(p2)):
	cly2.append(q2[j][1])
for j in range(len(q3)):
	clx3.append(q3[j][0])
for j in range(len(q3)):
	cly3.append(q3[j][1])
	
plt.scatter(clx1,cly1,c='orange')
plt.scatter(clx2,cly2,c='red')
plt.scatter(clx3,cly3,c='k')
plt.scatter(c1[0],c1[1],c='orange',marker='*')
plt.scatter(c2[0],c2[1],c='red',marker='*')
plt.scatter(c3[0],c3[1],c='k',marker='*')
plt.show()



