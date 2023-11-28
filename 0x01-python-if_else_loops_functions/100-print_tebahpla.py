#!/usr/bin/python3
for ascii in range(122, 96, -1):
    if (ascii % 2) != 0:
        ascii = ascii - 32
    print(chr(ascii).format(), end="")
