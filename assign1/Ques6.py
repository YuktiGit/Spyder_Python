# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 22:30:17 2020

@author: YUKTI_PC
"""
print("Find perimeter and area of following : ")

print("1. Square")
print("2. Rectangle")
print("3. Triangle")
print("4. Circle")

ch= int(input("Enter you choise : "))
if ch == 1:
    a = int(input("Enter the side of square : "))
    print("Perimeter of square is : ", 4*a , "m")
    print("Area of square is : ", a*a, "m sqr")

elif ch == 2:
    a = int(input("Enter the side 1 of rectangle : "))
    b = int(input("Enter the side 2 of rectangle : "))
    print("Perimeter of rectangle is : ", 2*(a+b), "m")
    print("Area of rectangle is : ", a*b, "m sqr")

elif ch == 3:
    a = int(input("Enter the side 1 of triangle : "))
    b = int(input("Enter the side 2 of triangle : "))
    c = int(input("Enter the side 3 of triangle : "))
    print("Perimeter of triangle is : ", a+b+c, "m")
    bs = int(input("Enter the base of triangle : "))
    h = int(input("Enter the height of triangle : "))
    print("Area of triangle is : ", 0.5*bs*h , "m sqr")

elif ch == 4:
    r = int(input("Enter the radius of circle : "))
    print("Perimeter of circle is : ", 2*3.14*r, "m")
    print("Area of circle is : ", r*r*3.14, "m sqr" )

else:
    print("Please enter a valid choise!!")


    