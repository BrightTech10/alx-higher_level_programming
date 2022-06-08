#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    """Function that computes the square value of all integers of a matrix

    Args:
        matrix: a 2 dimensional array

    Return:
        returns a new list
    """
    new_list = []

    for element in matrix:
        new_list.append(list(map(lambda x: x ** 2, element)))
    return new_list
