#!/usr/bin/python3
"""This module defines a Rectangle class with functional __repr__ for eval."""


class Rectangle:
    """Represents a geometric rectangle with recreation capability."""

    def __init__(self, width=0, height=0):
        """Initializes the rectangle with optional width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width with strict type and value validation."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height with strict type and value validation."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates and returns the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculates and returns the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Returns a printable string representation of the rectangle using #."""
        if self.__width == 0 or self.__height == 0:
            return ""

        rect_lines = []
        for _ in range(self.__height):
            rect_lines.append("#" * self.__width)
        return "\n".join(rect_lines)

    def __repr__(self):
        """Returns a string representation to recreate instance via eval().

        Returns:
            str: String format 'Rectangle(width, height)'
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)
