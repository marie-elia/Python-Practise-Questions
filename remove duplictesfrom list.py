# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 12:54:59 2019

@author: marie
"""

dupli=[1,1,3,4,5,5,6,7,7,1,3,9,4,12,13,31,221,4,90]
def remove(listt):
    listt.sort()
    t=set()
    for i in range (len(listt)):
        t.add(listt[i])
   
    print(t)
    
    
    
        
    
remove(dupli)
