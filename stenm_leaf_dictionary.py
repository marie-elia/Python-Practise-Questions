digits = [
    112, 72, 69, 97, 107, 73, 92, 76, 86, 73,
    126, 128, 118, 127, 124, 82, 104, 132, 134, 83,
    92, 108, 96, 100, 92, 115,76, 91, 102, 81,
    95, 141, 81, 80, 106, 84, 119, 113, 98, 75,
    68, 98, 115, 106, 95, 100, 85, 94, 106, 119
]

#Initialized a list with the numbers

print(digits)   #for checking purposes 
stem_dict = {}     #created a new dictionary called stem_dict

for digit in digits:            # created a for loop to iterate over the digits in my list 
    stem = str(digit)[:-1]      #i store the digit except the last number in stem
    leaf = str(digit)[-1]    
    #i store only the alst number in leaf

    if stem in stem_dict:                       #an if statement to check whether the stem already exists or not, if it does add the leaf
        stem_dict[stem].append(int(leaf))
    else:                                       #else add the stem and the leaf. 
        stem_dict[stem] = [int(leaf)]    
print(stem_dict)

stem_dict = {int(k) : v for k, v in stem_dict.items()}      #I then transofrmed the keys into integers so that it can be sorted numerically 
stem_dict = dict(sorted(stem_dict.items()))                 #I then used the sorted function to sort the dictionary items in a new dictionry called dict, then i put the dict in stem_dict

for key, leaf in stem_dict.items():                         #After that, i used .sort to sort the leaf
    leaf.sort()

print(stem_dict)