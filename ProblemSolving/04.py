def is_kiss(sentence):
    complex  = False  

    words  = sentence.split()
    
    words_amount = len(words)

    for word in words: 
        if len(word) > words_amount:
            complex = True 
    
    if complex: 
        return "Keep It Simple Stupid"
    else: 
        return "Good work Joe!"




if __name__ == "__main__":

    # test 

    sentence = "jump always mostly is touchy dancing choice is pineapples mostly"

    print(is_kiss(sentence))