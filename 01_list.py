# unpacking
# list of variables, separated by commas
person = ["Ahmed", 25, "Data Engineer", "spain"]
# name = person[0]
# age = person[1]
# role = person[2]
# country = person[3]

name, age, role, country = person
# print(name)
# print(role)


# ---------------------------------------

# using Asterisk
# RULE One asterisk (*) is allowed to use in unpacking
# what if you interested in the first and last item

name, *details, country = person
# print(name)     # string
# print(details)  # lst
# print(country)  # string

name, *details = person

# print(name)
# print(details)

*details, country = person
# print(details)
# print(country)

*details, role, country = person
# print(details)
# print(role)
# print(country)

# you can unpack any sequence
name = "Ahmed"
first, *rest = name
# print(first)
# print(rest)

# ----------------------------------
# using underscore to save memeory if you not interested

name, _, role, _ = person
# print(name)
# print(role)

# compine the power of * and _


numbers = [30, 40, 50, 70, 1, 22, 5, 4, 7]
# if you just care about the first and last one and you don't use the resources to save the rest of details
# use the * with _

first, *_, last = numbers

# print(first)
# print(last)

# -------------------------------------------------------------
# HOW TO ANALYZE THE DATA IN A LIST
"""
ANALYZE : MIN, MAX, SUM, LEN 
COMPLETENESS & EXISTIENCE CHECK : ALL, ANY
SEARCH & COUNT : COUNT, INDEX
MEMBERSHIP & IDENTITY : IN, IS 
COMPARISON :==, > , <
"""


# is operator check if 2 objects have the same address or not

numbers = [1, 4, 5, 6, 7, 2, 10]

# # the highes number
# print(max(numbers))

# # the lowest number
# print(min(numbers))

# # the sum of list
# print(sum(numbers))

# # the length of the list
# print(len(numbers))


# -------------------------------
lst = [1, "ahmed", 0]
# print(all(lst))

# print(any(lst))
# -------------------------------

# count & index


nums = [1, 4, 6, 7, 2, 4, 1, 1]
# to print all methods in the list
# print(dir(nums))
"""
'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'
"""

matrix = [["a", "b", "c"], ["f", "g", "h"]]

# print('before adding any things:')
# print(matrix)
# matrix.append(['f','f', 'f'])     # adding new row at last
# matrix.insert(0, ['a', 'a', 'a']) # adding new row at first
# print('After adding the 2 rows:')
# print(matrix)


# adding 'x' at the end of the second row
# matrix[1].append('x')
# print(matrix)

# adding 'z' at the start of the first row
# matrix[0].insert(0, 'z')
# print(matrix)


# remove the first item from the last row

# matrix[-1].pop(0)
# print(matrix)

# remove the last item of the first row
# matrix[0].pop()
# print(matrix)

# update the content of the last list
# matrix[-1] = ['c', 'c', 'c']
# print(matrix)

# update the first value in the first list
# matrix[0][0] = 'Ahmed'
# print(matrix)

# update the second item in the second list
# matrix[1][1] = "I am On the way don't hurry"

# print(matrix)
# -----------------------------------------------------------


# sorting 
letters = ['c', 'b', 'd', 'a']

# letters.sort()
# letters.sort(reverse= True)
# print(letters)


# in the nested list python sorts by the first item in each inner list 

matrix=[
    [6, 2, 1],
    [3, 5, 7],
    [1, 3, 5]
]
# inplace sort --> doesn't create a new object in the memory 
# sort inplace in the existing one 
# matrix.sort()
# print(matrix)


new_lst = sorted(letters)
# print(f"orginial list: {letters}")
# print(f"sorted list: {new_lst}" )



# reverse method: fild the list around not sorted reversed 
lst = [1, 5, 6, 7]
# lst.reverse()
# print(lst)


#  -----

# copy the list 
import copy 

matrix=[
    [6, 2, 1],
    [3, 5, 7]
]

# shallow copy 

matrix_copy = matrix.copy()

# matrix_copy.pop()
# matrix_copy[0].append('A')
# print('original:', matrix)
# print('copy    :', matrix_copy) 

# deep copy 

matrix_copy = copy.deepcopy(matrix)

