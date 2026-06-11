#!/usr/bin/python3
"""
101-lazy_matrix_mul module.

This module provides a function `lazy_matrix_mul` that multiplies two
matrices utilizing the powerful NumPy library.
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies 2 matrices using NumPy.

    Args:
        m_a (list of lists): The first matrix.
        m_b (list of lists): The second matrix.

    Returns:
        ndarray: The product of m_a and m_b.
    """
    return np.matmul(m_a, m_b)
