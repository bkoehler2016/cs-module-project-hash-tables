def no_dups(s):
    # Your code here
    d = dict()
    
    # loop over and split and if not just set it to word
    for word in s.split():
        if word not in d:
            d[word] = word
    
    # return join word and values
    return " ".join((word for word in d.values()))



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))