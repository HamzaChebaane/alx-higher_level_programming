#!/usr/bin/python3
for number in range(0, 10):
    for digit in range(number + 1, 10):
        if number < 8:
            print("{}{}, ".format(number, digit), end="")
        elif number == 8:
            print("{}{}".format(number, digit))
