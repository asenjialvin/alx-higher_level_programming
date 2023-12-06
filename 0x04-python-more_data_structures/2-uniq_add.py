#!/usr/bin/python3
def uniq_add(my_list=[]):
    list_sum = sum(map(lambda i: i, set(my_list)))
    return list_sum
    """
    x = 0
    for i in set(my_list):
        x += i
    return x
    """
