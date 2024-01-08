#!/usr/bin/python3
''' Module for the Square class '''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    ''' Defines an instance of a square '''

    def __init__(self, size):
        ''' Initialises a square
            Args:
                size: size of square
        '''
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        return self.__size * self.__size
