#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for x in range(0, list_length):
        try:
            new_element = my_list_1[x]/my_list_2[x]
        except TypeError:
            print("wrong type")
            new_element = 0
        except ZeroDivisionError:
            print("division by 0")
            new_element = 0
        except IndexError:
            print("out of range")
            new_element = 0
        finally:
            new_list.append(new_element)
    return (new_list)
