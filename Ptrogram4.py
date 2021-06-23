# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 20:05:30 2020

@author: YUKTI_PC
"""

#Dictionaries
d = {'a' : 1, 'b' : 2, 'c' : 3}
dd = dict(d:4,e:5,f:6)
s = d.update(dd)
print(s)
d.items()
d.keys
d.fromkeys('a')

#Tuples
t = (1, 2, 7, 4)
# temp = list(t)
# temp.sort()
# T = tuple(temp)
sorted(t)
l = [x+10 for x  in t]
t.count(x)
#cant change the tuple but 
#can change the mutablr inside the tuple 

a = 10
def foo():
    global a
    a += 10
foo()
print(a)

def intersect(seq1,seq2):
    res = []
    for x in seq1:
        if x in seq2:
            res.append(x)
    return res
s1 = "Yukti"
s2 = "Yukta"
print(intersect(s1,s2))
#one more way to neglect all the above step
#print([x for x in s1 if x in s2])



