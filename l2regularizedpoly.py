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

print("Enter the dimesnsion:")
p=int(input())

print("Enter the value of lagrange multiplier")
lam=int(input())

#loop for x with dimension "d"
for i  in range(2,p):
    x= np.vstack((x,np.power(x_g, i)))
x_p=x

#transpose of x-matrix
x=np.transpose(x)

from numpy.linalg import inv
#calculating the weight matrix
w=np.linalg.inv(x_p@x+lam*np.identity(p))@x_p@y

#ploting the training data
plt.plot(x_g,y,'-o')
plt.xlabel("Training Data(x)")
plt.ylabel("Training label(y)")
plt.plot(x_g,y,'-bo',label='samples of function')
plt.plot(x_g,x@w,'m:',label='l2 polynomial basis function')
plt.legend()
plt.plot(x_g,x@w,'m:')

#ploting two graphs 
plt.show()
