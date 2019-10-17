# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 03:05:45 2019

@author: marie
"""

def sumDigits(n):
  if n == 0:
    return 0
  else:
    return n % 10 + sumDigits(int(n / 10))

print(sumDigits(345))
print(sumDigits(45))