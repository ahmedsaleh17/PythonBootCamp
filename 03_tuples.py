my_tup = (10, 30, 20,10)

print(my_tup)  # ordered     # allow duplicates
# print(type(my_tup))
print(my_tup[0])  #indexing

# my_tup[0] = 'a'   # immutable 

tup_sorted = sorted(my_tup)   # sorted function take an iterable and return a sorted list 
print(tup_sorted)