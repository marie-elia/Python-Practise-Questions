# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 02:26:05 2019

@author: marie
"""

ld_dict = {'A': 67, 'B': 23, 'C': 45, 'D': 56, 'E': 12, 'F': 69, 'G': 67, 'H': 23} 
  
new_dict = dict([(value, key) for key, value in old_dict.items()]) 
    
# Printing original dictionary  
print ("Original dictionary is : ") 
print(old_dict)  
  
print() 
  
# Printing new dictionary after swapping keys and values 
print ("Dictionary after swapping is :  ")  
print("keys: values") 
for i in new_dict: 
    print(i, " :  ", new_dict[i]) 