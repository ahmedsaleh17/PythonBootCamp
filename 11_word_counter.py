from collections import Counter


def words_counter(text):
    # counter of words 
    words_cnt = {}
    # first we need to split the text to loop over words    
    # list of words
    words_lst = map(str.lower, text.split())

    for word in words_lst:
        words_cnt[word] = words_cnt.get(word,0)+1

    return dict(sorted(words_cnt.items(), key= lambda x: x[1], reverse= True))
     


# define the fuction using standard module (collections)

def words_counterv2(text):
    words_cnt = Counter(text.split())
    return words_cnt


def words_counterv3(text): 
    # counter of words 
    words_cnt = {}

    # list of words 
    words_list  = map(str.lower, text.split())
    # print(type(words_list))  # <class 'map'> iterator 
    for word in words_list: 
        if word in words_cnt:
            words_cnt[word] +=1
        else: 
            words_cnt[word] = 1 
    
    return dict(sorted(words_cnt.items(), key= lambda x: x[1], reverse= True))

if __name__ == "__main__":
    text  = ('this is sample text with several words '
             'this is a sample text wtih some different words '
             'that is also another text with other different words')
    


    count_of_words = words_counter(text= text)
    count_of_words2 = words_counterv2(text= text)
    count_of_words3 = words_counterv3(text= text)

    print(count_of_words)
    print('--'*20)
    print(count_of_words2)
    print('--'*20)
    print(count_of_words3)
    
    
    
    
    # # print(count_of_words) 
    # for key, value in sorted(count_of_words.items(), key = lambda x: x[1]):
    #     print(f"`{key}` is repeated {value} times.")

    

    # how to get unique words 
    # words is repeated 1 times 
    # unique_words = []
    # for key, value in count_of_words.items():
    #     if value == 1: 
    #         unique_words.append(key)

    # print(unique_words)    
    
