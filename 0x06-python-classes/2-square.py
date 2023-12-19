#!/usr/bin/python3
''' Module for the Square definition'''


class Square:
    ''' Defines a new square '''
    def __init__(self, size=0):
        ''' Constructor.
        Args:
            size: width and height of the Square
        '''
        if isinstance(size, int):
            self.__size = size
        else:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
