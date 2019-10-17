# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 03:13:07 2019

@author: marie
"""

# Returns number of pairs in arr[0..n-1]  
# with sum equal to 'sum' 
def getPairsCount(arr, n, sum): 
      
    count = 0 # Initialize result 
  
    # Consider all possible pairs 
    # and check their sums 
    for i in range(0, n): 
        for j in range(i + 1, n): 
            if arr[i] + arr[j] == sum: 
                count += 1
                print(arr[i])
                print(arr[j])
                print()
      
    return count 
  
# Driver function  
arr = [1, 5, 7, -1, 5] 
n = len(arr) 
sum = 6
print("Count of pairs is", 
      getPairsCount(arr, n, sum)) 