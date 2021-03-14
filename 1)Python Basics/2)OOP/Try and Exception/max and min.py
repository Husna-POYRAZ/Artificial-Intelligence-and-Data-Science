# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 10:11:56 2021

@author: DELL
"""

largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" : break
    try:
        num = int(num)
    except:
        print("Invalid input")
        continue
    if  smallest == None or largest == None:
        smallest = num
        largest = num
    if num > largest:
        largest = num
    elif num < smallest:
        smallest = num
    
    

print("Maximum is", largest)
print("Minimum is", smallest)