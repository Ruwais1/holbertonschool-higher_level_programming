#!/usr/bin/python3
"""
This module defines the Square class with a private size attribute
and explicit input validation for type and value constraints.
"""


class Square:
    """
    A class used to represent a geometric square with a validated size.
    """

    def __init__(self, size=0):
        """
        Initializes the Square instance with a private size attribute.

        Args:
            size (int): The width and height length of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
