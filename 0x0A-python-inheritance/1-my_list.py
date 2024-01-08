#!/usr/bin/python3
''' Module that defines the MyList class '''


class MyList(list):
    ''' Defines a list object
        Args:
            list: inherited from list
    '''

    def print_sorted(self):
        ''' Prints the list in ascending order
            all args are of type int
        '''
        if not isinstance(self, list):
            raise TypeError("Has to be a list")
        for i in range(len(self)):
            if not isinstance(self[i], int):
                raise TypeError("has to be an int")
        sorted_list = sorted(self)
        print(sorted_list)
