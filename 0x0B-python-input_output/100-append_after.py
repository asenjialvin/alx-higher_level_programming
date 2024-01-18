#!/usr/bin/python3
''' module for append_after '''


def append_after(filename="", search_string="", new_string=""):
    ''' inserts a line of text after a specific string
        Args:
            filename(file): name of file
            search_string(str): string
            new_string(str): string
    '''
    content = ""
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            content += line
            if search_string in line:
                content += new_string
    with open(filename, "w") as f:
        f.write(content)
