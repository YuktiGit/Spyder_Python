# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 11:34:46 2020

@author: YUKTI_PC
"""
while (True) :
    num = int(input("Enter an integer : "))

    if (num%2 == 0):
        print("The integer is even number!")
    else :
        print("The integer is odd number!")

    if(num < 0):
        print("The integer is negative!")
    else :
        print("The integer is positive!")