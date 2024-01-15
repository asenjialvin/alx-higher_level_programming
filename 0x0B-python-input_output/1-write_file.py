#!/usr/bin/python3
''' Module for write_file function '''


def write_file(filename="", text=""):
    ''' writes a string to a text file.
        Args:
            filename(file): name of file
            text(str): string to be written
        Return: number of characters written
    '''
    with open(filename, "w", encoding="utf-8") as f:
        number_of_characters = f.write(text)
        return (number_of_characters)
