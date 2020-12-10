import re

def word_count(s):
    # Your code here

    # char_list = ('":;.-+=/\|[]{}()*^&')
    #place to hold values
    d = dict()
    
    # ingnore chars
    char_list = '"":;.,-+=/\|[]{}()*^&'

    new_s = s.lower().replace("\r", " ").replace(
        "\t", " ").replace("\n", " ").split(" ")

    print(new_s)
    
    #loop though and strip the char list
    for word in new_s:
        new_word = word.strip(char_list)
        # print new word
        print(new_word)
        
        #check to see if in d and it's blank 
        if new_word not in d and new_word != "":
            # set to 1 else increase
            d[new_word] = 1
        elif new_word != "":
            d[new_word] += 1
    return d



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))