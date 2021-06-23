# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 21:34:22 2020

@author: YUKTI_PC
"""

def sumOfNauralNum(n):
    if n <= 1:
        return n
    return n + sumOfNauralNum(n-1)
num = int(input("Enter a number : "))
print(sumOfNauralNum(num))
