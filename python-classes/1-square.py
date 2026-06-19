#!/usr/bin/python3
"""
1-square module.

This module provides a class Square that defines a square with a
private instance attribute size.
"""


class Square:
    """
    A class that defines a square by its size.
    """

    def __init__(self, size):
        """
        Initializes a new Square instance.

        Args:
            size: The size of the new square.
        """
        self.__size = size
