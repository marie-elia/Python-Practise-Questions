# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 22:08:25 2019

@author: marie
"""

num1=int(input("input a number"))
num2=int(input("input a number"))
num3=int(input("input a number"))


if num2>num1:
    maximum=num2
else:
    maximum=num1  
if  num3>maximum:
    maximum=num3
print(maximum)    
    