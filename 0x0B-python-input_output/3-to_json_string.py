#!/usr/bin/python3
''' Module for the json_string function '''
import json
''' Json module '''


def to_json_string(my_obj):
    ''' returns a JSON representation of obj
        Args:
        my_obj(str): object
    '''
    return (json.dumps(my_obj, sort_keys=True))
