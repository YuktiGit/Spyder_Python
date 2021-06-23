# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 21:37:12 2020

@author: YUKTI_PC
"""

def temperature(t):
    def celsius2fahrenheit(x):
       return 9 * x / 5 + 32
    result = "It's " + str(celsius2fahrenheit(t)) + " degrees!" 
    return result
print(temperature(20))

def g():
    print("Hi, it's me 'g'")
    print("Thanks for calling me")
    
def f(func):
    print("Hi, it's me 'f'")
    print("I will call 'func' now")
    print(func(20))
print(f(temperature))
 

def f(x):
    def g(y):
        return y + x + 3 
    return g
nf1 = f(1) # x=1
nf2 = f(3) # x=3
print(nf1(1)) # y=1
print(nf2(1)) # y=1


#A simple decorator
def our_decorator(func):
    def function_wrapper(x):
        print("Before calling " + func.__name__)
        func(x)
        print("After calling " + func.__name__)
    return function_wrapper
@our_decorator()
def foo(x):
    print("Hi, foo has been called with " + str(x))
print("We call foo before decoration:")
foo("Hi")
print("We now decorate foo with f:")
# we can also use this here instead of @ --> foo = our_decorator(foo)
print("We call foo after decoration:")
foo(42)



