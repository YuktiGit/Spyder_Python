# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 12:30:49 2020

@author: YUKTI_PC
"""

# fruit = ['banana','papaya','grapes','orange','apple','kiwi'] 
# print("Size of list is :"+str(len(fruit))) 
# name = input("Enter name of fruit you want to search in list:  ") 
# if(name in fruit): 
#     print("Entered fruit name is present in list.") 
# else:
#     print("Entered fruit name is not present in list.") 
# fruitcopy = fruit[:] 
# print("Copied list : "+str(fruitcopy)) 

fruit_list = ['apple', 'orange', 'mango', 'banana', 'kiwi']
i = 0
print("Fruit list contain following fruits : ")
for x in fruit_list:
    print(fruit_list[i])
    i += 1

print('The length of the fruit list is : ', len(fruit_list))

j = input('Enter the fruit you want to search : ')
if(j in fruit_list):
   print('The fruit is there in the pentary!!')
else:
   print('The pentary is missing this fruit!!')
copy_list = fruit_list[:]
print('The list print is copied list of fruit list :',copy_list )


        
 