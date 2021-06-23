# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 11:52:43 2020

@author: YUKTI_PC
"""
num = int(input("Enter a number: "))  

def armStrong(n):
    sum = 0  
    temp = n 
  
    while temp > 0:  
        digit = temp % 10  
        sum += digit ** 3  
        temp //= 10  
        
    if n == sum:  
        print(n,"is an Armstrong number")  
    else:  
        print(n,"is not an Armstrong number")  

def primeNumber(s):
    if s > 1:
        for i in range(2,s):
            if (s % i) == 0:
                print(s,"is not a prime number")
                break
            else:
                print(s,"is a prime number")
    else:
       print(s,"is not a prime number")
       
print(primeNumber(num))
print(armStrong(num))
