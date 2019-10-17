# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 03:02:25 2019

@author: marie
"""

def power(a,b):
	if b==0:
		return 1
	elif a==0:
		return 0
	elif b==1:
		return a
	else:
		return a*power(a,b-1)

print(power(3,4))