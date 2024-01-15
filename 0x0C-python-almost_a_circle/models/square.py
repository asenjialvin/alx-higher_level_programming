#!/usr/bin/python3
''' Defines a Square '''
from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    ''' Defines a square instance br inheriting from
        the Rectangle class
        Args:
            Rectangle: class it inherits from
    '''
    def __init__(self, size, x=0, y=0, id=None):
        ''' Initialises a square instance
            Args:
                size(int): the length of the edges
                x: x co-ordinates of the square
                y: y co-ordinates of the square
                id: the unque number given to the instance
        '''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''prints a string representation of the square '''
        return "[{}] ({}) {}/{} - {}".format(Square.__name__, self.id,
                                             self.x, self.y, self.height)

    @property
    def size(self):
        ''' gets the width of the square '''
        return self.width

    @size.setter
    def size(self, value):
        ''' sets the size of the square '''
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        ''' assigns an argument to each variable
            Args:
                *args(int): variable number of arguments
                **kwargs(dict): key/ value arguments
        '''
        if args and len(args) != 0:
            count = 0
            for arg in args:
                if count == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif count == 1:
                    self.size = arg
                elif count == 2:
                    self.x = arg
                elif count == 3:
                    self.y = arg
                count += 1
        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        ''' Return the dictionary representation of a sqaure '''
        dictionary = {'id': self.id, 'size': self.width,
                      'x': self.x, 'y': self.y}
        sorted_dictionary = dict(sorted(dictionary.items()))
        return sorted_dictionary
