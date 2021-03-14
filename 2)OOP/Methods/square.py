# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 07:51:15 2021

@author: DELL
"""
#calculating the area of the square
class Square(object):
    
    edge = 5
    
    def area1(self):
        self.area = self.edge * self.edge
        print("Area = ",self.area)

s1 = Square()
s1.area1()

s1.edge = 7
s1.area1()
