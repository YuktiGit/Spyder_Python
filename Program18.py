# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 13:14:48 2020

@author: YUKTI_PC
"""

import pandas as pd 

import numpy as np 

listt=[1,2,3,4,5] 

arr=np.array([1,2,3,4]) 

dictt={0:11,1:22,2:33} 

series_list=pd.Series(data=listt) 

series_arr=pd.Series(arr) 

series_dictt=pd.Series(dictt) 

print("List Series: ") 

print(series_list) 

print("Array Series: ") 

print(series_arr) 

print("Dictionary Series: ") 

print(series_dictt) 

print("Operation 1: ") 

print((series_dictt)*3+(series_list)-(series_arr)) 

print("Operation 2: ") 

print((series_arr)*(series_arr)/(series_dictt)) 