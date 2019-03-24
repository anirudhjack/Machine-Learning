

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
#ploting the training data
plt.xlabel("Training Data(x)")
plt.ylabel("Training label(y)")
plt.title("Vanilla Regression")
plt.plot(x_g,y,'-bo',label='samples of function')
plt.plot(x_g,x@w,'m:',label='vanilla linear regression')
plt.legend()
#ploting the test data
#ploting two graphs 
plt.show()
