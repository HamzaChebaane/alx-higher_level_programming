#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if i % 15 == 0:
            c = "FizzBuzz"
        elif i % 5 == 0:
            c = "Buzz"
        elif i % 3 == 0:
            c = "Fizz"
        else:
            c = i
        print("{}".format(c), end=' ')
