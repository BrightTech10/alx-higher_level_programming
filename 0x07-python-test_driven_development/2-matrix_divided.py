#!/usr/bin/python3
""" This module divides a matrix by a given divisor """


def matrix_divided(matrix, div):
    """
    Divides each element in a matrix by div

    Args:
        matrix: a matrix (list of lists)
        div: divisor

    Raises:
        raises TypeError if matrix is not a list of lists
        raises TypeError if each row of matrix is not of the same size
        raises TypeError if div is not an int or float
        raises ZeroDivisionError if div is 0

    Return:
        returns new matrix
    """
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix" +
                        " (list of lists) of integers/floats")
    elif isinstance(matrix, list):
        for value in matrix:
            for subvalue in value:
                if not isinstance(subvalue, (int, float)):
                    raise TypeError("matrix must be a matrix"
                                    " (list of lists) of integers/floats")

    if not all(len(value) == len(matrix[0]) for value in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    else:
        new = [[round((subvalue / div), 2)
                for subvalue in value] for value in matrix]
    return new
