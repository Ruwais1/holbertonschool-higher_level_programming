#!/usr/bin/python3
"""
This module defines the Square class with a private size attribute,
getter/setter properties, an area method, and a method to print the square.
"""


class Square:
    """
    A class used to represent a geometric square with properties
    and a printing method.
    """

    def __init__(self, size=0):
        """
        Initializes the Square instance.

        Args:
            size (int): The width and height length of the square.
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
            int: The current size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square with strict validation.

        Args:
            value (int): The new size of the square.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates and returns the current square area.

        Returns:
            int: The area of the square (size squared).
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Prints the square with the character # to stdout.
        If size is 0, prints an empty line.
        """
        if self.__size == 0:
            print("")
            return

        for _ in range(self.__size):
            print("#" * self.__size)
