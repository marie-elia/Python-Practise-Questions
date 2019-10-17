# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 03:01:37 2019

@author: marie
"""

def Recurgcd(a, b):
	low = min(a, b)
	high = max(a, b)

	if low == 0:
		return high
	elif low == 1:
		return 1
	else:
		return Recurgcd(low, high%low)
print(Recurgcd(12,14))