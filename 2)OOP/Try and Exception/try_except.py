# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 09:51:47 2021

@author: DELL
"""
total = 0 
counter = 0 

while True:
    value = input("Enter a number: ")
    if value == "done":
        break
    try:
        value = int(value)
    except:
        print("Invalid Error.")
        continue
        
    counter = counter + 1
    total = total + value

print(counter, total, total / counter)
