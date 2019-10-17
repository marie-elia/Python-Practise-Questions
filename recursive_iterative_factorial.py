# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 19:43:56 2019

@author: marie
"""

n = 4
fact=1 

  
for i in range(1,n+1): 
    fact = fact * i 
      
print ("The factorial  is : ",end="") 
print (fact) 


#recursive factorial
def recur_factorial(n):
   """Function to return the factorial
   of a number using recursion"""
   if n == 1:
       return n
   else:
       return n*recur_factorial(n-1)

print(recur_factorial(4))