#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        result = fct(*args)
    except (IndexError, NameError, TypeError, ZeroDivisionError) as e:
        print("Exception: {}".format(str(e)), file=sys.stderr)
        result = "None"
    return result
