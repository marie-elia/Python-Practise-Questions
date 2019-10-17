# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 14:34:18 2019

@author: marie
"""

from re import findall
lstt1=findall('be.t','beetbtbelt?bet, best,belt,beet,be3t,be!t,be t')#be ay letter t
lstt2=findall('be*t','beetbtbelt?bet, best,belt,beet,be3t,be!t,be t')#be men zero lay n
lstt3=findall('be+t','beetbtbelt?bet, best,belt,beet,be3t,be!t,be t')#be men 1 ln
lstt4=findall('be?t','beetbtbelt?bet, best,belt,beet,be3t,be!t,be t')##bt aw bet
lstt5=findall('be[l,sa-r]t','beetbtbelt?bet, best,belt,beet,be3t,be!t,be t')#belt aw best
lstt6=findall('be[a-cx-z]t','beetbtbelt?bet, best,belt,beat,beyt,be!t,be t')
lstt7=findall('be[^a-cx-z]t','beetbtbelt?bet, best,belt,beat,beyt,beyt,be t')
lstt8=findall('a+','hello?bet, bestaab,belt,beat,beyt,beyt,be t')




print (lstt1)
print (lstt2)

print (lstt3)
print (lstt4)
print (lstt4)
print (lstt5)
print (lstt6)
print (lstt7)
print(lstt8)
