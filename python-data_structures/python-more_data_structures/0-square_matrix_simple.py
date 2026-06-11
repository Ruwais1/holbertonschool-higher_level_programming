#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """
    Computes the square value of all integers of a matrix.

    Args:
        matrix (list): A 2D array of integers.

    Returns:
        list: A new 2D array with each value squared.
    """
    return [[num ** 2 for num in row] for row in matrix]
