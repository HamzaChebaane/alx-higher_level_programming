#!/usr/bin/python3
def uppercase(str):
    for i in str:
        c = ord(i) - 32
        if ord(i) > 90 or ord(i) < 65 and ord != 32:
            print("{}".format(chr(c)), end='')
        else:
            print("{}".format(i), end='')
