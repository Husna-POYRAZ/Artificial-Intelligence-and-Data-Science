# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 08:21:07 2021

@author: DELL
"""

print(range(10))

#%%
for var in range(10):
    print(var)
    
#%%
for var in enumerate(range(10)):
    print(var)    # type(var) = <class 'tuple'>

#%%
for (index, var) in enumerate(range(5,10)):
    print(var)