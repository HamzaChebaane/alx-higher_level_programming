#!/usr/bin/python3
def no_c(my_string):
    new_string = list(my_string)
    for s in new_string:
        if new_string.count('c') > 0:
            i = new_string.index('c')
            del new_string[i]
    for s in new_string:        
        if new_string.count('C') > 0:
            i = new_string.index('C')
            del new_string[i]
    return "".join(new_string)
