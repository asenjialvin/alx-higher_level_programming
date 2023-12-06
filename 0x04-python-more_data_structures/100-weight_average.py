#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    score = 0
    weight = 0
    for group in my_list:
        score += group[0] * group[1]
        weight += group[1]
    final = score / weight

    return final
