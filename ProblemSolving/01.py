"""
"String" => "StRiNg"
"Weird string case" => "WeIrD StRiNg CaSe"
"""


def to_weird_case(words):
    idx = 0 
    result = ''

    # loop over letters in each word
    for letter in words: 
        # if there is a space not letter 
        if letter == ' ':
            # reset index to begin from the first idx in each word 
            idx = 0 
            # adding space to the result 
            result += letter
            continue 

        if idx % 2 ==0 :
            result += letter.upper()
        else: 
            result += letter.lower()
    
        # increase index 
        idx +=1

    # return the output 
    return result


if __name__ == '__main__':

    case1  = "String"
    case2 = "Weird string case"

    assert to_weird_case(case1) == "StRiNg"
    assert to_weird_case(case2) == "WeIrD StRiNg CaSe"