#!/usr/bin/python3
''' This is the module for the Rectangle class '''


class Rectangle:
    ''' This is an empty class that does nothing for now'''
    def __init__(self, width=0, height=0):
        '''Initialises the width and height
            Args:
                width: width of the rectangle
                height: height of the rectangle
            Return: new rectangle
        '''
        self.height = height
        self.width = width

    @property
    def height(self):
        ''' This gets the height private instance'''
        return self.__height

    @height.setter
    def height(self, value):
        ''' This setes the height to the new vlaue with some exceptions'''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        ''' This gets the width private instance'''
        return self.__width

    @width.setter
    def width(self, value):
        ''' This sets the width to the new value with some exceptions'''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        ''' Calculates the area of a rectangle (width*height)'''
        return (self.__width * self.__height)

    def perimeter(self):
        ''' Calculates the perimeter of the rectangle '''
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__height * 2) + (self.__width * 2))

    def __str__(self):
        ''' Returns new string object from the given object.
            Creates reactangles using #
        '''
        if self.__width == 0 or self.__height == 0:
            return ("")

        rectangle = []
        for row in range(self.__height):
            for column in range(self.__width):
                rectangle.append("#")
            if row != self.__height - 1:
                rectangle.append("\n")
        return ("".join(rectangle))
