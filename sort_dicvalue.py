# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 01:12:46 2019

@author: marie
"""

sortvalue={0:23,1:49,2:45,3:56}
listt=[]
for k,v in sortvalue.items():
   listt.append(v)
listt.sort()
print(listt)
    
#print(sortvalue.values())
def dictionairy():  
  
 # Declaring the hash function       
 key_value ={}     
   
# Initialize value  
 key_value[2] = 56       
 key_value[1] = 2 
 key_value[5] = 12 
 key_value[4] = 24
 key_value[6] = 18      
 key_value[3] = 323 
   
 print ("Task 2:-\nKeys and Values sorted in",  
            "alphabetical order by the key  ")   
  
 # sorted(key_value) returns an iterator over the  
 # Dictionary’s value sorted in keys.   
 for i in sorted (key_value) : 
    print ((i, key_value[i]), end =" ") 
  

    # function calling 
dictionairy()    
def dictionairy():  
 # Declare hash function       
 key_value ={}     
  
# Initializing value  
 key_value[2] = 56       
 key_value[1] = 2 
 key_value[5] = 12 
 key_value[4] = 24
 key_value[6] = 18      
 key_value[3] = 323 
  
 print ("Task 1:-\n") 
 print ("Keys are") 
   
 # iterkeys() returns an iterator over the  
 # dictionary’s keys. 
 for i in sorted (key_value.keys()) :  
     print(i, end = " ") 
  

    # function calling 
dictionairy() 