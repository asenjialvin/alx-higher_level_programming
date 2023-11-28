#!/usr/bin/python3
def remove_char_at(str, n):
    copy_of_str = str
    if n >= len(str) or n < 0:
        return (str)
    copy_of_str = str[:n] + str[n+1:]
    return (copy_of_str)
