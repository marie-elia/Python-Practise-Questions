# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 16:24:47 2019

@author: marie
"""
def isPalindrome(str): 
  
    # Run loop from 0 to len/2  
    for i in xrange(0, len(str)/2):  
        if str[i] != str[len(str)-i-1]: 
            return False
    return True
  
# main function 
s = "malayalam"
ans = isPalindrome(s) 
  
if (ans): 
    print("Yes") 
else: 
    print("No") 


def reverse(s): 
    

    return( s[::-1]) 
  
def isPalindrome(s): 
    # Calling reverse function 
    rev = reverse(s) 
  
    # Checking if both string are equal or not 
    if (s == rev): 
        return True
    return False
  
  
# Driver code 
s = "malayalam"
ans = isPalindrome(s) 
  
if ans == 1: 
    print("Yes") 
else: 
    print("No")          