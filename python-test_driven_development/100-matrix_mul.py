#!/usr/bin/python3
"""
100-matrix_mul module.

This module provides a function `matrix_mul` that multiplies two matrices
after performing rigorous sequential validations.
"""


def matrix_mul(m_a, m_b):
    """
    Multiplies 2 matrices.

    Args:
        m_a (list of lists): The first matrix.
        m_b (list of lists): The second matrix.

    Returns:
        list of lists: The product of m_a and m_b.
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    for row in m_a:
        for x in row:
            if type(x) not in (int, float):
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        for x in row:
            if type(x) not in (int, float):
                raise TypeError("m_b should contain only integers or floats")

    len_a = len(m_a[0])
    if not all(len(row) == len_a for row in m_a):
        raise TypeError("each row of m_a must be of the same size")

    len_b = len(m_b[0])
    if not all(len(row) == len_b for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    if len_a != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = []
    for i in range(len(m_a)):
        row_res = []
        for j in range(len_b):
            val = sum(m_a[i][k] * m_b[k][j] for k in range(len(m_b)))
            row_res.append(val)
        result.append(row_res)

    return result
