#!/usr/bin/python3
''' Module for the is_kind_of_class function '''


def is_kind_of_class(obj, a_class):
    ''' checks if it is an instacne of the object or it's parent
        Args:
            obj: object
            a_class: class to check against
        Return: True, otherwise false
    '''
    if isinstance(obj, a_class):
        return (True)
    else:
        return (False)
