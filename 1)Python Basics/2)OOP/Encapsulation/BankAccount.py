# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 07:57:14 2021

@author: DELL
"""

class BankAccount(object):
    #create constructor
    def __init__(self, name, money, address):
        self.name = name        #global variable
        self.__money = money    #private variable
        self.address = address
        
    #global method (get and set)
    def getMoney(self):
        return self.__money
    
    def setMoney(self, amount):
        self.__money = amount
    
    #private method
    def __increase(self):
        return self.__money + 500

#create obje (p1, p2)
p1 = BankAccount("Messi", 1000, "Barcelona")
p2 = BankAccount("Neymar", 2000, "Paris")

p1.setMoney(5000)
print("After set method:", p1.getMoney())

# p1.__increase()
# print("After increase method:", p1.getMoney())




        
    