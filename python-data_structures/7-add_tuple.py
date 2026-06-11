#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """
    Adds two tuples and returns a tuple with the sum of the first two elements.

    Args:
        tuple_a (tuple): The first tuple.
        tuple_b (tuple): The second tuple.

    Returns:
        tuple: A tuple containing the sum of the first two elements of both.
    """
    a = tuple_a + (0, 0)
    b = tuple_b + (0, 0)
    return (a[0] + b[0], a[1] + b[1])
