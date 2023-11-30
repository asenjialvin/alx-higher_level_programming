#!/usr/bin/python3
import sys

if __name__ == "__main__":
    sum_of_arg = 0
    for arguments in sys.argv[1:]:
        sum_of_arg += int(arguments)
    print(sum_of_arg)
