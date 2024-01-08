#!/usr/bin/python3
''' Module for the BaseGeometry class '''


class BaseGeometry:
    ''' defines base geometry '''

    def area(self):
        ''' calculates the area of a shape '''
        raise Exception("area() is not implemented")
