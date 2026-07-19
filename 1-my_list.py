#!/usr/bin/python3
"""This module defines a custom list class MyList."""


class MyList(list):
    """A custom list class that inherits from the built-in list."""

    def print_sorted(self):
        """Prints the elements of the list in ascending sorted order."""
        print(sorted(self))
