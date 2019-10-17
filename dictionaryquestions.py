# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 02:21:24 2019

@author: marie
"""

# This sorts the dictionary by value (either in ascending or descending order)

import operator
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print('Original dictionary : ',d)
sorted_d = sorted(d.items(), key=operator.itemgetter(0))
print('Dictionary in ascending order by value : ',sorted_d)
sorted_d = sorted(d.items(), key=operator.itemgetter(0),reverse=True)
print('Dictionary in descending order by value : ',sorted_d)

# This allows you to add another key into an existing Dictionary

d = {0:10, 1:20}
print(d)
d.update({2:30})
print(d)

# This concatenates (joins) dictionaries to make one large Dictionary

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic4 = {}
for d in (dic1, dic2, dic3): dic4.update(d)
print(dic4)

# This checks whether a key is present inside a Dictionary

d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def is_key_present(x):
  if x in d:
      print('Key is present in the dictionary')
  else:
      print('Key is not present in the dictionary')
is_key_present(5)
is_key_present(9)

# This allows you to iterate of dictionaries using for loops


d = {'x': 10, 'y': 20, 'z': 30} 
for dict_key, dict_value in d.items():
    print(dict_key,'->',dict_value)
	
# This generates and prints a dictionary that contains a number between 1 and number

n=int(input("Input a number "))
d = dict()

for x in range(3,n+1):
    d[x]=x*x

print(d) 

# This prints a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys

d=dict()
for x in range(1,16):
    d[x]=x**2
print(d)  

# This merges 2 python dictionaries


d1 = {'a': 100, 'b': 200}
d2 = {'x': 300, 'y': 200}
d = d1.copy()
d.update(d2)
print(d)

# This iterates over a dictionary using for loops

d = {'Red': 1, 'Green': 2, 'Blue': 3} 
for color_key, value in d.items():
     print(color_key, 'corresponds to ', d[color_key]) 

# This sums all the items in a dictionary 

my_dict = {'data1':100,'data2':-54,'data3':247}
print(sum(my_dict.values()))

# This multiplies all the items in a dictionary

my_dict = {'data1':100,'data2':-54,'data3':247}
result=1
for key in my_dict:    
    result=result * my_dict[key]

print(result)

# This removes a key from a dictionary

myDict = {'a':1,'b':2,'c':3,'d':4}
print(myDict)
if 'a' in myDict: 
    del myDict['a']
print(myDict)

# This maps two lists into a dictionary

keys = ['red', 'green', 'blue']
values = ['#FF0000','#008000', '#0000FF']
color_dictionary = dict(zip(keys, values))
print(color_dictionary)

# This sorts a dictionary by key

color_dict = {'red':'#FF0000',
          'green':'#008000',
          'black':'#000000',
          'white':'#FFFFFF'}

for key in sorted(color_dict):
    print("%s: %s" % (key, color_dict[key]))
	
# This gets the maximum and minimum value in a dictionary

my_dict = {'x':500, 'y':5874, 'z': 560}

key_max = max(my_dict.keys(), key=(lambda k: my_dict[k]))
key_min = min(my_dict.keys(), key=(lambda k: my_dict[k]))

print('Maximum Value: ',my_dict[key_max])
print('Minimum Value: ',my_dict[key_min])

# This gets a dictionary from an object's fields

class dictObj(object):
     def __init__(self):
         self.x = 'red'
         self.y = 'Yellow'
         self.z = 'Green'
     def do_nothing(self):
         pass
test = dictObj()
print(test.__dict__)

# This removes duplicates from Dictionary

student_data = {'id1': 
   {'name': ['Sara'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
 'id2': 
  {'name': ['David'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
 'id3': 
    {'name': ['Sara'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
 'id4': 
   {'name': ['Surya'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
}

result = {}

for key,value in student_data.items():
    if value not in result.values():
        result[key] = value

print(result)

# This checks whether a dictionary is empty or not

my_dict = {}

if not bool(my_dict):
    print("Dictionary is empty")
	
# This combines two dictionary adding values for common keys

from collections import Counter
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d = Counter(d1) + Counter(d2)
print(d)

# This prints all unique values in a dictionary

L = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
print("Original List: ",L)
u_value = set( val for dic in L for val in dic.values())
print("Unique Values: ",u_value)

# This creates and display all combinations of letters, selecting each letter from a different key in a dictionary

import itertools      
d ={'1':['a','b'], '2':['c','d']}
for combo in itertools.product(*[d[k] for k in sorted(d.keys())]):
    print(''.join(combo))
	
# This finds the highest 3 values in a dictionary

from heapq import nlargest
my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}  
three_largest = nlargest(3, my_dict, key=my_dict.get)
print(three_largest) 

# This combines values in python list of dictionaries

from collections import Counter
item_list = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
result = Counter()
for d in item_list:
    result[d['item']] += d['amount']
print(result) 

# This creates a dictionary from a string

from collections import defaultdict, Counter
str1 = 'w3resource' 
my_dict = {}
for letter in str1:
    my_dict[letter] = my_dict.get(letter, 0) + 1
print(my_dict)

# This prints a dictionary in table format

my_dict = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
for row in zip(*([key] + (value) for key, value in sorted(my_dict.items()))):
    print(*row)
	
# This counts the values associated with key in a dictionary

student = [{'id': 1, 'success': True, 'name': 'Lary'},
 {'id': 2, 'success': False, 'name': 'Rabi'},
 {'id': 3, 'success': True, 'name': 'Alex'}]
print(sum(d['success'] for d in student))

# This converts a list into a nested dictionary of keys

num_list = [1, 2, 3, 4]
new_dict = current = {}
for name in num_list:
    current[name] = {}
    current = current[name]
print(new_dict)

# This sorts a list alphabetically in a dictionary

num = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}
sorted_dict = {x: sorted(y) for x, y in num.items()}
print(sorted_dict)

# This removes spaces from dictionary keys

student_list = {'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
print("Original dictionary: ",student_list)
student_dict = {x.translate({32: None}): y for x, y in student_list.items()}
print("New dictionary: ",student_list)

# This gets the top three items in a shop

from heapq import nlargest
from operator import itemgetter
items = {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
for name, value in nlargest(3, items.items(), key=itemgetter(1)):
    print(name, value)

# This gets the key, value and item in a dictionary

dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
print("key  value  count")
for count, (key, value) in enumerate(dict_num.items(), 1):
    print(key,'   ',value,'    ', count)

# This prints a dictionary line by line

students = {'Aex':{'class':'V',
        'rolld_id':2},
        'Puja':{'class':'V',
        'roll_id':3}}
for a in students:
    print(a)
    for b in students[a]:
        print (b,':',students[a][b])
		
# This checks multiple keys exists in a dictionary

student = {
  'name': 'Alex',
  'class': 'V',
  'roll_id': '2'
}
print(student.keys() >= {'class', 'name'})
print(student.keys() >= {'name', 'Alex'})
print(student.keys() >= {'roll_id', 'name'})

# This counts number of items in a dictionary value that is a list

dict =  {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
ctr = sum(map(len, dict.values()))
print(ctr)

# This sorts Counter by value

from collections import Counter
x = Counter({'Math':81, 'Physics':83, 'Chemistry':87})
print(x.most_common())

# This creates a dictionary from two lists without losing duplicate values

from collections import defaultdict
class_list = ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII']
id_list = [1, 2, 2, 3]
temp = defaultdict(set)
for c, i in zip(class_list, id_list):
    temp[c].add(i)
print(temp)

# This replaces dictionary values with their sum

def sum_math_v_vi_average(list_of_dicts):
    for d in list_of_dicts:
        n1 = d.pop('V')
        n2 = d.pop('VI')
        d['V+VI'] = (n1 + n2)/2
    return list_of_dicts 
student_details= [
  {'id' : 1, 'subject' : 'math', 'V' : 70, 'VI' : 82},
  {'id' : 2, 'subject' : 'math', 'V' : 73, 'VI' : 74},
  {'id' : 3, 'subject' : 'math', 'V' : 75, 'VI' : 86}
]
print(sum_math_v_vi_average(student_details))

# This converts a dictionary to OrderedDict

import collections
student = [("Student_name", "Alex"),
        ("ID", 5),
        ("Class", 'V'),
        ("Country", 'USA')]

student = collections.OrderedDict(student)
print(student)

# This matches key values in two dictionaries

x = {'key1': 1, 'key2': 3, 'key3': 2}
y = {'key1': 1, 'key2': 2}
for (key, value) in set(x.items()) & set(y.items()):
    print('%s: %s is present in both x and y' % (key, value))
