# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 00:44:48 2019

@author: marie
"""
import untitled0

def Experimenter (nTimes, r) :
    lstoflst=[]
    for k in range(nTimes):
        lstoflst.append(untitled0.OneRun(r))
        print(lstoflst[k])
#mini=list.min(lstoflst[k])
#print(mini)


Experimenter(3,7)


def Experimenter(n,r):
    'it prints the average and maximum and minimum number of iterations needed to get two consecutive same numbers'
    lstOflsts=[]
    for i in range(n):
        lstOflsts.append(OneRun(r))     #filling the list with the result of every iteration og OneRun func
        #print(lstOflsts[i])
    mx=0                #initiLLY equal to zero
    min= math.inf       #initially equal to infinity
    for item in lstOflsts:
        if item>mx:         #comparing items in the list with mx and assigninng the maximum to mx
            mx=item
        if item<min:        #comparing items in the list with min and assigninng the minimum to min
            min=item

    avg=sum(lstOflsts)//n #integer division of sum over length of the list
    print("minimum = {}, maximum = {}, average = {}".format(min,mx,avg))
iter= int(input('Please enter number of iterations(integer): '))
rg= int(input('Please enter your range(integer): '))
Experimenter(iter,rg)   #calling the func experimenter