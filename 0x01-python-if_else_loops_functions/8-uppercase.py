#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        if ord("a") <= ord(letter) <= ord("z"):
            letter = chr(ord(letter) - 32)
        print("{:s}".format(letter), end="")
    print()
