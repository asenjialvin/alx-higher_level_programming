#!/usr/bin/python3
''' Module for the append_write function '''


def append_write(filename="", text=""):
    ''' appends a string to a file
        Args:
            filename(file): name of the file
            text(str): text to append
        Return: number of characters added
    '''
    with open(filename, "a", encoding="utf-8") as f:
        return (f.write(text))
