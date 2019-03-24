import cv2
import numpy as np
import matplotlib.pyplot as plt
import random as rd
image =cv2.imread("d.jpg")
import math
from numpy.linalg import eig
from numpy import array
from numpy import mean
from numpy import cov
A=[]
for i in range(np.shape(image)[0]):
	for j in range(np.shape(image)[1]):
		A.append(image[i][j])
A = array(A)
# calculate the mean of each column
M = mean(A.T, axis=1)
# center columns by subtracting column means
C = A - M
# calculate covariance matrix of centered matrix
V = cov(C.T)
# eigendecomposition of covariance matrix
values, vectors = eig(V)
# project data
P = vectors.T.dot(C.T)
P=P.T
P=array(P)
k=0
for i in range(np.shape(image)[0]):
	for j in range(np.shape(image)[1]):
		image[i][j]=P[k]
		k+=1
cv2.imwrite("pca.ipg",image)
