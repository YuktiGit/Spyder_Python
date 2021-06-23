# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 21:58:13 2020

@author: YUKTI_PC
"""


def Count(li): 
    counter = 0
    for num in li: 
        if isinstance(num, tuple): 
            break
        counter = counter + 1
    return counter 
  
li = [4, 5, 6, 10, (1, 2, 3), 11, 2, 4] 
print("Number of tuples present in", li,"is " , Count(li)) 

