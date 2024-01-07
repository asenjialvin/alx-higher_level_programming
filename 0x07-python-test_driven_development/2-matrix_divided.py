#!/usr/bin/python3
''' Module for matrix_divided
    a function that divides all elements of a matrix.
    raises error if inputs are not of type int/float
'''


def matrix_divided(matrix, div):
    ''' Args:
            matrix: lists of lists that have int/floats
            div: the divisor int/float
        Return: a new matrix with divided values
    '''
    new_mx = []
    err1 = "matrix_divided() missing 1 required positional argument: 'matrix'"
    err2 = "matrix must be a matrix (list of lists) of integers/floats"
    if len(matrix) == 0:
        raise TypeError(err1)
    if any(len(row) == 0 for row in matrix):
        raise TypeError(err2)
    if matrix is None or not isinstance(matrix, list):
        raise TypeError(err2)
    if div is None:
        raise TypeError("div must be a number")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for row in range(len(matrix)):
        if not isinstance(matrix[row], list):
            raise TypeError(err2)
        if len(matrix[row]) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        new_list = []
        for element in range(len(matrix[row])):
            if not isinstance(matrix[row][element], int):
                if not isinstance(matrix[row][element], float):
                    raise TypeError(err2)
            new_element = round(matrix[row][element] / div, 2)
            new_list.append(new_element)
        new_mx.append(new_list)
    return new_mx
