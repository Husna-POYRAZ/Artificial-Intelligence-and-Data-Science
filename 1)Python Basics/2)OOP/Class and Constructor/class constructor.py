# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 13:44:32 2020

@author: DELL
"""

class Employee:
    
    raise_salary = 1.8
    counter = 0
    def __init__(self, name, surname, salary): # constructor
        self.name = name
        self.surname = surname
        self.salary = salary
        self.email = name + surname+ "@asd.com"
        
        Employee.counter = Employee.counter + 1
        
        
    def giveNameSurname(self): # Use self to access the variables of the class.
        return self.name +" " +self.surname
        
    def salary_increase(self):
        self.salary = self.salary + self.salary*self.raise_salary

employee1 = Employee("Hüsna", "Poyraz", 1000)
print(employee1.email)
print(employee1.giveNameSurname())
print(employee1.salary)

employee1.salary_increase()
print("New salary : " + str(employee1.salary))

employee2 = Employee("Ali", "Poyraz", 1000)
employee3 = Employee("Hasan", "Poyraz", 3000)
employee4 = Employee("Melih", "Poyraz", 2400)

list1 = [employee1, employee2, employee3, employee4]

# Finding the highest salary
max_salary = -1
for each in list1:
    if(each.salary > max_salary):
        max_salary = each.salary
        index = each   

print(max_salary)
print(index.giveNameSurname())
    
# %% Simple Class-Constructor Example

class A:
    global a
    a = 5
    def _init_(self, x = 4):
        self.x = x
    
    def sum(self):
        return a + self.x
    
x = A(5)
x.sum()  #output = 10

# %% Simple Class-Constructor Example
class Hello:
    def _init_(self, x = "hi"):
        self.x = x
    
    def show(self):
        print(self.x)
    
    my_class = Hello()
    my_class.show()




