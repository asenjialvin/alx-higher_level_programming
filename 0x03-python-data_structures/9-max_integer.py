#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return (None)
    maximum_num = my_list[0]
    for i in range(len(my_list)):
        if my_list[i] > maximum_num:
            maximum_num = my_list[i]
    return (maximum_num)
