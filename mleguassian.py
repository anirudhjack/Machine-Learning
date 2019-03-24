#maximum likelihood algorithm for guassian distribution with K=2:
import numpy as np
import random as rd

def guassian(x,m,v):
	r=np.exp(-((x-m)**2)/(2*v))
	r=float(r)/float((np.sqrt(2*(np.pi)*v)))
	return r
def comp(p,m,v):
	r=m+np.sqrt(-v*np.log(2*(np.pi)*v)-2*v*(np.log(p)))
	print(r)
def comp1(p,m,v):
	r=m-np.sqrt(-v*np.log(2*(np.pi)*v)-2*v*(np.log(p)))
	print(r)
#data
data=[-9.345,2.371,4.654,-7.2349,3.238,-8.2412,12.234,5.974,-6.214,-0.345]
#assigning random means and varainces:
mu1=rd.uniform(-15,15)
v1=rd.uniform(0.5,5)
mu2=rd.uniform(-15,15)
v2=rd.uniform(0.5,5)
#declaring priors initially:
p1=0.5
p2=0.5
f1=[]
f2=[]
for i in range(50):
	#declaring lists for apriori probabilities:
	ap1=[]
	ap2=[]
	for j in range(len(data)):
		lp1=guassian(data[j],mu1,v1)
		lp2=guassian(data[j],mu2,v2)
		aap1=float(lp1*p1)/float(lp1*p1+lp2*p2)
		aap2=1-aap1
		ap1.append(aap1)
		ap2.append(aap2)
	mu1=0
	mu2=0
	v1=0
	v2=0
	sum1=0
	sum2=0
	#updating the means and varainces:
	for k in range(len(data)):
		mu1=mu1+data[k]*ap1[k]
		sum1=sum1+ap1[k]
	mu1=float(mu1)/float(sum1)
	for k in range(len(data)):
		v1=v1+ap1[k]*((data[k]-mu1)**2)
	v1=float(v1)/float(sum1)
	for k in range(len(data)):
		mu2=mu2+data[k]*ap2[k]
		sum2=sum2+ap2[k]
	mu2=float(mu2)/float(sum2)
	for k in range(len(data)):
		v2=v2+ap2[k]*((data[k]-mu2)**2)
	v2=float(v2)/float(sum2)
	#updating prioris:
	p1=float(sum1)/float(len(data))
	p2=1-p1
	if i==49:
		f1=ap1
		f2=ap2

