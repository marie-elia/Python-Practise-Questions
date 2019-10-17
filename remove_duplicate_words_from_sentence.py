# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 22:33:24 2019

@author: marie
"""

def removeduplicatewordsfromsentence(s):
    m=[]
    k=set()
    m=s.split(" ")
    #print(m)
    for i in range (len(m)):
        #print(m[i])
        l=m[i]
        print()
        #print(p)
        k.add(l)
    print(repr(k))
    for i in k:
        print (i,end=' ')
removeduplicatewordsfromsentence("Python is great and Java is also great")