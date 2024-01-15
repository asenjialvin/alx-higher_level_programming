#!/usr/bin/python3
''' Mdule for the read_file function '''


def read_file(filename=""):
    ''' Reads a text file with encoding UTF8 to stdout
        Args:
            filename(file): name of the file
    '''
    with open(filename, encoding="utf-8") as f:
        read_file = f.read()
        print("{}".format(read_file), end="")
