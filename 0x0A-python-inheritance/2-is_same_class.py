#!/usr/bin/python3
''' Module for the is_same_calss function '''


def is_same_class(obj, a_class):
    ''' defines an instance that is exactly of the specified class as true,
        otherwise it is defined as false

        Args:
            obj: object specified
            a_class: class used to compare obj with
        Return: True if isinstance, false otherwise
    '''
    if type(obj) == a_class:
        return True
    else:
        return False
