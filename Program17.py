# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 11:56:20 2020

@author: YUKTI_PC
"""
#INHERITENCE
class Animal:
	multicellular = True
	eukaryotic = True
    
	def breath(self):
           pass
	def feed(self):
           pass 

class Mammal(Animal):
	haveMammaryGland = True
	warmBlood = True
	def produceMilk(self):
           pass

class Amphibian(Animal):
	liveInWater = True
	def metamorphosis(self):
           pass 
    
Frog = Amphibian()
Frog.breath()
Frog.metamorphosis()    
print ("Do frogs live in water : ",Frog.liveInWater)
 


#ENCAPSULATION
class Computer:

    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()
c.sell()

c.__maxprice = 1000
c.sell()

c.setMaxPrice(1000)
c.sell()






#POLYMORPHISM
class Animal:
	multicellular = True
	eukaryotic = True
    
	def breathe(self):
	    print("I breathe oxygen.")
        
	def feed(self):
	    print("I eat food.")
        
#Child class Herbivores has overridden method feed()
class Herbivorous(Animal):
	def feed(self):
	    print("I eat only plants. I am vegetarian.")

obj = Herbivorous()
print(obj.feed())
print(obj.breathe())



class Compute:
    def area(self, x = None, y = None):
        if x != None and y != None:
            return x * y
        elif x != None:
            return x * x
        else:
            return 0
obj = Compute()

#Overloadding 
print("Area:", obj.area())
print("Area:", obj.area(2))
print("Area:", obj.area(4, 5))


