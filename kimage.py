import cv2
import numpy as np
import matplotlib.pyplot as plt
import random as rd
image =cv2.imread("example17.png")
#generating random centriods
c1=[]
c2=[]
c3=[]
x1=rd.uniform(1,200)
y1=rd.uniform(1,200)
z1=rd.uniform(1,200)
c1.append(x1)
c1.append(y1)
c1.append(z1)
x2=rd.uniform(1,200)
y2=rd.uniform(1,200)
z2=rd.uniform(1,200)
c2.append(x2)
c2.append(y2)
c2.append(z2)
x3=rd.uniform(1,200)
y3=rd.uniform(1,200)
z3=rd.uniform(1,200)
c3.append(x3)
c3.append(y3)
c3.append(z3)
q1=[]
q2=[]
q3=[]
sum1=0
sum2=0
sum3=0
for k in range(10):
	p1=[]
	p2=[]
	p3=[]
	for i in range(np.shape(image)[0]):
		for j in range(np.shape(image)[1]):
			#comparing the distances
			d1=(c1[0]-image[i][j][0])**2+(c1[1]-image[i][j][1])**2+(c1[2]-image[i][j][2])**2
			d2=(c2[0]-image[i][j][0])**2+(c2[1]-image[i][j][1])**2+(c2[2]-image[i][j][2])**2
			d3=(c3[0]-image[i][j][0])**2+(c3[1]-image[i][j][1])**2+(c3[2]-image[i][j][2])**2
			if min(d1,d2,d3)==d1:
				image[i][j]
				p1.append(image[i][j])
			elif min(d1,d2,d3)==d2:
				p2.append(image[i][j])
			elif min(d1,d2,d3)==d3:
				p3.append(image[i][j])
	#update centroid1:
	if len(p1)!=0:
		for o in range(len(p1)):
			sum1=sum1+p1[o][0]
		c1[0]=sum1/len(p1)
		sum1=0
		for o in range(len(p1)):
			sum2=sum2+p1[o][1]
		c1[1]=sum2/len(p1)
		sum2=0
		for o in range(len(p1)):
			sum3=sum3+p1[o][2]
		c1[2]=sum3/len(p1)
		sum3=0
	#update centroid2:
	if len(p2)!=0:
		for o in range(len(p2)):
			sum1=sum1+p2[o][0]
		c2[0]=sum1/len(p2)
		sum1=0
		for o in range(len(p2)):
			sum2=sum2+p2[o][1]
		c2[1]=sum2/len(p2)
		sum2=0
		for o in range(len(p2)):
			sum3=sum3+p2[o][2]
		c2[2]=sum3/len(p2)
		sum3=0
	#update centriod3:
	if len(p3)!=0:
		for o in range(len(p3)):
			sum1=sum1+p3[o][0]
		c3[0]=sum1/len(p3)
		sum1=0
		for o in range(len(p3)):
			sum2=sum2+p3[o][1]
		c3[1]=sum2/len(p3)
		sum2=0
		for o in range(len(p3)):
			sum3=sum3+p3[o][2]
		c3[2]=sum3/len(p3)
		sum3=0
	if(k==9):
		q1=p1
		q2=p2
		q3=p3
#assigning colours to each cluster:
for t in range(len(q1)):
	q1[t][0]=100
	q1[t][1]=100
	q1[t][2]=256
for t in range(len(q2)):
	q2[t][0]=100
	q2[t][1]=256
	q2[t][2]=100
for t in range(len(q3)):
	q3[t][0]=256
	q3[t][1]=100
	q3[t][2]=100

cv2.imwrite("test2.png",image)

