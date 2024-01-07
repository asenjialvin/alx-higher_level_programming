#!/usr/bin/python3
''' add_integer() add two intergers
    Handles cases of type() == int
    with execption TypeError
    otherwise it return the sum
'''


def add_integer(a, b=98):
    ''' Args:
            a: first integer
            b: second integer (initialised to 98)
        Return: Sum of the integers'''
    if a is None:
        raise TypeError("a must be an integer")
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)
    return a + b
