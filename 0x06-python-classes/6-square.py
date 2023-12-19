#!/usr/bin/python3
''' Module for the Square definition'''


class Square:
    ''' Defines a new square '''
    def __init__(self, size=0, position=(0, 0)):
        ''' Constructor.
        Args:
            size(int): width and height of the Square
            position(int, int): position of the square created
        '''
        self.__size = size
        if isinstance(position, tuple):
            self.__position = position
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    @property
    def size(self):
        ''' Retrieves the private instance attribute size '''
        return self.__size

    @size.setter
    def size(self, value):
        ''' Sets the Size attribute.
        Args:
            value:size of new value of the square
        '''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        ''' Retrieves the position of the square '''
        return self.__position

    @position.setter
    def position(self, value):
        ''' Sets the Positin attribute.
        Args:
            value: new value as a tuple with 2 elements
        '''
        lg = len(value)
        if (not isinstance(value, tuple) or
                lg != 2 or
                not all(isinstance(nm, int) for nm in value)
                or not all(nm >= 0 for nm in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    # moved area to after setter so that it uses updated values

    def area(self):
        ''' Calculates the area of Object Square.
        Return:
            the current square area
        '''
        return (self.__size * self.__size)

    def my_print(self):
        ''' Prints in Stdout the square with the character # '''
        if self.__size == 0:
            print()
            return
        for n in range(0, self.__position[1]):
            print(" ")
        for i in range(0, self.__size):
            for k in range(0, self.__position[0]):
                print(" ", end="")
            for j in range(0, self.__size):
                print("#", end="")
            print("")
