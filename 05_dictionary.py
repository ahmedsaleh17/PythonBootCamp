"""
Dictionary properties:
ordered, not indexing (keyed), allow duplicates but in values not keys, mutable 
"""

my_dict = {
    "a" : 10,
    "b" : 20,
    "c" : 30 
}

# print(my_dict)
my_dict['c']  = 100
# print(my_dict)

# print(dir(my_dict))
"""
'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 
'pop', 'popitem', 'setdefault', 'update', 'values'
"""


user = {
    'id' : 1,
    'age' : 20,
    'city' : 'Berlin'
}

# access 
# print(user['city'])
# print(user['name']) #keyerror 

# print(user.get('name'))  # none # return the values safely, gives none if missing 

# print(user.get('name', 'not found'))


# checks

print('id' in user)
print('name' in user)

print("all keys: ", user.keys())
print("all values: ", user.values())
print(user.items())
print(type(user)) # class dict
print(type(user.items()))  #class dict_items

print('--'*25)

# --------------------------------

# looping 
for u in user: 
    print(u)

for key, value in user.items():
    print(f"user's {key} is {value}")



print('--'*25)
# ----------------------------------------

# Add, Remove, Update 
print(user)
# {'id': 1, 'age': 20, 'city': 'Berlin'}

user['name'] = 'Ahmed'   # add

# del user['city']
user.pop('city', 'not found')
user.popitem()  # delete the last item

user['age'] = 25   # update
user.update({'age': 25, 'city' :'Ismailia'})  # update multiple keys
print(user)

print('--'*25)

# ------------------------------
# how to create a dict with a none for all keys

# user = {
#     'id' : None,
#     'name' : None, 
#     'age' : None
# }

# what if you have 20 keys you do that 

# creating Dictionary in An Elgant way

user = dict.fromkeys(['id', 'name', 'age', 'country'], None)
print(user)
user['id'] = '001'

# print(user)

#-----------------------------------

# challenge
user = {'id':1, 'name':'john', 'age': 30, 'city': 'berlin'}
# keep on pairs with string values 
# convert values to uppercase 

# user_modified = {key: value.upper() for key, value in user.items() if type(value) == str}
user_modified = {key: value.upper() for key, value in user.items() if isinstance(value, str)}

print(user_modified)