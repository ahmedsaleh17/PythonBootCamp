# using recursion
def factorial(n):
    if n == 1 or n == 0:
        return 1

    return n * factorial(n - 1)


#
def factorial2(n):

    result = 1

    for i in range(n, 0, -1):

        result *= i
    return result 


print(factorial(9)) # faster 

print(factorial2(9))