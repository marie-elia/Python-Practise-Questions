# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 23:24:06 2019

@author: marie
"""

import random
def oneRun(rangem):
    listt=[]
    num=random.randrange(1, rangem)
    while True:
        listt.append(num)
    print(listt)
    

oneRun(12)