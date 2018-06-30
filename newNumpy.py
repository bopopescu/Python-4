import numpy as np

"""A= np.array([(10,20,30),(40,50,60)])
print(A)
print(type(A))

B = np.array([ [[10,20],[30,40]] , [[70,80],[89]] ])

print(A[0])

print("dimension of array",A.ndim)
print("dimension of array",B.ndim)"""

#SHAPE OF A NUMPY ARRAY IS IMMUTABLE

A = np.array([10,20,30,40,50,60])
print("Size: ", A.itemsize)
print("Size: ",A.__sizeof__())
print("Size: ",A.size)

print("DataType ",A.dtype)
print("Shape ",A.shape)
print("***************************")
P = np.array([(10,20,30),(40,50,60)])
print(P)
print(P.shape)
Q = P.reshape(3,2)
print(Q)
print(Q.shape)

print(P[0,1])#SLICING
print(P[0][1])

print(P[0:,2])
print(P[0:2,1])
print("***************************")

w=np.linspace(1,5,10)
print(w)
print("***************************")

v = np.array([10,20,30,])
print("Max",v.min())
print("Min",v.max())
print("sum",v.sum())

print("***************************")

x = np.array([[1,2,3],[4,5,6]])
y= np.array([[1,2,3],[4,5,6]])

z=x+y
print(z)

z=x-y
print(z)

print("***************************")

k = np.array([[1,2],[3,4]])
l = np.array([[5,6],[7,8]])
m=np.sqrt(k)
print(m)
n=np.std(k)
print(n)
