# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 22:50:47 2019

@author: marie
"""

infile = open('word_freq.txt')# open the file if not found generate exception
#content = infile.read()
wordcount={}
content=infile.read()
k=content.split()
maxi=0
for word in k:
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1

for k,v in wordcount.items():
    print( k, v)
    if maxi< len(k):   
        maxi=len(k)
        maxwo=k
print("maximum word length")
print(maxi,maxwo)



infile.close()
    

def s_r():
    infile = open('word_freq.txt')# open the file if not found generate exception
    s = infile.read()
    count = [s[0], 1]
    for i in range(len(s)):
        if count[0] == s[i]:
            count[1] += 1
        else:
            print(str(count[1])+count[0], end='/')
            count=[s[i], 1]
    infile.close()
#s_r()