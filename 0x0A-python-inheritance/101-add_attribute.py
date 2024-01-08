#!/usr/bin/python3
''' Module for can I? '''


def add_attribute(obj, attr_name, attr_value):
    ''' adds a new attribute if possible
        Args:
            obj: object
            attr_name: name of attribute
            attr_value: name of value
    '''
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, attr_name, attr_value)
