# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 12:55:11 2020

@author: YUKTI_PC
"""

import numpy as np
x = np.random.random(25)
print("Original Array:")
print(x) 
xmin, xmax = x.min(), x.max()
print("Minimum and Maximum Values:")
print(xmin,"and " , xmax, "respectively")
print("Index values are : ")
print(np.argmax(x))
print(np.argmin(x))