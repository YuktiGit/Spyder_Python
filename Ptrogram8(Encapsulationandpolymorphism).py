# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 12:40:08 2020

@author: YUKTI_PC
"""

#ENCAPSULATION
#Selected members of a class can be made inaccessible(hidden ) from the clients, refered
#to as information hiding(is a form of abstraction).
class ExplodeStr(str):
    def __init__(self,value="..."):
        str.__init__(value)
        

#POLYMORPHISM
#types are static or compile(method and operator overloadind) and 
#dynamic and runtime(virtual or overriding method) 

#Method overriding is a concept that changes implementation of a function in child class
class Animal:
    multicellular = True
    def breathe(self):
        print("I breathe oxygen")
    def feed(self):
        print("I eat to survive")
        
class Herbivorous(Animal):
    def feed(self):
        print("I eat only plants to survive")
        

#Method overloading is feature that allows a class to have more than one method 
#having the same name, if their arguments are different
#some overloading built-in functions are get_cart_len(), append_to_cart(), 
#__len__(), __add__(), __getitem__(index), etc(on ppt)
class Compute:
    def area(self, x = None, y = None):
        if x!=None and y !=None:
            return x*y
        elif x!=None :
            return x*x
        else :
            return 0
obj = Compute()
obj.area()
obj.area(2)
obj.area(3,4)