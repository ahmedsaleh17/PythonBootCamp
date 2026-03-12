
# handling error 
# try: 
#     print(5/0)
# except Exception as e: 
#     # print(dir(e))
#     # print(e.args[0])
#     # print(e.__class__)
#     print(e)

# -------------------------------------------


# try: 
#     print(aa)
# except ZeroDivisionError as e: 
#     print("you can't divide by zero")

# except Exception as e: 
#     print(f'something wrong happened which is {e}')


# --------------------------------------------

""" 'else' block will be executed if there is no errors raised"""

try: 
    print('aa')
except ZeroDivisionError as e: 
    print("you can't divide by zero")

except Exception as e: 
    print(f'something wrong happened which is {e}')

else: 
    print('No errors found')


# ---------------------------------------------------
# try:
#     raise Exception("HI buddy")
# except: 
#     print("ايه انت هتصحابني ولا اي")

# -----------------------------------------------



