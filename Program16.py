# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 11:56:18 2020

@author: YUKTI_PC
"""
class Person:
    def __init__(self, name, surname, birthyear, address, telephone, email):
        self.name = name
        self.surname = surname
        self.birthyear = birthyear

        self.address = address
        self.telephone = telephone
        self.email = email
        

person1 = Person("Jane", "Doe", "1992", "No. 12 Short Street, Greenville",
                 "9971956382", "jane.doe@example.com")
person2 = Person("David", "Tennant", "1971", "Bathgate, West Lothian, Scotland",
                 "9874560987", "david.tennant@example.com")
person3 = Person("Michael", "Sheen", "1969", "Newport, Wales",
                 "845645987", "michael.sheen@example.com")
person4 = Person("Benedict", "Cumberbatch", "1976", "Hammersmith, London, England",
                 "945645987", "benedict.cumberbatch@example.com")
person4 = Person("Benedict", "Cumberbatch", "1976", "Hammersmith, London, England",
                 "985638287", "benedict.cumberbatch@example.com")
person5 = Person("Robert", "Downey", "1965", "Manhattan, New York, United States",
                 "954645987", "robert.dowmey@example.com")


print("Name of person1 is :" ,person1.name, person1.surname)
print("Birth year of person2 is :" , person2.birthyear)
print("Address of person3 is :" , person3.address)
print("Telephone no. of person4 is :",person4.telephone)
print("Email of person5 is :",person5.email)
