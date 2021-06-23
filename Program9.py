# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 11:56:09 2020

@author: YUKTI_PC
"""

def recurFactorial(n):  
   if n == 1:  
       return n  
   else:  
       return n*recurFactorial(n-1)  
 
num = int(input("Enter a number: "))  
 
if num < 0:  
   print("Sorry, factorial does not exist for negative numbers")  
elif num == 0:  
   print("The factorial of 0 is 1")  
else:  
   print("The factorial of",num,"is",recurFactorial(num))  