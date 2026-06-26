#!/usr/bin/env python3
"""
Module that defines shapes using Abstract Base Classes and demonstrates duck typing.
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class representing a generic shape."""

    @abstractmethod
    def area(self):
        """Calculates and returns the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculates and returns the perimeter of the shape."""
        pass


class Circle(Shape):
    """Class representing a circle."""

    def __init__(self, radius):
        """Initializes a Circle with a radius."""
        self.radius = radius

    def area(self):
        """Calculates the area of the circle."""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Calculates the perimeter of the circle."""
        return 2 * math.pi * abs(self.radius)


class Rectangle(Shape):
    """Class representing a rectangle."""

    def __init__(self, width, height):
        """Initializes a Rectangle with width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Calculates the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Calculates the perimeter of the rectangle."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Prints the area and perimeter of a shape relying on duck typing.
    Does not explicitly check the object's type.
    """
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
