#!/usr/bin/python3
''' Module for load_from_json function '''
import json
''' module for json '''


def load_from_json_file(filename):
    ''' creates an obj from a json file
        Args:
            filename(file); name of file
    '''
    with open(filename) as f:
        return json.load(f)
