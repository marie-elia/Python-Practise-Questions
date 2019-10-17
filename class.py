# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 01:51:11 2019

@author: marie
"""

print('he'.__add__('llo'))
print([1,2,3].__repr__())
print('a'.__le__('a'))
if'a'<='z':
    print("FDF")
class Point:
    def __init__(self, xcoord, ycoord):
        'initialize coordinates to (xcoord, ycoord)'
        self.x = xcoord
        self.y = ycoord

    # other Point methods here

    def __repr__(self):
        'canonical string representation Point(x, y)'
        return 'Point({}, {})'.format(self.x, self.y)

a = Point(3, 4)
print(a.__repr__())
from tkinter import Tk, Label 
root = Tk()
hello = Label(master = root, text = 'Hello GUI world!')
hello.pack() # widget placed against top boundary of master (default)
root.mainloop()




