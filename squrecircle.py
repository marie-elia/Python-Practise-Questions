# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 01:29:40 2019

@author: marie
"""

import turtle
import time
def draw_square():
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
turtle.color('green')
for i in range(360):
    draw_square()
    turtle.left(i)