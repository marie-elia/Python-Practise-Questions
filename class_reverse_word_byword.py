# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 23:52:00 2019

@author: marie
"""

class py_solution:
    def reverse_words(self, s):
        return ' '.join(reversed(s.split()))


print(py_solution().reverse_words('hello .py'))