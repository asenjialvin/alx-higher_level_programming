#!/usr/bin/python3
''' Module for MyInt class  '''


class MyInt(int):
    ''' inherits from int
        Args:
        int(int): class
    '''
    def __bool__(int):
        ''' override the bool subclass of int'''
        return False

    def __eq__(self, value):
        ''' overrisde == with !='''
        return self.real != value

    def __ne__(self, value):
        ''' override != with == '''
        return self.real == value
