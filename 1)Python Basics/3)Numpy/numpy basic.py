# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 11:18:05 2020

@author: DELL
"""

# importing
import numpy as np
#create python list
py_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

#create numpy array
np_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

print(type(py_list))
print("Python List :") 
print(py_list) 

print(type(np_array))
print("Numpy Array :") 
print(np_array)

# %%
#create multi python list 
py_multi = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

#create multi numpy array
np_multi = np_array.reshape(3, 3)  # 3x3 matrix 

print("Multi Python List :") 
print(py_multi)
print("Multi Numpy Array :")
print(np_multi)

# %% .ndim
print("Dimention numpy array : ")
print(np_array.ndim)
print("Dimention multi array :")
print(np_multi.ndim)

# %% .shape
print("Shape Numpy Array :") 
print(np_array.shape)
print("Shape Multi Numpy Array :")  
print(np_multi.shape)

# %% 
# arange()
result = np.arange(1, 10)
print(result)

result = np.arange(1, 10, 2)
print(result)

result = np.arange(10)
print(result)

# %%
# zeros()
result = np.zeros(5)
print(result)
zeros = np.zeros((3,3))

zeros[0,0] = 5
print(zeros)

# %%
#ones()
result = np.ones(5)
print(result)

# %%
# eye() method

result = np.eye(5,5)    
print(result)

# %%
# linspace () method

result = np.linspace(0, 100, 5)
print(result)

result = np.linspace(0, 5, 5)
print(result)

# %%
# random

result = np.random.randint(0, 10, 9)     # Random integer numbers between 0 and 10 are generated and returns.
print(result)

result = np.random.randint(20)         # beginning is default value = 0
print(result)

result = np.random.randint(10, 50, 3)     # Returns 3 random numbers between the specified range
print(result)

# %%
# concatenate() method

numpy_array = np.array([0,1, 2, 3, 4, 5, 6, 7, 8, 9])
numpy_multi = numpy_array.reshape(5,2)

print("Vertical merge :")
print(np.concatenate([numpy_multi, numpy_multi], axis =0))

print("Horizontal merge :")
print(np.concatenate([numpy_multi, numpy_multi], axis =1))

# %%
# mathematical operation

print(numpy_multi.sum(axis = 1)) # Vertical sum

print(numpy_multi.sum(axis = 0)) # Horizantol sum

# max () method
result = numpy_array.max()
print(result)

# min () method
result = numpy_array.min()
print(result)

# argmax () method
result = numpy_array.argmax()
print(result)

# argmin () method
result = numpy_array.argmin()
print(result)

# %%
# numpy basics examples
myarray = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])  # 1*15 vector

print(myarray.shape)

a = myarray.reshape(3,5)
print("shape: ",a.shape)
print("dimension: ", a.ndim)

print("data type: ",a.dtype.name)
print("size: ",a.size)

print("type: ",type(a))

array1 = np.array([[1,2,3,4],[5,6,7,8],[9,8,7,5]])

zeros = np.zeros((3,4))

zeros[0,0] = 5
print(zeros)

ones = np.ones((3,4))
print(ones)

empty = np.empty((2,3))
print(empty)

a = np.arange(10,50,5)
print(a)

a = np.linspace(10,50,20)
print(a)
