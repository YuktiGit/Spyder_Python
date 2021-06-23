# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 13:25:15 2020

@author: YUKTI_PC
"""

num1 = input('Enter first number: ')
num2 = input('Enter second number: ')
num3 = input('Enter a string : ')

# Add two numbers.
sum = float(num1) + float(num2)
print('The sum of two numbers is : %s' %sum)

#Substract two numbers 
diff = float(num1) - float(num2)
print('The difference of two numbers is : %s' %diff)

#Product of two numbers 
product = float(num1) * float(num2)
print('The product of two numbers is : %s' %product)

#Remainder of two numbers 
rem = float(num1) % float(num2)
print('The remainder of two numbers is : %s' %rem)

#Division of two numbers 
div = float(num1) / float(num2)
print('The division of two numbers is : %s' %div)

#Power function using two numbers 
power = float(num1) ** float(num2)
print('The value is : %s' %power)

x = print(sum > diff)
y = print(sum <= product)
z = print(div != diff)

print('a' in num3)



