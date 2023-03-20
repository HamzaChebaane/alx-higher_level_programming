#!/usr/bin/python3
def remove_char_at(str, n):
    cr = ''
    for i in range(len(str)):
        if i != n:
            cr += str[i]
