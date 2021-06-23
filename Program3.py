# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 12:16:21 2020

@author: YUKTI_PC
"""
i = 0
j = 0
while i < 5 :
    word = input("Enter the word :" )
    for j in range(len(word)):
        print(word[j])
    i = i+1
print(" ")