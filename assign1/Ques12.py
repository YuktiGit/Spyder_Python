# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 22:17:10 2020

@author: YUKTI_PC
"""

l = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
print("Old tuple : ", l)
print("New tuple : ",[t[:-1] + (100,) for t in l])

