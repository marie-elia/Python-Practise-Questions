# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 21:18:51 2019

@author: marie
"""

infile = open("1.txt")
content = infile.readlines()
two=open("2.txt")
content2=two.readlines()
#print(content)
#print(content2)
listt=[]
for i in range (len(content)):
    if content[i] in content2:
        listt.append(content[i])
print("ggggg")
print(listt)













infile.close()   
two.close() 
#infile = open(filename, 'w') #open the file as write to amend data 
#infile.write(''.join(content))# write the updated data
#infile.close()#close for better os performane