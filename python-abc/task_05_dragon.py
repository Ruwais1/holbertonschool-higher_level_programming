#!/usr/bin/env python3
"""
Module that defines SwimMixin, FlyMixin, and a Dragon class utilizing both.
"""


class SwimMixin:
    """Mixin that provides swimming functionality."""

    def swim(self):
        """Prints a swimming message."""
        print("The creature swims!")


class FlyMixin:
    """Mixin that provides flying functionality."""

    def fly(self):
        """Prints a flying message."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Class representing a dragon that can both swim and fly using Mixins."""

    def roar(self):
        """Prints a roaring message specific to the dragon."""
        print("The dragon roars!")
