# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 03:07:08 2019

@author: marie
"""

def recursive_list_sum(data_list):
	total = 0
	for element in data_list:
		if type(element) == type([]):
			total = total + recursive_list_sum(element)
		else:
			total = total + element

	return total
print( recursive_list_sum([1, 2, [3,4],[5,6]]))