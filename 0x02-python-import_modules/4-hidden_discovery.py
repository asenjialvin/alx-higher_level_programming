#!/usr/bin/python3
import hidden_4
import re

if __name__ == "__main__":
    count = 0
    for count in range(len(dir(hidden_4))):
        if not (dir(hidden_4)[count]).startswith("__"):
            print(dir(hidden_4)[count])
