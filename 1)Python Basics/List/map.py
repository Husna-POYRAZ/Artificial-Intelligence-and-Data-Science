# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 09:57:40 2021

@author: DELL
"""
def div(number):
    return number / 2

myList = list(range(0,10))
newList = []

for var in myList:
    newList.append(div(var))
    
print(myList)
print(newList)

#%%
def div(number):
    return number / 2

myList = list(range(0,10))

newList = [div(var) for var in myList]

print(myList)
print(newList)

#%%
myList = list(range(0,10))

newList = list(map(div, myList))

print(myList)
print(newList)

#%% 

def func(string):
    return "a" in string
        
strList = ["Hüsna", "Ali", "Nur", "Ecem", "Hasan", "Furkan", "Mehmet"]

#map, return true or false value
newList = list(map(func, strList))

print(newList)


# filter, return true variable

x = list(filter(func, strList))
print(x)


print(newList.count(True))



# lambda
myList = [10, 20, 30, 40, 50]
result = list(map(lambda multiplication : multiplication * 3, myList))
print(result)






















