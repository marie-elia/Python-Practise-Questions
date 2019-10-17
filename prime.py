# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 03:03:11 2019

@author: marie
"""
prime=int(input("enter number"))


for i in range (2,prime,1):
    if prime%i==0  :
        print("not prime")
        break
else :
    print(" prime")
        



