#!/usr/bin/python3
for i in range(122, 96, -1):
    if i % 2 == 1:
        o = i - 32
    else:
        o = i
    print("{}".format(o), end=' ')
