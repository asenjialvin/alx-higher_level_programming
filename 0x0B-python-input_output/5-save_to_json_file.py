#!/usr/bin/python3
''' Module for save_to_json_file '''
import json
''' module for json '''


def save_to_json_file(my_obj, filename):
    ''' write an obj to text file using json representation
        Args:
            my_obj(obj): object
            filename(file): name of the file
    '''
    with open(filename, "w", encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
