# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 12:03:04 2020

@author: YUKTI_PC
"""

list1 = ['ram', 'shyam', 'raju']
print("list1  :  "+str(list1))
tuple1 = tuple(list1)
print("list1 converted to tuple1  :  "+str(tuple1))
tuple2 = ('printer', 'speaker', 'UPS')
print("Tuple2  :  "+str(tuple2))
list2 = list(tuple2)
print("tuple2 converted to list2  :  "+str(list2))
list3 = [1,'jammu',2,'kashmir',3,'goa']
print("list3  :  "+str(list3))
dict1 = {}
for i in range(0,len(list3),2):
    dict1[list3[i]]= list3[i+1]
print("list3 converted to dict1  :  "+str(dict1))