#!/usr/bin/python3
''' Module for the function inherits_from '''


def inherits_from(obj, a_class):
    ''' check if obj is directly/indirectly an instance of class
        Args:
            obj: object
            a_class: class in question
        Return: True , otherwise false
    '''
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
