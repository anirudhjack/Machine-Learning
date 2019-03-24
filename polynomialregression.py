import numpy as np
print(" Enter the No of training samples")
N=int(input())
x_g=np.linspace(0,2*np.pi,N)
y=np.sin(x_g)
mean=0
std=0.05
y+=np.random.normal(mean,std,N)
import matplotlib.pyplot as plt

x=np.vstack((np.ones(N),x_g))
print("Enter the dimension:")
p=int(input())
for i  in range(2,p):
    x= np.vstack((x,np.power(x_g, i)))
x_p=x
x=np.transpose(x)
from numpy.linalg import inv
w=np.linalg.inv(x_p@x)@x_p@y

plt.xlabel("Training Data(x)")
plt.ylabel("Training label(y)")
plt.title("Polynomial regression")
plt.plot(x_g,y,'-bo',label='samples of function')
plt.plot(x_g,x@w,'m:',label='polynomial basis function')
plt.legend()
plt.show()
