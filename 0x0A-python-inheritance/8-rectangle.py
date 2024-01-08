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
