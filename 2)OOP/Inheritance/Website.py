# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 08:44:00 2021

@author: DELL
"""

class Website:
    "parent"
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        
    def loginInfo(self):
        print(self.name + " " + self.surname)
    
class Website1(Website):
    "child"
    def __init__(self, name, surname, id):
        Website.__init__(self, name, surname)
        self.id = id
        
    def login(self):
        print(self.name + " " + self.surname + " " + self.id)

class Website2(Website):
    "child"
    def __init__(self, name, surname, email):
        Website.__init__(self, name, surname)
        self.email = email
    
    def login(self):
        print(self.name + " " + self.surname + " " + self.email)
    
p1 = Website("name", "surname")
p2 = Website1("name", "surname", "123")
p3 = Website2("name", "surname", "email@gmail.com")
