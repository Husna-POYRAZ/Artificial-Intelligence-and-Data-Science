# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 07:59:16 2021

@author: DELL
"""
from random import randint

#%%
a = randint(0,10)
print(a)

#%%
sortedList = list(range(0,10))
print(sortedList)          # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#%%
from random import shuffle
shuffle(sortedList)         #[6, 4, 7, 3, 0, 9, 2, 8, 5, 1]
print(sortedList)