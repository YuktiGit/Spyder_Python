# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 09:25:38 2020

@author: YUKTI_PC
"""

#INHERITENCE

class Parent:
    a = 10
    b = 100
    def doThis(self):
        s = self.a + self.b
        return s
    def doThat(self):
        m = self.a * self.b
        return m
class Child(Parent):
    x = 1000
    y = -1
    
    def doWhat(self):
        sb = self.x - self.y
        return sb
    def doNotDoThat(self):
        d = self.x / self.y
        return d
    def parentToChild(self):
        sums = Parent.a + Parent.b + self.x + self.y 
        if sums == Parent.doThis():
            return sums
#all the method and attributes are inherited by the child class but 
#vise versa is not possible 
child1 = Child()
print(child1.doThis()) 

#Mulitple inheritence
class GrandChild(Child):
    s = 90


issubclass(Child,Parent)#true or false
