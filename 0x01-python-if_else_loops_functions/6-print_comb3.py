#!/usr/bin/python3
for numbers in range(9):
    for digits in range(numbers + 1, 10):
        if numbers * 10 + digits < 89:
            print("{:d}{:d}".format(numbers, digits), end=", ")
print("{:d}".format(89))
