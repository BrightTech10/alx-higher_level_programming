#!/usr/bin/python3
""" This module multiplies two matrices """


def matrix_mul(m_a, m_b):
    """
    Multiplies tow matrices and returns the result

    Args:
        m_a: first matrix
        m_b: second matrix

    Returns:
        returns product of two matrices
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")

    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if isinstance(m_a, list):
        for value in m_a:
            if not isinstance(value, list):
                raise TypeError("m_a must be a list of lists")

    if isinstance(m_b, list):
        for value in m_b:
            if not isinstance(value, list):
                raise TypeError("m_b must be a list of lists")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")

    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if isinstance(m_a, list):
        for value in m_a:
            for subvalue in value:
                if not isinstance(subvalue, (int, float)):
                    raise TypeError("m_a should contain"
                                    " only integers or floats")

    if isinstance(m_b, list):
        for value in m_b:
            for subvalue in value:
                if not isinstance(subvalue, (int, float)):
                    raise TypeError("m_b should contain"
                                    " only integers or floats")

    if not all(len(value) == len(m_a[0]) for value in m_a):
        raise TypeError("each row of m_a must be of the same size")

    if not all(len(value) == len(m_b[0]) for value in m_b):
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    size_a = len(m_a)
    size_b = len(m_b)
    new_matrix = list()
    for row_a in range(size_a):
        flag = 0
        sub_list = list()
        for row_b in range(size_b):
            for col in range(len(m_b[row_a])):
                if flag == 0:
                    sub_list.append(m_a[row_a][row_b] * m_b[row_b][col])
                else:
                    sub_list[col] += (m_a[row_a][row_b] * m_b[row_b][col])
            flag = 1
        new_matrix.append(sub_list)
    return new_matrix
