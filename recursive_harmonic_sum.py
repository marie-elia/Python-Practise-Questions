# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 02:54:32 2019

@author: marie
"""

def harmonic_sum(n):
  if n < 2:
    return 1
  else:
    return 1 / n + (harmonic_sum(n - 1))
    
print(harmonic_sum(7))
print(harmonic_sum(4))