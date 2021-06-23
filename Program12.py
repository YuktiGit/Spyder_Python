# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 11:36:00 2020

@author: YUKTI_PC
"""

thisdict = {
  "Brand": "Ford",
  "Model": "Mustang",
  "Year": 1999
}
print("Original dictionary : ")
for x, y in thisdict.items():
  print(x, y)

thisdict["Year"] = 2018

z = thisdict.get("Model")
print("The model of car is :")
print(z)
      
print("Dictionary after change : ")
for x, y in thisdict.items():
  print(x, y)
 