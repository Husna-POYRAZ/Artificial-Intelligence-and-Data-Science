# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 08:40:02 2021

@author: DELL
"""

#%%
def add(*args):
    return sum(args)

result = add(1,2,3,4,5)
print(result)

#%%
def func(**kwargs):
    print(kwargs)
    
func(apple = 300 , banana = 200, orange = 130)  # return dictionary

#%%
def keyWordControl(**kwargs):
    if "Ali" in kwargs:
        print("He is here.")
    else:
        print("He isn't here.")
        
student = keyWordControl(Ali = 1001, Veli = 1002, Hasan = 1003)
