# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 11:52:41 2020

@author: YUKTI_PC
"""

import math

n = int(input("Enter an integer on which in- built math functions can be performed : "))

print("Square root calculation")
print(math.sqrt(n))

print("Trignometric functions")
print(math.cos(n))
print(math.sin(n))
print(math.tan(n))

print("the factorial of a number")
print(math.factorial(n))

print("the natural logarithm of a number, or the logarithm of number to base")
print(math.log(n, 10))

print("the value of x to the power of y")
print(math.pow(n, 5))

print("the remainder of specified numbers when a number is divided by another number")
print(math.fmod(n, 2))

print("the absolute value of a number")
print(math.fabs(n))

print("Rounds a number upwards to the nearest integer")
print(math.ceil(n))	
