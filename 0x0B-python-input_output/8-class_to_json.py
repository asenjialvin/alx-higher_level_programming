#!/usr/bin/python3
''' Module for class_to_json '''


def class_to_json(obj):
    ''' returns the dictionary description with
        simple data structure
        Args:
            obj: an instance of a Class
        Return: sictionary with simple data structure
    '''
    return obj.__dict__
