#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    temp = a_dictionary.copy()
    for x, y in temp.items():
        if value == y:
            a_dictionary.pop(x)
    return a_dictionary
