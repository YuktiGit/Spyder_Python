# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 12:42:22 2020

@author: YUKTI_PC
"""

# fruit = [] 

# size = int(input("Enter size of list : ")) 

# for i in range(size): 

#     str = input("Enter fruit name: ") 

#     fruit.append(str) 

# str = input("Enter new fruit to add: ") 

# fruit.append(str) 

# print("Enter index and name of fruit to add at particular place.") 

# index = int(input("Index : ")) 

# str = input("Fruit name : ") 

# fruit.insert(index,str) 

# print("Enter two fruit names to add in list.") 

# str1 = input("first fruit name : ") 

# str2 = input("second fruit name : ") 

# fruit.extend([str1,str2]) 

# print("Entered fruit list.") 

# for fr in fruit: 

#     print(fr,end="  ") 

# str1 = input("Enter fruit you want to delete: ") 

# fruit.remove(str1) 

# str2 = int(input("Enter index of fruit you want to delete: ")) 

# del fruit[str2] 

# str3 = int(input("Enter index of fruit you want to delete: ")) 

# letter = fruit.pop(str3) 

# print(letter+" is deleted") 

# for fr in fruit: 

#     print(fr,end="  ") 
    
    
    
    
    
    
    
    
fruit_list = ['apple', 'orange', 'mango']
i = 0
print("Fruit list contain following fruits : ")
for x in fruit_list:
    print(fruit_list[i])
    i += 1

print("1. Append ")
print("2. Extend ")
print("3. Insert ")
print("4. Delete ")
print("5. Remove ")
print("6. Pop ")

ch = int(input("Enter the action to be performed :"))
if (ch == 1):
    print("Enter the fruit to be appended :")
    a = input()
    fruit_list.append(a)
elif (ch == 2):
    b = input("Enter the fruit to be extended :")
    fruit_list.extend(b)
elif (ch == 3):
    c = input("Enter the fruit to be inserted :")
    fruit_list.insert(c)
elif (ch == 4):
    print("the length of the fruit list is ",len(fruit_list))
    d = int(input("Enter the index of the fruit to be deleted :"))
    del fruit_list[d]
elif (ch == 5):
    e = input("Enter the fruit to be removed :")
    fruit_list.remove(e)
elif (ch == 6):
    f = input("Enter the fruit to be poped :")
    fruit_list.pop(f)
else :
    print("Enter a valid option")

j = 0
print("Fruit list now contain following fruits : ")
for x in fruit_list:
    print(fruit_list[j])
    j += 1
     
    
    
    
    
    
    
    
    
    
    
    