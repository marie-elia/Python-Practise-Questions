# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 18:40:13 2019

@author: marie
"""

import random
k=random.randrange(1,6)
import random

s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
passlen = 8
p =  "".join(random.sample(s,passlen ))
print (p)