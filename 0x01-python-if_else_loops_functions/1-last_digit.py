#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
string = "Last digit of {} is {} and is {}"
if number >= 0:
    if number % 10 == 0:
        print(string.format(number, number % 10, "0"))
    elif number % 10 > 5:
        print(string.format(number, number % 10, "greater than 5"))
    elif number % 10 < 6:
        print(string.format(number, number % 10, "less than 6 and not 0"))
elif number < 0:
    if (0 - number) % 10 == 0:
        print(string.format(number, (0 - number) % 10, "0"))
    elif (0 - number) % 10 > 5:
        print(string.format(number, (0 - number) % 10, "greater than 5"))
    elif (0 - number) % 10 < 6:
        print(string.format(number, (0 - number) % 10, "less than 6 and not 0"))
