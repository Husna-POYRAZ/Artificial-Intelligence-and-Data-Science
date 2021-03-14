# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 08:16:48 2021

@author: DELL
"""
#%%
emptyList = []
myList = "Hüsna POYRAZ"

for var in myList:
    emptyList.append(var)
    
print(emptyList)

#%%
newList = [var for var in myList]
print(newList)

#%%
myList = [num * 5 for num in range(0, 10)]
print(myList)

