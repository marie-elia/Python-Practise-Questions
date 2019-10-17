# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 23:54:21 2019

@author: marie
"""

class IOString():
    def __init__(self):
        self.str1 = ""

    def get_String(self):
        self.str1 = input("enter the word: ")

    def print_String(self):
        print(self.str1.upper())



str1 = IOString()
str1.get_String()
str1.print_String()