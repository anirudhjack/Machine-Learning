import numpy as np
print(" Enter the No of training samples")
N=int(input())
x_g=np.linspace(0,2*np.pi,N)

y=np.sin(x_g)

mean=0

std=0.05

y+=np.random.normal(mean,std,N)

import matplotlib.pyplot as plt

#creating x-matrix using vstack function i.e arrange the data row wise
x=np.vstack((np.ones(N),x_g))
x_p=x

#transpose of x-matrix
x=np.transpose(x)

from numpy.linalg import inv

#calculating the weight matrix
w=np.linalg.inv(x_p@x)@x_p@y

print("The values of weights are:")
print(w)

error=np.power((y-x@w),2)
print("errors for each test data:")
print(error)

print("value of Maximum likelihood variance:")
p=np.power((y-x@w),2).sum()/N
print(p)

