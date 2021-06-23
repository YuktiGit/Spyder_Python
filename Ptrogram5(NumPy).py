# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 13:19:02 2020

@author: YUKTI_PC
"""

#NUMPY FILE 

import numpy as np

#NumPy Introduction
#making simple array
#numpy makes only arrays
list1 = [1,2,3,4,5]
a = np.array(list1)

#some built-in-methods
np.arange(10)
np.arange(0,11,2)#2 is the gap
#zeros and ones
np.zeros((3,4))#if two brackets are put it will show error
np.ones(5)*5
#linespace
np.linspace(0,10,5)#(start, stop, num)
#eye
np.eye(5)#creates identity matrix
#random
np.random.rand(4)
np.random.randn(6,8)#-ve is included
np.random.randint(1,100,5)
#reshape
a.reshape(1,25)
#max,min,argmax,argmin
a.max()
a.argmax()#index value
a.min()
a.argmin()
#Shape attribute not method
a.reshape(25,1).shape
#data type
a.dtype


#NumPy Operations
#Airthmetic
arr = np.arange(0,11)
arr+arr
arr*a
arr-a
a/arr#for division of zeroes or infinity instead of error there is warning
a**4

#universal array functions
np.sqrt(a)
np.exp(arr)
np.max(a)#same as a.max
np.sin/cos/tan(arr)
np.log(a)



#Numpy Indexing And Selection
#Indexing
ar = np.arange(0,11)
ar[2]; ar[0:2]; ar[:]
#Broadcasting
ar[0:5] = 100
#Indexing in 2D array
arr_2d = np.array(([5,10,15],[20,25,30],[35,40,45]))
#arr_2D[row][col]
arr_2d[2,:]; arr_2d[2]
arr2d = np.zeros((10,10))
#Selection
arr = np.arange(1,11)
x = 2
arr[arr>x]
bool_arr = arr>4





































