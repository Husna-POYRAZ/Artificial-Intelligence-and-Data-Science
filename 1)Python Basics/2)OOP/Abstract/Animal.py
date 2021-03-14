# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 09:03:22 2021

@author: DELL
"""
from abc import ABC, abstractmethod

class Animal(ABC):
    
    @abstractmethod
    def walk(self): pass

    @abstractmethod
    def run(self): pass

    
    def swim(self): pass

class Bird(Animal):
    def __init__(self):
        print("Bird is created.")
    def walk(self):
        print("Bird walk")
        
    def run(self):
        print("Bird run")
    
b1 = Bird()   