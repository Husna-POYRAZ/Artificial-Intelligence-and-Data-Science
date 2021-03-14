# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 14:58:24 2020

@author: DELL
""" 
# %%
#variable

var1 = 10 #integer
var2 = 15
day = "sunday" #string
var3 = 10.3   #double or float


 # %%
#string

s = "Today is Monday."

variable_type = type(s)
print(s)

var1 ="Ankar"
var2 = "İst"
var3 = var1 + var2
print(var3)
print(len(var3))
print(var3[2])

# %%
#numbers

#integer
integer_deneme = -49

#double = float = ondalikli sayi
float_deneme = -13.4

# %%  built in function

str1 = "1002"
print(type(int(str1)))
print(round(int(str1)))
print(len(str1))

# %% user define function
def func(var1, var2):
    output = (((var1 + var2) * 50) / 100.0) * var1 / var2
    return output

result = func(20, 50)

# %% user define function example
def x(y):
    y = y + [2]
    print(y)
c = [1, 2, 3]
print(x(c))
print(len(c))

# %% default ve flexible functions

# default function: circumference length of the circle = 2*pi*r 

def compute(r, pi=3.14): 
   """ 
   circumference length of the circle
   input(parametre): r,pi 
   output = circumference of the circle
   """ 
   output = 2*pi*r 
   return output
print(compute(3))
print(compute(3,3))

# %% default function exmaple
def s(x, y=2):
    c = 2
    for i in range(y):
        c = c + x
    return c
print(s(2))
print(s(2,3))
    
# %% flexible function
def compute(height,weight,*args): 
    print(args)
    output = (height + weight)
    return output
print(compute(165, 56, 3, 5, 7, 9))

# %% Summary

# int variable: age
# string name: name
# fonction print(type(),len,float()) 
# *args : surname
# default parametre : foot_number
    
age = 10
name = "Ali"
surname = "Sahin"

def function_summary(age, name, *args, foot_number=39):
    print("Child' name: ",name, " age: ",age," foot number: ",foot_number)
    print(type(name))
    print(float(age))
    
    output = args[0]*age
    
    return output

result = function_summary(age, name, surname)  # args -> surname 

print("args[0]*age : ", result)

# %% lambda function

def compute(x):
    return x*x
sonuc = compute(3)

sonuc2 = lambda x: x*x
print(sonuc2(3))

# %% lambda function example
y = 3
z = lambda x : x*y
print(z(3))
































