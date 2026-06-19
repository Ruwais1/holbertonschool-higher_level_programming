#!/usr/bin/python3
"""This module defines the Square class with a string representation."""


class Square:
    """A class used to represent a geometric square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes the Square instance.

        Args:
            size (int): The width and height length of the square.
            position (tuple): The x and y coordinates of the square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieves the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieves the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position of the square."""
        if (not isinstance(value, tuple) or len(value) != 2 or
                type(value[0]) is not int or type(value[1]) is not int or
                value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculates and returns the current square area."""
        return self.__size * self.__size

    def my_print(self):
        """Prints the square with the character # to stdout."""
        print(self)

    def __str__(self):
        """Returns the string representation of the square."""
        if self.__size == 0:
            return ""

        result = []
        for _ in range(self.__position[1]):
            result.append("")
        for _ in range(self.__size):
            result.append(" " * self.__position[0] + "#" * self.__size)
        
        return "\n".join(result)
