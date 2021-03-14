# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 11:40:53 2021

@author: DELL
"""

#String Methods
str = "hüsna Poyraz"
print(str)               # hüsna Poyraz
print(str.capitalize())  # Hüsna Poyraz
print(str.upper())       # HÜSNA POYRAZ
print(str.lower())       # hüsna poyraz
print(str.split())       # ['hüsna', 'Poyraz']  --> this is a list.
print(str.split(' ')[1]) # Poyraz
print(str.split(' ')[0]) # hüsna

#%%
a = "Hello"
b = input("Enter your name:")  # if enter a ALi
print(a +" " + b)        # Hello ALi
print(b * 5)             # ALiALiALiALiALi

#%%
k = '34'
j = '43'
print(k + j)