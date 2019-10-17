# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 02:05:27 2019

@author: marie
"""
from re import findall
data={1:['a','b'],2:['c','d','i'],3:['p','o','l']}
lstt=[]
for k,v,p in data.values():
    for i in range(len(v)):
        print(p[i])
        lstt.append(v[i])
print(lstt)

for i in range (len(data)):
    for j in range (len(data)):
        print(,end='')          
        print(data[j],end='  ')
