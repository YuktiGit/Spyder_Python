# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 19:39:18 2020

@author: YUKTI_PC
"""

def binaryToDecimal(n): 
    num = n; 
    dec_value = 0; 
    base = 1; 
      
    temp = num; 
    while(temp): 
        last_digit = temp % 10; 
        temp = int(temp / 10); 
          
        dec_value += last_digit * base; 
        base = base * 2; 
    return dec_value; 
  
num = int(input("Enter a four digit binary number :")); 
print("The decimal conversion of binary", num,"is : " , binaryToDecimal(num)); 
