#!/usr/bin/python3
''' This is the module for the Rectangle class '''


class Rectangle:
    ''' This is represents a rectangle
        Attributes (class):
            number_of_instances (int): self explanatory
            print_symbol (any): Used as symbol for string representation
    '''

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        '''Initialises the width and height
            Args:
                width (int): width of the rectangle
                height (int): height of the rectangle
            Return: new rectangle
        '''
        self.height = height
        self.width = width
        type(self).number_of_instances += 1

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
                rectangle.append(str(self.print_symbol))
            if row != self.__height - 1:
                rectangle.append("\n")
        return ("".join(rectangle))

    def __repr__(self):
        ''' Returns canonical string representation of the object.
            Creates rectangles using #
        '''
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        '''Prints Bye Rectangle when deleted '''
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        ''' Finds bigger rectangle
            Args:
                rect_1 (Rectangle): first rectangle
                rect_2 (Rectangle): second rectangle
            Return: Larges rect/ rect_1
        '''
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() < rect_2.area():
            return rect_2
        else:
            return rect_1
