def create_phone_number(n):
    # convert list of int numbers to string numbers 
    # first we need to convert all numbers in list to string not integer 
    lst = [*map(str, n)]
    # now join all these string nums to one string  
    phone_number = "".join(lst)
    
    # basic slicing 
    return f"({phone_number[:3]}) {phone_number[3:6]}-{phone_number[6:]}"
#pythonic solution 
def create_phone_number_v2(numbers):

    return "({}{}{}) {}{}{}-{}{}{}{}".format(*numbers)


# test 

print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))