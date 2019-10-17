# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 21:53:51 2019

@author: marie
"""

def reverse(s,n):
   # k=[]
    summ=0
    for i in range(0,len(s),n):
        k=s[i:summ]
        summ=summ+n
        k[::-1]
        print(k)
        
reverse("kmjkjjkre",2)