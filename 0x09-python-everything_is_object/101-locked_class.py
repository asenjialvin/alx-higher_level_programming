#!/usr/bin/python3
'''Defines a class that it locked'''


class LockedClass:
    ''' Prevents user fomr dynamically creating new attr.
        unless that new attr is "first_name"
    '''
    __slots__ = ["first_name"]
    ''' only allowed attribute '''
