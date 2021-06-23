# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 20:44:42 2020

@author: YUKTI_PC
"""

	
a, b, i, j, flag = 0, 0, 0, 0, 0

print("Enter lower bound of the interval:", end = "") 
a = int(input())

print("Enter upper bound of the interval:", end = "") 
b = int(input())

print("Prime numbers between", a, "and", b, "are:", end = "") 
    
for i in range(a, b + 1): 
	if (i == 1): 
		continue
	flag = 1
		
	for j in range(2, i // 2 + 1): 
		if (i % j == 0): 
			flag = 0
			break
	if (flag == 1): 
		print(i, end = " ") 
			
