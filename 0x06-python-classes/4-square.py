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

    @property
    def size(self):
        ''' Retrieves the private instance attribute size '''
        return self.__size

    @size.setter
    def size(self, value):
        ''' Sets the Size attribute '''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    # moved area to after setter so that it uses updated values

    def area(self):
        ''' Calculates the area of Object Square.
        Return:
            the current square area
        '''
        return (self.__size * self.__size)
