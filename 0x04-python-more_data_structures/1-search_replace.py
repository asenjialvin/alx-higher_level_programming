#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return list(map(lambda x: replace if x == search else x, my_list))

    # derived from the code

    """
    new_list = []
    for i in my_list:
        if i == search:
            new_list.append(replace)
        else:
            new_list.append(i)
    return(new_list)
    """
