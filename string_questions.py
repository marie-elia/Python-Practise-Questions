# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 03:21:04 2019

@author: marie
"""

# This calculates the length of a string:

def string_length(rajive):
  count = 0
  for n in rajive:
    count += 1
  return count
print(string_length("rajive"))

# This counts the character frequency within a string:

def char_frequency(rajive):
  dict = {}
  for n in rajive:
      keys = dict.keys()
      if n in keys:
          dict[n] += 1
      else:
          dict[n] = 1
  return dict
print(char_frequency("rajive"))

# This combines the first 2 and last 2 letters of a string, any string with less than 2 letters will output an empty string

def string_both_ends(rajive):
  if len(rajive) < 2:
    return ""

  return rajive[0:2] + rajive[-2:]

print(string_both_ends("rajive"))

# This replaces a letter in a string to a $ symbol

def change_char(rajive):
  char = rajive[0]
  length = len(rajive)
  rajive = rajive.replace(char, "$")
  rajive = char + rajive[1:]
  return rajive
print(change_char("restart"))

# This gives a single string from 2 strings, and swaps the first 2 characters of EACH string

def chars_mix_up(Andi, Mack):
  new_Andi = Mack[:2] + Andi[2:]
  new_Mack = Andi[:2] + Mack[2:]
  
  return new_Andi + " " + new_Mack
print(chars_mix_up("Andi", "Mack"))

# This allows you to add 'ing' at the end of a given string when the length is at least 3. If it already ends with 'ing' then end it with 'ly'. If the length of the string is less than 3, then leave it unchanged!

def add_string(rajive):
  length = len(rajive)
  
  if length > 2:
    if rajive[1:3] == 'ing':
      rajive += 'ly'
    else:
      rajive += 'ing'
  
  return rajive
print(add_string("rajive"))

# This finds the first appearance of the substring 'not' and 'poor' from a given string. If 'bad' follows 'poor' replace the whole 'not'...'poor' substring with 'good'.

def not_poor(rajive):
  snot = rajive.find('not')
  sbad = rajive.find('poor')
  
  if sbad > snot:
    rajive = rajive.replace(rajive[snot:(sbad+4)], 'legendary')
  
  return rajive
print(not_poor('rajive is not poor!'))

# This takes a list of words and returns the length of the longest word

def find_longest_word(words_list):
    word_len = []
    for n in words_list:
        word_len.append((len(n), n))
    word_len.sort()
    return word_len[-1][1]

print(find_longest_word(["Clash Royale", "Call of Duty", "Fifa"]))

# This removes a n^th index character of a string

def remove_char(str, n):
      first_part = str[:n] 
      last_part = str[n+1:]
      return first_part + last_part
print(remove_char('rajive', 0))
print(remove_char('prison break', 3))
print(remove_char('call of duty', 5))

# This changes the old string into a new string, it also exchanges the first and last characters of string

def change_sring(str1):
      return str1[-1:] + str1[1:-1] + str1[:1]
	  
print(change_sring('rajive'))
print(change_sring('clash royale'))

# This removes the odd index characters of a string

def odd_values_string(str):
  result = "" 
  for i in range(len(str)):
    if i % 2 == 0:
      result = result + str[i]
  return result

print(odd_values_string('Pokemon'))
print(odd_values_string('Call of Duty'))

# This counts the occurence of each word in a given sentence

def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

print( word_count('the quick brown fox jumps over the lazy dog.'))

# This takes the input from a user and displays it in both upper and lower case in the console

user_input = input("What's your favourite language? ")
print("My favourite language is ", user_input.upper())
print("My favourite language is ", user_input.lower())

# This accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically).

items = input("Input comma separated sequence of words")
words = [word for word in items.split(",")]
print(",".join(sorted(list(set(words)))))

# This creates the HTML string with tags around the word(s)

def add_tags(tag, word):
	return "<%s>%s" % (tag, word, tag)
print(add_tags('i', 'Python'))
print(add_tags('b', 'Python Tutorial'))

# This inserts a string in the middle of a string

def insert_sting_middle(str, word):
	return str[:2] + word + str[2:]

print(insert_sting_middle('[[]]', 'Python'))
print(insert_sting_middle('{{}}', 'PHP'))
print(insert_sting_middle('<<>>', 'HTML'))

# This creates 4 copies of the last two characters of a specified string (length must be at least 2)

def insert_end(str):
	sub_str = str[-2:]
	return sub_str * 4

print(insert_end('Python'))
print(insert_end('Exercises'))

# This gets a string made of its first three characters of a specified string. If the length of the string is less than 3 then return the original string


def first_three(str):
	return str[:3] if len(str) > 3 else str

print(first_three('ipy'))
print(first_three('python'))
print(first_three('py'))

# This gets the last part of a string before a specified character

str1 = 'http://www.w3resource.com/python-exercises/string'
print(str1.rsplit('/', 1)[0])
print(str1.rsplit('-', 1)[0])

# This reverses a string if it's length is a multiple of 4

def reverse_string(str1):
    if len(str1) % 4 == 0:
       return ''.join(reversed(str1))
    return str1

print(reverse_string('abcd'))
print(reverse_string('python'))

# This converts a given string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters

def to_uppercase(str1):
    num_upper = 0
    for letter in str1[:4]: 
        if letter.upper() == letter:
            num_upper += 1
    if num_upper >= 2:
        return str1.upper()
    return str1

print(to_uppercase('Python'))
print(to_uppercase('PyThon'))

# This sorts a string lexicographically

def lexicographi_sort(s):
    return sorted(sorted(s), key=str.upper)

print(lexicographi_sort('w3resource'))
print(lexicographi_sort('quickbrown'))

# This removes a newline in Python

str1='Python Exercises\n'
print(str1)
print(str1.rstrip())

# This checks whether a string starts with specified characters

# This creates a Caesar encryption

#https://gist.github.com/nchitalov/2f2b03e5cf1e19da1525
def caesar_encrypt(realText, step):
	outText = []
	cryptText = []
	
	uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

	for eachLetter in realText:
		if eachLetter in uppercase:
			index = uppercase.index(eachLetter)
			crypting = (index + step) % 26
			cryptText.append(crypting)
			newLetter = uppercase[crypting]
			outText.append(newLetter)
		elif eachLetter in lowercase:
			index = lowercase.index(eachLetter)
			crypting = (index + step) % 26
			cryptText.append(crypting)
			newLetter = lowercase[crypting]
			outText.append(newLetter)
	return outText

code = caesar_encrypt('abc', 2)
print()
print(code)
print()

# This displays formatted text (width=50) as output

import textwrap
sample_text = '''
  Python is a widely used high-level, general-purpose, interpreted,
  dynamic programming language. Its design philosophy emphasizes
  code readability, and its syntax allows programmers to express
  concepts in fewer lines of code than possible in languages such
  as C++ or Java.
  '''
print()
print(textwrap.fill(sample_text, width=50))
print()

# This removes existing indentation from all of the lines in a given text

import textwrap
sample_text = '''
    Python is a widely used high-level, general-purpose, interpreted,
    dynamic programming language. Its design philosophy emphasizes
    code readability, and its syntax allows programmers to express
    concepts in fewer lines of code than possible in languages such
    as C++ or Java.
    '''
text_without_Indentation = textwrap.dedent(sample_text)
print()
print(text_without_Indentation )
print()

# This adds a prefix text to all of the lines in a string

import textwrap
sample_text ='''
    Python is a widely used high-level, general-purpose, interpreted,
    dynamic programming language. Its design philosophy emphasizes
    code readability, and its syntax allows programmers to express
    concepts in fewer lines of code than possible in languages such
    as C++ or Java.
    '''
text_without_Indentation = textwrap.dedent(sample_text)
wrapped = textwrap.fill(text_without_Indentation, width=50)
#wrapped += '\n\nSecond paragraph after a blank line.'
final_result = textwrap.indent(wrapped, '> ')
print()
print(final_result)
print()

# This sets the indentation of the first line

import textwrap
sample_text ='''
Python is a widely used high-level, general-purpose, interpreted, dynamic
programming language. Its design philosophy emphasizes code readability,
and its syntax allows programmers to express concepts in fewer lines of
code than possible in languages such as C++ or Java.
    '''

text1 =  textwrap.dedent(sample_text).strip()
print()
print(textwrap.fill(text1,
                    initial_indent='',
                    subsequent_indent=' ' * 4,
                    width=80,
                    ))
print()

# This prints the following floating numbers upto 2 decimal places

x = 3.1415926
y = 12.9999
print("\nOriginal Number: ", x)
print("Formatted Number: "+"{:.2f}".format(x));
print("Original Number: ", y)
print("Formatted Number: "+"{:.2f}".format(y));
print() 

# This prints the following floating numbers upto 2 decimal places with a sign

x = 3.1415926
y = -12.9999
print("\nOriginal Number: ", x)
print("Formatted Number with sign: "+"{:+.2f}".format(x));
print("Original Number: ", y)
print("Formatted Number with sign: "+"{:+.2f}".format(y));
print()

# This prints the following floating numbers with no decimal places

x = 3.1415926
y = -12.9999
print("\nOriginal Number: ", x)
print("Formatted Number with no decimal places: "+"{:.0f}".format(x));
print("Original Number: ", y)
print("Formatted Number with no decimal places: "+"{:.0f}".format(y));
print()

# This prints the following integers with zeros on the left of specified width

x = 3
y = 123
print("\nOriginal Number: ", x)
print("Formatted Number(left padding, width 2): "+"{:0>2d}".format(x));
print("Original Number: ", y)
print("Formatted Number(left padding, width 6): "+"{:0>6d}".format(y));
print()

# This prints the following integers with '*' on the right of specified width

x = 3
y = 123
print("\nOriginal Number: ", x)
print("Formatted Number(right padding, width 2): "+"{:*< 2d}".format(x));
print("Original Number: ", y)
print("Formatted Number(right padding, width 6): "+"{:*< 6d}".format(y));
print()

# This displays a number with a comma separator

x = 3000000
y = 30000000
print("\nOriginal Number: ", x)
print("Formatted Number with comma separator: "+"{:,}".format(x));
print("Original Number: ", y)
print("Formatted Number with comma separator: "+"{:,}".format(y));
print()

# This formats a number with a percentage

x = 0.25
y = -0.25
print("\nOriginal Number: ", x)
print("Formatted Number with percentage: "+"{:.2%}".format(x));
print("Original Number: ", y)
print("Formatted Number with percentage: "+"{:.2%}".format(y));
print()

# This displays a number in left, right and center aligned of width 10

x = 22
print("\nOriginal Number: ", x)
print("Left aligned (width 10)   :"+"{:< 10d}".format(x));
print("Right aligned (width 10)  :"+"{:10d}".format(x));
print("Center aligned (width 10) :"+"{:^10d}".format(x));
print()

# This counts occurrences of a substring in a string

str1 = 'The quick brown fox jumps over the lazy dog.'
print()
print(str1.count("fox"))
print()

# This reverses a string

def reverse_string(str1):
    return ''.join(reversed(str1))
print()
print(reverse_string("abcdef"))
print(reverse_string("Python Exercises."))
print()

# This reverses words in a string

def reverse_string_words(text):
    for line in text.split('\n'):
        return(' '.join(line.split()[::-1]))
print(reverse_string_words("The quick brown fox jumps over the lazy dog."))
print(reverse_string_words("Python Exercises."))



