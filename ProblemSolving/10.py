def another_one(digits):
    if digits[-1] == 9:
        # reset all items 
        digits[1:] = [0 for _ in range(len(digits[1:]))]
        # update the lst
        if digits[0] !=9: 
            digits[0] += 1
        else: 
            digits[0] = 1 
            digits.append(0)
        
    else:
        digits[-1] += 1

    return digits


if __name__ == "__main__":

    # testcases

    input1 = [1, 2, 3]
    print(another_one(input1))
    
    input2 = [6, 9]
    print(another_one(input2))

    input3 = [9, 9]
    print(another_one(input3))


