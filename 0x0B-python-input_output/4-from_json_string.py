#!/usr/bin/python3
''' Module for from_json_string '''
import json
''' json module '''


def from_json_string(my_str):
    ''' return an obj represented by json string
        Args:
            my_str(str): json string
    '''
    return (json.loads(my_str))