# matrix_copy.pop()
# matrix_copy[0].append('A')
# print('original:', matrix)
# print('copy    :', matrix_copy) 



# testing using is operator 

# is operator : check object identity in the ram 
# return true if the 2 objects have the same address in the memeory 


lst = [
    [1, 3],
    [5, 6]
]

# assigment copy 
lst_copy = lst

# print(lst is lst_copy)



# shallow copy 

lst_copy2 = lst.copy()
# print(lst is lst_copy2)

# check the childern 
# print(lst[0] is lst_copy2[0])


# deep copy 
lst_copy3 = copy.deepcopy(lst)

# print(lst is lst_copy3)
# print(lst[0] is lst_copy3[0])

"""
HOW TO COPY?
- avoid assignmetn =    (risky and confusing)
- use .copy() for 1 simple, flat lists  []
- use copy.deepcopy() for nested lists [[],[]]
"""


# -------------------------------------------------------


# How to combine 

letters = ['a', 'b', 'c']
nums = [1, 2, 3]

comb = letters + nums

# print(comb)
# * Multiplier Operator makes multiple copies of the same list
# print(letters * 2 )

comb1 = [letters, nums]
# print(comb1)

# letters.extend(nums)
# print(letters)



# combining using zip()
ids = [101, 102, 103]
names =['ahmed', 'sarah', 'ali']
customers = list(zip(ids, names))

# python stops at the shortest list

print(customers)

# how to get them back 
# tup1, tup2 = zip(*customers)
# print(tup1)
# print(tup2)


# -----------------------------------------------------

# itertatror and the iterable : 
"""
iterable : object you can iterate over it 
any sequence in python is iterable (list, tuple, set, dictionary, strings)

iterator: object used to iterate over iterable by using next() fucntion
-- use cases look at google documenets 
https://docs.google.com/document/d/1bBNV5ET8Y-hd1_Xd8KWvz5TlOU7rrZYZaA5b6Mnrkx0/edit?usp=sharing
"""


# iterable
employees = ['ahmed', 'ali', 'sarah']
for emp in employees:
    print(emp.upper())

# -------------------------
# iterator = iter("ahmed")
# print(iterator)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# ------------------------

# enumerate ()

enumerate_object = enumerate(employees, start= 1)  # iterator
print(enumerate_object)

# print(next(enumerate_object))
# print(next(enumerate_object))
# print(next(enumerate_object))

# enumerate list 
enum_lst = list(enumerate_object) 
print(enum_lst)



"""
Enumerate Use Case 
find the exact position of the bad data in you list
"""

lst = ['ahmed', 'mona', '', 'sarah']
# for idx, name in enumerate(lst):
#     print(idx, name)


# reversed function 
reversed_object = reversed(employees)  # list_reverseiterator
# print(list(reversed_object))


"""
so this function takes an iterable and return an iterator
iter()
enumerate()
reversed()
zip()
"""



# ----------------------------------------
# map() function 
"""
used to make the data transformation in a clean way
map(function, iterable) return iterator

"""
nums_str = ['1', '2', '3']
nums_int = map(int, nums_str)
print(nums_int)  # map iterator object 
# convert it to iterable 
nums = list(nums_int)
print(type(nums[0]))  # <class 'int'>


"task: clearn up the list by removing all unwanted spaces"
names = [' ahmed', '  sarah ', ' mona   ']
# for name in  map(str.strip, names):
    # print(name)



# --------------------------------------
# filter() function 
"""

takes an iterable and return a filter iterator object 
""" 

lst = ['a', 'b', '1', 'c', '5']
just_letters = filter(str.isalpha, lst)
for l in just_letters:
    print(l)

# anotherway
just_letters = [ item  for item in lst   if item.isalpha() ]






def remove_none(nums):
    """
    remove none values from an iterable     
    :param nums: a list of numbers
    :return: a list of actual items 
    """
    result = filter(lambda x: x is not None, nums)

    return list(result)



nums = [12, 0, None, 23, None, -55, 234, 89, None, 0, 6, -12]
print("Original list:")
print(nums)
print("\nRemove None value from the said list:")
print(remove_none(nums))