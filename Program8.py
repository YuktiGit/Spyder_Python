# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 11:56:04 2020

@author: YUKTI_PC
"""
print("Upper and lower cases : ")
ss = "Python Program"
print(ss.upper())
print(ss.lower())

print("Is the string numeric : ")
number = "5dfg"
letters = "ab3cgh"
print(number)
print(number.isnumeric())
print(letters)
print(letters.isnumeric())

print("Length of string : ")
open_source = "contributes to open source."
print(open_source)
print(len(open_source))

print("Join and Split functions :")
balloon = "Variable as a balloon."
a = balloon.split()
print(a)
print(" ".join(a))

print("Is the string numeric or aphabatic : ")
strs = "123"
print(strs)
print(strs.isalnum())
print(strs.isalpha())