# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 00:19:26 2020

@author: DELL
"""

import numpy as np

numbers1 = np.random.randint(10, 100, 6)
numbers2 = np.random.randint(10, 100, 6)

print(numbers1)
print(numbers2)

result = numbers1 + numbers2
result = numbers1 + 10
result = numbers1 - numbers2
result = numbers1 * 10
result = numbers1 / numbers2
result = numbers1 / 2

result = np.sin(numbers1)
result = np.tan(numbers1)
result = np.sqrt(numbers1)
result = np.log(numbers1)

# %%
mnumbers1 = numbers1.reshape(2,3)
mnumbers2 = numbers2.reshape(2,3)

print(mnumbers1)
print(mnumbers2)

result = np.vstack((mnumbers1, mnumbers2)) # Vertical merge
result = np.vstack((mnumbers1, mnumbers2)) #Horizontal merge

result = numbers1 >= 50 # return boolean value
result = numbers1 % 2 == 0

print(result)
print(numbers1[result]) # Returns true values

