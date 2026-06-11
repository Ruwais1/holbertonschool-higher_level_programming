#!/usr/bin/python3
"""
0-add_integer module.

This module provides a simple function `add_integer`
that adds two integers or floats together.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats.
    Args:
        a: First number.
        b: Second number, defaults to 98.
    Returns:
        The addition of a and b casted to integers.
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
