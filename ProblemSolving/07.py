def convertToBase13(num):
    postivie_number = True 

    result = ""
    base = "0123456789ABC"
    if num < 13 and num >0 : 
      return base[num]
    
    elif num == 0:
      return 0
    
    elif num < 0 : 
        # validate number 
        num = -num 
        postivie_number = False
        
    
    while num !=0:
        
        # calculate the remainder 
        remainder = num % 13

        # calulate the quotient
        quotient = num // 13 

        result += base[remainder]

        # update the quotient 
        num = quotient

    if not postivie_number: 
       result+= "-"

    return result[::-1]

def convertToBase13v2(num):
    if num == 0:
        return "0"
    
    base13_digits = "0123456789ABC"
    digits_arr = []
    positive = abs(num)
    
    while positive > 0:
        # Append to list
        digits_arr.append(base13_digits[positive % 13])  
        positive = positive // 13
    
    reversed_digits = digits_arr[::-1]
    # Join list into a string
    result = ''.join(reversed_digits)  
    
    if num < 0:
        return "-" + result
    else:
        return result
    
if __name__ == "__main__":
    print(convertToBase13(10)) # A
    print(convertToBase13(11)) # B
    print(convertToBase13(12)) # C
    print(convertToBase13(14)) # 11
    print(convertToBase13(49)) # 3A
    print(convertToBase13(69)) # 54
    print(convertToBase13(-1845))

