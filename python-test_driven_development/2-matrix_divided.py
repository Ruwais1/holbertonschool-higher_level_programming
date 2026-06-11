#!/usr/bin/python3
"""
2-matrix_divided module.

This module provides a function `matrix_divided` that divides all elements
of a matrix (list of lists) by a given number (integer or float).
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div.

    Args:
        matrix (list of lists): Matrix containing integers or floats.
        div (int/float): The divisor number.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats.
        TypeError: If rows of the matrix are not of the same size.
        TypeError: If div is not an integer or float.
        ZeroDivisionError: If div is equal to 0.

    Returns:
        list of lists: A new matrix containing the results rounded to 2.
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(msg)

    row_len = None
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(msg)
        if row_len is None:
            row_len = len(row)
        elif len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")
        for num in row:
            if type(num) not in (int, float):
                raise TypeError(msg)

    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(num / div, 2) for num in row] for row in matrix]
