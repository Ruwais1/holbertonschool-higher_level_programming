#!/usr/bin/python3
"""This module defines a class MyInt that inherits from int."""


class MyInt(int):
    """A rebel class that inherits from int and inverts == and !="""

    def __eq__(self, other):
        """Inverts the behavior of the == operator."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Inverts the behavior of the != operator."""
        return super().__eq__(other)
