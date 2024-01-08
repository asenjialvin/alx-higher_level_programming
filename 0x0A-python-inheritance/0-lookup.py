#!/usr/bin/python3
''' Module for the lookup function '''


def lookup(obj):
    ''' Function lists all available attributes and methods of an obj
        Args:
            obj(obj): object
        Return: list
    '''
    return dir(obj)
