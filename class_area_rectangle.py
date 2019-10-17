# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 00:01:41 2019

@author: marie
"""
class Rectangle():
    def __init__(self,):
        self.x=0
        self.y=0
    def getx(self):
       self.x= int(input("choose x lenght "))
    def gety(self):
       self.y= int(input("choose y lenght "))
    def area(self) :
        print(self.y*self.x)
rec = Rectangle()

rec.getx()
rec.gety()
rec.area()

