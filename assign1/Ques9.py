# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 20:57:46 2020

@author: YUKTI_PC
"""

def gcd(a,b): 
    if (b == 0): 
         return a 
    return gcd(b, a%b) 
  
a = int(input("Enter first number : "))
b = int(input("Enter first number : "))
if(gcd(a, b)): 
    print('GCD of', a, 'and', b, 'is', gcd(a, b)) 
else: 
    print('not found') 
  
    