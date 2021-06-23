# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 12:03:05 2020

@author: YUKTI_PC
"""

inp = input("Input some space seprated words : ")
words = inp.split(" ")
tup1 = tuple(words)
inp2 = input("Input some other comma separated words :")
words2 = inp2.split(",")
tup2 = tuple(words2)
print("Tuple 1 :",tup1)
print("Tuple 2 :",tup2)
print("After joining both the tuples we get ",(tup1+tup2))