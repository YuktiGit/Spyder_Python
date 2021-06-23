# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 12:30:23 2020

@author: YUKTI_PC
"""

import numpy as np

print("Make array using arrange : " , np.arange(0,11,2))


print("Array using linspace and eye functions :")
print(np.linspace(0,10,5))
print(np.eye(5))

print("Ones and zeros in-built functions : ")
print(np.zeros((3,4)))
print(np.ones(5)*5)

print("List to Array using numpy : ")
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print("List is :" , list1)
a = np.array(list1)
print("Array is : ",a)
print("Square rooting each element of array : " , np.sqrt(a))


newarr = a.reshape(2, 3, 2)
print("After respahing the new array is: " , newarr)
