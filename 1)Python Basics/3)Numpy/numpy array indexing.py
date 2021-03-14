# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 23:51:27 2020

@author: DELL
"""

# numpy array indexing

import numpy as np

numbers = np.array([0, 5, 10, 15, 20, 25, 50, 75])

result = numbers[5]
result = numbers[-1]
result = numbers[0:3]
result = numbers[:3]
result = numbers[3:]
result = numbers[::]   # array sort
result = numbers[::-1] # reverse sort


numbers2 = np.array([[0, 5, 10], [15, 20, 25], [50, 75, 85]])

result = numbers2[0]
result = numbers2[2]
result = numbers2[0, 2]
result = numbers2[2, 1]
result = numbers2[:,2]  # return the element in index 2 of each row
result = numbers2[:,0]
result = numbers2[:,0:2] # return the elements from index 0 to  2 of each row
result = numbers2[-1,:]
result = numbers2[:2,:2]

# %%
arr1 = np.arange(0, 10)
arr2 = arr1  # reference

print(arr1)
print(arr2)

arr2[3] = -23 #arr 1 and arr 2 are arrays that point to the same address. Changes made in one affect the other

print(arr1)
print(arr2)

# %%
arr3 = np.arange(10, 20)
arr4 = arr3.copy() # It keeps a different address, so the changes made do not affect each other.

print(arr3)
print(arr4)

arr4[3] = -23

print(arr3)
print(arr4)







