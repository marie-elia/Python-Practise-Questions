# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 11:53:37 2019

@author: marie
"""
# return fibonnaci of a certain number
def Fibonnaci(iterations):
    listt=[]
    summ=0
    if iterations==1:
        return 0
    elif iterations==2:
        return 1
        
    else:
        return Fibonnaci(iterations-1)+Fibonnaci(iterations-2)
#iterative fibonnaci      
def fibonacci(n):
    a = 0
    b = 1
    for i in range(0, n):
        temp = a
        a = b
        b = temp + b
    return a

# Display the first 15 Fibonacci numbers.
for c in range(0, 17):
    print(fibonacci(c))  
    
#print(Fibonnaci(9))
#listt to show fibonnaci sequence
def gen_fib():
    count = int(input("How many fibonacci numbers would you like to generate? "))
    i = 1
    if count == 0:
        fib = []
    elif count == 1:
        fib = [1]
    elif count == 2:
        fib = [1,1]
    elif count > 2:
        fib = [1,1]
        while i < (count - 1):
            fib.append(fib[i] + fib[i-1])
            i += 1

    return fib
print(gen_fib())