# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 09:36:37 2020

@author: YUKTI_PC
"""
#Example1:
string = "SPAM"
a,b,c,d = string
print(a,b)
(e,f),g = string[:2], string[2:]
print(e,g)
h, *k = string
print(h,k)

#Example2:
L = [1,2,3,4]
L.append(5)  #can pass only one args in append and extend
L.extend((7,8))
L += [9,10]
print(L)

#Example3:
x = 'good'
y = 'morning'
z = 'india'
print(x,y,z,sep='  ',end='!!!\n')

#Example4:
text = '%s: %-.2f, %03d' % ('result' , 3.22345, 47)
print('%s: %-.2f, %03d' % ('result' , 3.22345, 47))
print(text)

#Example5:
branch = 'eggs'
choice = {'spam' : 1.23,'ham' : 1.299,'eggs' : 0.99}
print(choice[branch])
print(branch.endswith('gs'))
choice.items()
if branch in choice :
    print(choice[branch])
else :
    print("change your choice")


for x in s:
    print(x,end='\n')
#range
for x in range(len(s)):
    print(s[x],end='\n')
#zip
s1 = 'abc'
s2 = 'xyz'
print(list(zip(s1,s2)))

#Lists
l = [1,2,3]
l.append(9)
l*2
l[1:]
matrix = [[1,2,3],[4,5,6][7,8,9]]
l = []
l[0:2] = ['egg','mate']
l[1:2] = [4,5] #Relacement
l[1:1] = [8,9] #Insertion
l[1:2] = []    #Deletion
print(l)
l.extend[(8,7,4)]
l.sort() #Descending order
l.insert(#length/position,object)
l.sort(key = sr.lower,reverse=True)
l.pop() ; l.reverse()
l.index() ; l.count(object)#no.of same object occurence is counted
del l[2] ; 


#Tuples represented in () [anthing inside these paretheses]
t = (1,2,3,4,4)
t*3
temp = list(t)
temp.sort()
t = tuple(temp)
t.count(4)
t.index(3)
t.index(4,2)




a = 10
def foo(a):
    a = a + 10
foo(a)
print(a)








































































    