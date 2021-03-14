# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 07:58:49 2021

@author: DELL
"""

#method and function
class Emp(object):
    age = 25
    salary = 1000 
    
    #method
    def ageSalaryRatio(self):
        a = self.age / self.salary
        return a

#function
def ageSalaryRatio(age, salary):
    a = age / salary
    return a

#create obje
e1 = Emp()
#call method
print(e1.ageSalaryRatio())

#call function
print(ageSalaryRatio(25, 1000))

