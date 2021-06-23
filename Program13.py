# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 11:36:10 2020

@author: YUKTI_PC
"""
theDict = {}
theDict = dict([(1,'apple'), (2,'banana'), (3,'mango'), (4,'orange')])


x = len(theDict)
print("The length of dictionary is : ")
print(x)


print("Delete lst element : ") 
theDict.pop(3) 
print(theDict) 

print("Add a element : ") 
theDict["5"]="kiwi" 
print("After addition : ")
print(theDict) 

print("Create a copy of dictionary : ") 
dict1 = theDict 
print(dict1) 