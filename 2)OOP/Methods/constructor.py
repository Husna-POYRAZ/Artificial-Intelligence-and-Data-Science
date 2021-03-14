# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 08:27:27 2021

@author: DELL
"""
#constructor or initializer
class Animal(object):
    
    #crate constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    #create method
    def getAge(self):
        return self.age
    
    def getName(self):
        print(self.name)

#create obje
a1 = Animal("Pamuk", 5)
a2 = Animal("Duman", 3)
a3 = Animal("Mess", 15)

a1.getName()
print(a1.getAge())

