def str():
    string="The quick Brow Fox"
    upper=0
    lower=0
    i=0
    while i<len(string):
        if string[i].islower():
            lower+=1
        elif string[i].isupper():
            upper+=1
        i+=1
    print(upper,"upper case")
    print(lower,"lower case")
str()
