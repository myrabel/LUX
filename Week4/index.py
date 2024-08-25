#Question 2, Explaining list comprehension
'''
List comprehension:a concise way to create lists. It consists of brackets containing an expression followed by a for clause, and optionally, if clauses.
Examples:
'''
#Example 1: Creating a list of squares
squares = [x**2 for x in range(10)]

#Example 2: Filtering a list to get even numbers
evens = [x for x in range(20) if x % 2 == 0]

#Example 3: Flattening a list of lists
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [num for row in matrix for num in row]


'''Question 3 , Compound datatypes
lists : they are ordered and changeable'''
bigfive=["lion","buffalo","elephant","rhino","leopard"]

'''
tuples: they are unordered and not changeable, preferrable for defining a variable that is a constant
'''
capitals=("Nairobi","Dar es Salaam","Lagos","Kigali" )

'''
dictionaries: are key and value pairs, accessed via its key
'''
capitals={
    '254':"Kenya's code",
    '255': "Tanzania's code",
    '234':"Nigeria's code",
    '256':"Uganda's code"
}


'''
Given a dictionary with keys as letters and values as lists of letters, write a function closest_key to find the key with the input value closest to the beginning of the list.
'''
letters_dict={
    'a':['b','c','d'],
    'e':['f','g','h']
}

def closest_key(d, target):
    for key,value_list in d.items():
        if target in value_list:
            return key
    return None

print(closest_key(letters_dict, 'd'))