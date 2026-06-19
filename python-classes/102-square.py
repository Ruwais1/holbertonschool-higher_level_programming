#!/usr/bin/python3
"""This module defines a Square class with area-based comparison operators."""


class Square:
    """Represents a geometric square with comparison capabilities."""

    def __init__(self, size=0):
        """Initializes the square with a given size."""
        self.size = size

    @property
    def size(self):
        """Retrieves the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size, validating that it's a number (int or float)."""
        if type(value) is not int and type(value) is not float:
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates the area of the square."""
        return self.__size ** 2

    def __eq__(self, other):
        """Checks if the areas are equal."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Checks if the areas are not equal."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Checks if this area is strictly less than the other area."""
        return self.area() < other.area()

    def __le__(self, other):
        """Checks if this area is less than or equal to the other area."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Checks if this area is strictly greater than the other area."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Checks if this area is greater than or equal to the other area."""
        return self.area() >= other.area()
