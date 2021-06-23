# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 12:41:13 2020

@author: YUKTI_PC
"""

class Example:
    myVariable = "some value"
#init is used for initialisation and new are used to define/create objs of constuctor 
    def __init__(self, para1):
         self.myVariable = para1
         return self.myVariable
    def __new__(self):
        return 'ncu students'
#destructor- destroying the object or other aspects
    def __del__(self):
        return 'ncu student destroyed'
#creating object of the class Example()
mutantObj = Example()
print(mutantObj)
simpleObj = Example('collegestudents')
print(simpleObj)


#Name manging :
# Public - normal self.myVariable is defined
# Protected - self._myVariable is defined[_ is mandatory]
# Private - uses two __ for defination like self._""_myVariable(to call some function
#or access some variable that are private use obj._classname_""_myvarible)
# for making child/subcass define it in the the brackets class Child(Example)

#Abstract class - declaration id done without implementation and doesnt have objects made
#needs subclass to be implemented
from abc import ABC
class Polygons(ABC):
    
    def noofsides(self):
        pass
class Triangle(Polygons):
    #overriding the ab-class    
    def noofsides(self):
        print("I have 3 sides")
        
        
#UML Example:
        
#get and set functions(Composition)
class XY(object):
    def  __init__(self,x,y):
        self.__xCo = x
        self.__yCo = y
    
    def getXY(self):
        return (self.__xCo, self.__yCo)
    
    def setXY(self,x,y):
        self.__xCo = x
        self.__yCo = y
        
#add and remove function(Aggregation)
class ShapeCollection:
    def __init__(self):
        self.__collection = []
    
    def add(self, shape):
        self.__collection.append(shape)
    def remove(self,shape):
        self.__collection.remove(shape) 
        
#__str__ function is called when an obj is displayed using print function it
#produces a str representation of an obj value that is more redable by humans
#__repr__ function is called when the value of an obj display in the python shell it
#produces a str represenrtation that python can evaluate
#Arithmetic operator to fraction class are __neg__ , __add__, __sub__, __mul__
#Relation operator to fraction class are __lt__, __le__, __eq__, __ne__, __ge__ , __gt__

 
        
    
        

