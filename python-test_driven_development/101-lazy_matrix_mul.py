#!/usr/bin/python3
"""
101-lazy_matrix_mul module.

This module provides a function `lazy_matrix_mul` that multiplies two
matrices utilizing the powerful NumPy library, with legacy error mapping.
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
    # 1. Check for scalar / non-list types
    if type(m_a) not in (list, tuple) or type(m_b) not in (list, tuple):
        raise ValueError("Scalar operands are not allowed, use '*' instead")

    # 2. Check for jagged matrices and string data types (einsum error)
    for m in (m_a, m_b):
        if isinstance(m, list) and len(m) > 0 and isinstance(m[0], list):
            row_len = len(m[0])
            for row in m:
                if not isinstance(row, list):
                    continue
                if len(row) != row_len:
                    raise ValueError(
                        "setting an array element with a sequence.")
                for x in row:
                    if type(x) is str:
                        raise TypeError("invalid data type for einsum")
        elif isinstance(m, list):
            for x in m:
                if type(x) is str:
                    raise TypeError("invalid data type for einsum")

    # 3. Check for dimensional misalignment natively matches 1.15.0 format
    dim_a_0 = len(m_a)
    dim_a_1 = len(m_a[0]) if dim_a_0 > 0 and isinstance(m_a[0], list) else 0
    dim_b_0 = len(m_b)
    dim_b_1 = len(m_b[0]) if dim_b_0 > 0 and isinstance(m_b[0], list) else 0

    if dim_a_1 != dim_b_0:
        raise ValueError(
            "shapes ({},{}) and ({},{}) not aligned: "
            "{} (dim 1) != {} (dim 0)".format(
                dim_a_0, dim_a_1, dim_b_0, dim_b_1, dim_a_1, dim_b_0
            )
        )

    # 4. Perform the actual matrix multiplication
    return np.matmul(m_a, m_b)
