# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 13:30:43 2019

@author: marie
"""

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89,89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
a.sort()
k=len(a)
bb=len(b)-2
listt=[]
for i in  range(k-2):
    if a[i]==a[i+1]:
        del a[i]
print(a)        
for l in b:
    if l in a:
        listt.append(l)
print(listt)