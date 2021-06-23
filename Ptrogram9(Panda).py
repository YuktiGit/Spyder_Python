# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 21:21:14 2020

@author: YUKTI_PC
"""

#PANDAS

#Series is same as numpy array what diff os series have axis labels 

import numpy as np
import pandas as pd

pd.Series(data = name of the list/array/dict)
pd.Series(data=my_list,index=labels)/ pd.Series(my_list,labels)
pd.Series(arr/d,label(op))
#we can perform operations on series
ser1 + ser2

# Dataframes - came from r programming languege are the workhorses of panda
df = pd.DataFrame(randn(5,4),index='A B C D E'.split(),columns='W X Y Z'.split())
df['W']['B']#gives value
df[['W','Z']]#gives rows and columns
df.W#whole w column
df['new'] = df['W'] + df['Y']#creating new column
 df.drop(W,axis=1/0,inplace = true/false)#removing
  #1=colm and 0=row  true = original pe changes and false = copy of the original\
      
#Now for rows
 df.loc['A'/2]
 df.iloc[1]
 df.loc['B','Y']#value
 df.loc[['A','B'],['W','Y']]#both rows and colms table
 df[df['W']>0][['Y','X']]#table
 df[df>0]
 df[(df['W']>0) & (df['Y'] > 1)]#multiple conditions
 newind = 'CA NY WY OR '.split()#split the ele and insert in variable
 df['States'] = newind#variable one by one insert in table
 #dataframes colm are series 
df.set_index('States',inplace=True)
 df.loc['G1']
 
 
 outside = ['G1','G1','G1','G2','G2','G2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside,inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)  #or
df = pd.DataFrame(np.random.randn(6,2),index=hier_index,columns=['A','B'])
df.loc['G1']/df.xs('G1')
df.loc['G1'].loc[1]/df.xs(['G1',1])
df.index.names = ['Group','Num']#naming colms
df.xs(1,level='Num')
#MISSING VALLES
df.dropna()#delete all rows and colms which contains nan value
 #1=colm and 0=row
df.fillna(value='FILL VALUE')#fill the nan box
df['A'].fillna(value=df['A'].mean())#in this the all nan values in a is filled
# by the mean of the values present in a
#GROUPBY METHOD
#consider data is the file which cotain data then
df = pd.DataFrame(data)
gb = df.groupby("company")#by this we are aggregating or grouping the value present
# in the data file accoring to the companies now operations can be applied on them
#the groupby make a object which can be then stored in a variable on which op are performed
 gb.mean()
 gb.min()/max()
 gb.count()
 gb.discribe()#tells all the fuctions that can be performed t=by the varible
 gb.transpose()#rows become colms and colms become rows
#MERGING JOINING
#1. concatenation
pd.cancat([df,gb])#keep in mind the dimentions of the fames should be same to cancatenate
pd.cancat([df,gb],axis=1)#according colms
#2. merging
pd.merge(df,gb,how="inner/outter",on='key')#it is important(but optional) to
# have something in common according and on which it would merg and overlap each other
#can be any size
#3.joining is combining the dataframes using indexs 
left.join(right)#first left and then right according to left if right have extra it is ignored
#it is defualt inner if it would be outter than all the values of right and lef would be there






























