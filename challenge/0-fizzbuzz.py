#!/usr/bin/python3
"""FizzBuzz module"""


def fizzbuzz():
    """Print numbers from 1 to 100 with FizzBuzz replacements"""
    for i in range(1, 101):
        if i % 15 == 0:
            print("FizzBuzz", end="")
        elif i % 3 == 0:
            print("Fizz", end="")
        elif i % 5 == 0:
            print("Buzz", end="")
        else:
            print(i, end="")

        if i != 100:
            print(" ", end="")
    print()
