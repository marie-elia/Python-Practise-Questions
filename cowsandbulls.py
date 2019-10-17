# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 18:55:13 2019

@author: marie
"""

import random
game=True
k=str(random.randrange(1000,9999))
print(k)
while(game!=False):
    countercows=0
    countbu=0
    
    num=input("enter the number")
    for i in range(4):
        if k[i]==num[i]:
            countercows+=1   
        elif num[i]!=k[i] and num[i]in k :
            countbu+=1
    print(str(countbu)+" bulls")
    print(str(countercows)+" cows")
    if countercows==4:
        game=False