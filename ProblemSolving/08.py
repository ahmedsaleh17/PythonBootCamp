"""
Solution
Tracking diagonal elements

What if we could figure out which elements in a matrix are on the same diagonal stripe? This would make the problem easier. If we can group the elements on the same diagonal together, we could just check if all elements in each diagonal are equal.

But how do we determine if elements are on the same diagonal stripe? Let's use this example:
1	2	3
4	5	6
7	8	9
10	11	12

The elements 1, 5, 9 are on the same diagonal. Their positions are (0,0), (1,1), (2,2).
The difference between their row and column (i - j) is the same for all of them: 0.
Similarly, the elements 4, 8, 12 are also on the same diagonal.
Their positions are (1,0), (2,1), (3,2), and their i - j difference is also the same: 1.

Implementation:

We can use a dictionary to track diagonal elements efficiently. The key of the dictionary will be the difference i - j, and the value will be the first element we encounter for that diagonal. Then, we'll compare subsequent elements on that diagonal to the stored value. If any mismatch is found, we return False immediately. If we finish traversing the matrix without finding a mismatch, we return True.

Here's how the approach works:

    If i - j is not in the dictionary, we store the current element in the dictionary as the first element of this diagonal.
    If i - j is already in the dictionary, we compare the stored element with the current one. If they are different, we return False immediately.
    After the entire matrix is traversed, return True if no mismatches were found.

Same diagonal has the same (row_idx - col_idx) 
Here is the full code:"""


def is_same_stripes(matrix):

    stripe_check = {}

    # loop for each row
    for i in range(len(matrix)):
        # loop for each column
        for j in range(len(matrix[i])):
            # check if the key is exist first and compare it's value with the current value
            key = i - j

            if key not in stripe_check.keys():
                # insert the key and it's value 
                stripe_check[key] = matrix[i][j]
            else: 
                # if the key is exist 
                # check if it's value equal to the current value  
                # if not return false otherwise continue 
                if matrix[i][j] != stripe_check[key]:
                    # so now this matrix is not same stripes 
                    return False
    return True 


if __name__ == "__main__":

    # test cases 
    matrix = [[42, 7, 13, 99], [6, 42, 7, 13], [1, 6, 42, 7]]
    print(is_same_stripes(matrix)) # True 

    matrix2 = [[8, 42],[1, 8]]

    print(is_same_stripes(matrix2)) # True 
    
    matrix3 = [[8, 42],[1, 10]]

    print(is_same_stripes(matrix3)) # False
 
