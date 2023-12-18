#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    element_counter = 0
    try:
        for i in range(x):
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                element_counter += 1
    except (IndexError, ValueError, TypeError):
        raise
    print()
    return element_counter
