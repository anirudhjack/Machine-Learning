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

print("Enter the dimension:")
p=int(input())

print("Enter the value of alpha:")
alpha=float(input())

print("Enter the value of beta:")
beta=float(input())

lam=alpha/beta
print("Maximum posterior regularized lagrange multiplier:")
print(lam)

#loop for x with dimension "d"
for i  in range(2,p):
    x= np.vstack((x,np.power(x_g, i)))
    
x_p=x

#transpose of x-matrix
x=np.transpose(x)

#calculating the weight matrix
from numpy.linalg import inv
w=np.linalg.inv(x_p@x+lam*np.identity(p))@x_p@y

print("Maximum posterior weight matrix:")
print(w)


