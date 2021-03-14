# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 17:17:09 2020

@author: DELL
"""
# %% list

liste = [1,2,3,4,5,6]
print(type(liste))

liste_str = ["Monday","Tuesday","Wednesday"]
print(type(liste_str))

value = liste[1]
print(value)

last_value = liste[-1]
print(last_value)

liste_divide = liste[0:3]

liste.append(7)
liste.remove(7)
liste.reverse()
liste2 = [1,5,4,3,6,7,2]
liste2.sort()

string_int_liste = [1,2,3,"aa","bb"]

# %% Simple list example

list3 = ["milk", "orange", "fish", "water"]
for i in list3:
    print(i)

# %% tuple

t = (1,2,3,3,4,5,6)

t.count(3) # return number of occurrences of value
           #output = 2

t.index(3) #return first index of value
           #output = 2

# %% dictionary

dictionary = {"ali":32,"veli":45,"ayse":13}


# ali ,veli ,ayse = keys
# 32,45,13 = values

print(dictionary.keys())       #output = dict_keys(['ali', 'veli', 'ayse'])
print(dictionary.values())     #output = dict_values([32, 45, 13])

def deneme():
    dictionary = {"ali":32,"veli":45,"ayse":13}
    return dictionary

dic = deneme()
print(dic)      #output = {'ali': 32, 'veli': 45, 'ayse': 13}


# %% conditionals
# if else statement

var1 = 10
var2 = 20

if(var1 > var2):
    print("var1 is greater than var2.")
elif(var1 == var2):
    print("var and var2 are equal.")
else:
    print("var1 kucuktur var2")


list1 = [1,2,3,4,5]

value = 3
if value in list1:  #if value(3) is in the list
    print("Yes. The value {} is in the list.".format(value))
else:
    print("No. The value {} is not in the list.".format(value))


keys = dictionary.keys()

if "veli" in keys:
    print("Yes")
else:
    print("No")
    
# %%
# 1640. yil == 17. yuzyil
# 109. yil == 2. yuzyil
# 2000. yil = 20. yuzyil
    
# metod yazin.
    # input integer yillar
    # output integer yuzyil

# input = year  >> 1 <= year <= 2005
    
def year2Century(year):
    """
    year to century
    """
    str_year = str(year)
    
    if(len(str_year)<3):
        return 1
    elif(len(str_year) == 3):
        if(str_year[1:3] == "00"):  # 100 ,200 300, 400 ... 900
            return int(str_year[0])
        else:                       # 190, 250, 450
            return int(str_year[0])+1
    else:                           # 1750, 1700, 1805
        if(str_year[2:4]=="00"):    # 1700, 1900, 1100
            return int(str_year[:2])
        else:                       # 1705, 1645, 1258
            return int(str_year[:2])+1
        
# %% loops
# for loop
    
for each in range(1,11):   # Get all numbers from 1 to 11 (11 not included)
    print(each)            # output = 1 2 3 4 5 6 7 8 9 10
    
for each in "ankara ist":  # Retrieves all the characters of the entered string expression one by one in                            #order
    print(each)            # output = a n k a r a   i s t
    
for each in "ankara ist".split():  # separate the array by the space character.
    print(each)
    
liste = [1,4,5,6,8,3,3,4,67]
 
summation = sum(liste)      # sum() is a method.

count = 0
for each in liste:
    count = count + each
    print(count)


# %% while loop
    
i = 0
while(i <4):
    print(i)
    i = i + 1


sinir = len(liste)   
each = 0
count = 0
while(each < sinir):
    count = count + liste[each]
    each = each + 1 
    
    
# %% simple while loop example

c = 1
while c < 7:
    print(c)
    if c == 4:
        break
    c += 1
    

# %%

# Find the smallest element in a given list

liste = [1,2,3,4,5,6,4,23,67,21,-500,23,451,67]

mini = 100000
for each in liste:
    if(each < mini):
        mini = each
    else:
        continue  
    
print(mini)  
    
    
    
    
    
    
    
    
    