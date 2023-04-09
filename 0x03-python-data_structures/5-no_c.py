#!/usr/bin/python3
def no_c(my_string):
    new_string = list(my_string)
    i = 0
    for index in new_string:
        if index == 'c' or index == 'C':
            del new_string[i]
        i += 1
    return "".join(new_string)
