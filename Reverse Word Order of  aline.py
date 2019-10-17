# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 18:28:20 2019

@author: marie
"""
#line is reversed now
line=input("please enter your line ")
resu=line.split(" ")
print(resu)
k=len(resu)
for i in range(k-1,-1,-1):
    print (resu[i],end=' ')




 #another way
def reverseWord(w):
  return ' '.join(w.split()[::-1])

print(reverseWord("my life is a mess"))