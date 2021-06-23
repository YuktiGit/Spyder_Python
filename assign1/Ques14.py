# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 21:46:16 2020

@author: YUKTI_PC
"""
count = 0
s = input("Enter a string :" )
vowels = ['a' , 'e' , 'i' ,'o' , 'u']
for char in s:
    if char in vowels:
        count += 1
print ('Number of vowels: ' , count)