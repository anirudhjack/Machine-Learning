import numpy as np
import random as rd

def sigmoid(num):
	return 1.0/(1.0+np.exp(-num))
	
weight1=[[rd.random() for i in range(4)]for j in range(10)]

weight=[[rd.random() for i in range(10)]for j in range(4)]

learning_rate=0.5

def Forward_propagate(Input):
	preoutput=sigmoid(np.dot(weight1,Input))
	output=sigmoid(np.dot(weight,preoutput))
	return (preoutput,output)
	
def back_propagation(Input,target):
	(preoutput,output)=Forward_propagate(Input)
	error_weight=[]
	for i in range(4):
		error_last=[]
		for j in range(10):
			error=learning_rate*(target[i]-output[i])*output[i]*(1-output[i])*preoutput[j]
			error_last.append(error)
		error_weight.append(error_last)
	
	error_weight=np.array(error_weight)
	error_weight=error_weight[:,:,0].reshape(4,10)
	(preoutput,output)=Forward_propagate(Input)
	#updating the weights between hidden layer and input layer:
	error_weight1=[]
	for i in range(10):
		error_first=[]
		for j in range(4):
			for k in range(4):
				error=0.0
				error=error+(target[k]-output[k])*(output[k])*(1-output[k])*weight[k][i]
			error=error*preoutput[i]*(1-preoutput[i])*Input[j]*learning_rate
			error_first.append(error)
		error_weight1.append(error_first)
	error_weight1=np.array(error_weight1)
	error_weight1=error_weight1[:,:,0].reshape(10,4)
	

	return (error_weight,error_weight1)
for i in range(1000):
	Input1=[[0,0,0,0]]
	Input1=np.transpose(Input1)
	target1=[0,0,0,0]
	Input2=[[1,1,1,1]]
	Input2=np.transpose(Input2)
	target2=[1,1,1,1]	
	Input3=[[1,0,0,0]]
	Input3=np.transpose(Input3)
	target3=[1,0,0,0]
	Input4=[[0,0,0,1]]
	Input4=np.transpose(Input4)
	target4=[0,0,0,1]
	(p,q)=back_propagation(Input1,target1)
	weight=weight+p
	weight1=weight1+q
	(p,q)=back_propagation(Input2,target2)
	weight=weight+p
	weight1=weight1+q
	(p,q)=back_propagation(Input3,target3)
	weight=weight+p
	weight1=weight1+q
	(p,q)=back_propagation(Input4,target4)
	weight=weight+p
	weight1=weight1+q
	
i=[[0,0,0,0]]
i=np.transpose(i)
(o,r)=Forward_propagate(i)
print(r)
i=[[1,1,1,1]]
i=np.transpose(i)
(o,r)=Forward_propagate(i)
print(r)
i=[[1,0,0,0]]
i=np.transpose(i)
(o,r)=Forward_propagate(i)
print(r)
i=[[0,0,0,1]]
i=np.transpose(i)
(o,r)=Forward_propagate(i)
print(r)

