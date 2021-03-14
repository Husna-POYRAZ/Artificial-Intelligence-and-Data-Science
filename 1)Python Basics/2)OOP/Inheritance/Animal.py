# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 08:21:16 2021

@author: DELL
"""

#Parent class Animal
class Animal(object): 
    def __init__(self):
        print("Animal is created.")
        
    def toString(self):
        print("Animal")
    
    def walk(self):
        print("Animal walk")
    
#Child class Monkey
class Monkey(Animal): 
    def __init__(self):
        super().__init__() #use init of parent(animal) class
        print("Monkey is created.")
        
    #override
    def toString(self):
        print("Monkey")
    
    def climb(self):
        print("Monkey climb")

#Child class Bird
class Bird(Animal):
    def __init__(self):
        print("Bird is created")
        
    def fly(self):
        print("Bird fly")

m1 = Monkey()
m1.toString()
m1.climb()
print("******")    
b1 = Bird()
b1.toString()
b1.fly()