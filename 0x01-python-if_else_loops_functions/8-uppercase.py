#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) > 90 or ord(i) < 65 and ord != 32:
            c = ord(i) - 32
        else:
            c = ord(i)
        print("{}".format(chr(c)), end='')
    print()
