#!/usr/bin/python3
''' Module for the Rectangle class '''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    ''' defines a rectangle by inheriting from BaseGeometry
        Args:
            BaseGeometry: parent class inherited from
    '''
    def __init__(self, width, height):
        ''' Initiates a rectangle instance '''
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        obj = type(self).__name__
        return ("[{}] {}/{}".format(obj, self.__width, self.__height))
