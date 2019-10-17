# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 03:21:59 2019

@author: marie
"""

# This sums all the items in a list

def sum_list(items):
    sum_numbers = 0
    for number in items:
        sum_numbers += number
    return sum_numbers
print(sum_list([27,21,-63]))

# This multiplies all the items in a list

def multiply_list(items):
    tot = 1
    for number in items:
        tot *= number
    return tot
print(multiply_list([2,4,6]))

# This finds the maximum number in a list

def max_num_in_list(list):
  max = list[0]
  for number in list:
    if number > max:
      max = number
  return max
print(max_num_in_list([27, 2, -8, 0]))

# This finds the smallest number in a list

def smallest_num_in_list(list):
  min = list[0]
  for number in list:
    if number < min:
      min = number
  return min
print(smallest_num_in_list([27, 2, -8, 0]))

# This counts the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings

def match_words(words):
  ctr = 0

  for word in words:
    if len(word) > 1 and word[0] == word[-1]:
      ctr += 1
  return ctr

print(match_words(['aba', 'aba', 'xyz']))

# This organises the tuples in ascending order by the last element

def last(n): return n[-1]

def sort_list_last(tuples):
  return sorted(tuples, key=last)

print(sort_list_last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))

# This removes duplicates from a list

a = [10,20,30,20,10,50,60,40,80,50,40]

dup_items = set()
uniq_items = []
for x in a:
    if x not in dup_items:
        uniq_items.append(x)
        dup_items.add(x)

print(dup_items)

# This checks whether a list is empty or not

l = []
if not l:
  print("List is empty")
  
# This copies/clones the original List

original_list = [10, 22, 44, 23, 4]
new_list = list(original_list)
print(original_list)
print(new_list)

# This finds the longest words that bigger than n from a given string

def long_words(n, str):
    word_len = []
    txt = str.split(" ")
    for x in txt:
        if len(x) > n:
            word_len.append(x)
    return word_len	
print(long_words(3, "The quick brown fox jumps over the lazy dog"))

# This takes two lists and returns True if they have at least one common member

def common_data(list1, list2):
     result = False
     for x in list1:
         for y in list2:
             if x == y:
                 result = True
                 return result
print(common_data([1,2,3,4,5], [5,6,7,8,9]))
print(common_data([1,2,3,4,5], [6,7,8,9]))

# This prints a specified list after removing the 0th, 4th and 5th elements

color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color = [x for (i,x) in enumerate(color) if i not in (0,4,5)]
print(color)

# This generates a 3*4*6 3D array whose each element is *

array = [[ ['*' for col in range(6)] for col in range(4)] for row in range(3)]
print(array)

# This prints the numbers of a specified list after removing even numbers from it

num = [7,8, 120, 25, 44, 20, 27]
num = [number for number in num if number%2!=0]
print(num)

# This shuffles and prints a specified list

from random import shuffle
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
shuffle(color)
print(color)

# This generates and print a list of first and last 5 elements where the values are square of numbers between 1 and 30 (both included)

def printValues():
	l = list()
	for i in range(1,21):
		l.append(i**2)
	print(l[:5])
	print(l[-5:])

printValues()

# This generates and print a list except for the first 5 elements, where the values are square of numbers between 1 and 30 (both included)

def printValues():
	l = list()
	for i in range(1,21):
		l.append(i**2)
	print(l[5:])

printValues()

# This generates all permutations of a list in Python

import itertools
print(list(itertools.permutations([1,2,3])))

# This gets the difference between the two lists

list1 = [1, 2, 3, 4]
list2 = [1, 2]
print(list(set(list1) - set(list2)))

# This accesses the index of a list

nums = [5, 15, 35, 8, 98]
for num_index, num_val in enumerate(nums):
    print(num_index, num_val)

# This converts a list of characters into a string

s = ['a', 'b', 'c', 'd']
str1 = ''.join(s)
print(str1)

# This finds the index of an item in a specified list

num =[10, 30, 4, -6]
print(num.index(30))

# This flattens a shallow list

import itertools
original_list = [[2,4,3],[1,5,6], [9], [7,9,0]]
new_merged_list = list(itertools.chain(*original_list))
print(new_merged_list)

# This appends a list to the second list

list1 = [1, 2, 3, 0]
list2 = ['Red', 'Green', 'Black']
final_list = list1 + list2
print(final_list)

# This selects an item randomly from a list

import random
color_list = ['Red', 'Blue', 'Green', 'White', 'Black']
print(random.choice(color_list))

# This checks whether two lists are circularly identical

list1 = [10, 10, 0, 0, 10]
list2 = [10, 10, 10, 0, 0]
list3 = [1, 10, 10, 0, 0]

print('Compare list1 and list2')
print(' '.join(map(str, list2)) in ' '.join(map(str, list1 * 2)))
print('Compare list1 and list3')
print(' '.join(map(str, list3)) in ' '.join(map(str, list1 * 2)))

# This finds the second smallest number in a list

def second_smallest(numbers):
    a1, a2 = float('inf'), float('inf')
    for x in numbers:
        if x <= a1:
            a1, a2 = x, a1
        elif x < a2:
            a2 = x
    return a2
print(second_smallest([1, 2, -8, -2, 0]))

# This finds the second largest number in a list

def second_largest(numbers):
    count = 0
    n1 = n2 = float('-inf')
    for x in numbers:
        count += 1
        if x > n2:
            if x >= n1:
                n1, n2 = x, n1            
            else:
                n2 = x
    return n2 if count >= 2 else None

print(second_largest([1, 2, -8, -2, 0]))

# This gets unique values from a list

my_list = [10, 20, 30, 40, 20, 50, 60, 40]
print("Original List : ",my_list)
my_set = set(my_list)
my_new_list = list(my_set)
print("List of unique numbers : ",my_new_list)

# This gets the frequency of the elements in a list

import collections
my_list = [10,10,10,10,20,20,20,20,40,40,50,50,30]
print("Original List : ",my_list)
ctr = collections.Counter(my_list)
print("Frequency of the elements in the List : ",ctr)


# This counts the number of elements in a list within a specified range

def count_range_in_list(li, min, max):
	ctr = 0
	for x in li:
		if min <= x <= max:
			ctr += 1
	return ctr

list1 = [10,20,30,40,40,40,70,80,99]
print(count_range_in_list(list1, 40, 100))

list2 = ['a','b','c','d','e','f']
print(count_range_in_list(list2, 'a', 'e'))

# This checks whether a list contains a sublist

def is_Sublist(l, s):
	sub_set = False
	if s == []:
		sub_set = True
	elif s == l:
		sub_set = True
	elif len(s) > len(l):
		sub_set = False

	else:
		for i in range(len(l)):
			if l[i] == s[0]:
				n = 1
				while (n < len(s)) and (l[i+n] == s[n]):
					n += 1
				
				if n == len(s):
					sub_set = True

	return sub_set

a = [2,4,3,5,7]
b = [4,3]
c = [3,7]
print(is_Sublist(a, b))
print(is_Sublist(a, c))

# This generates all sublists of a list

def sub_lists(my_list):
	subs = [[]]
	for i in range(len(my_list)):
		n = i+1
		while n <= len(my_list):
			sub = my_list[i:n]
			subs.append(sub)
			n += 1
	
	return subs

l1 = [10, 20, 30, 40]
l2 = ['X', 'Y', 'Z']
print(sub_lists(l1))
print(sub_lists(l2))

# This program uses Sieve of Eratosthenes method for computing primes upto a specified number, (i.e. finds all prime numbers up to a given point)

def prime_eratosthenes(n):
    prime_list = []
    for i in range(2, n+1):
        if i not in prime_list:
            print (i)
            for j in range(i*i, n+1, i):
                prime_list.append(j)

print(prime_eratosthenes(100))';
include("../../new_editor/editor_python.php")

# This creates a list by concatenating a given list which range goes from 1 to n

my_list = ['p', 'q']
n = 4
new_list = ['{}{}'.format(x, y) for y in range(1, n+1) for x in my_list]
print(new_list)

# This gets variable unique identification number or string

x = 100
print(format(id(x), 'x'))
s = 'w3resource'
print(format(id(s), 'x')) 

# This finds common items from two lists

color1 = "Red", "Green", "Orange", "White"
color2 = "Black", "Green", "White", "Pink"
print(set(color1) & set(color2))

# This changes the position of every n-th value with the (n+1)th in a list

from itertools import zip_longest, chain, tee
def replace2copy(lst):
    lst1, lst2 = tee(iter(lst), 2)
    return list(chain.from_iterable(zip_longest(lst[1::2], lst[::2])))
n = [0,1,2,3,4,5]
print(replace2copy(n))

# This converts a list of multiple integers into a single integer

L = [11, 33, 50]
print("Original List: ",L)
x = int("".join(map(str, L)))
print("Single Integer: ",x)

# This splits a list based on first character of word

from itertools import groupby
from operator import itemgetter

word_list = ['be','have','do','say','get','make','go','know','take','see','come','think',
     'look','want','give','use','find','tell','ask','work','seem','feel','leave','call']

for letter, words in groupby(sorted(word_list), key=itemgetter(0)):
    print(letter)
    for word in words:
        print(word)



