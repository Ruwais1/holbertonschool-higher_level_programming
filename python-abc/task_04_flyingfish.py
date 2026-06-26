#!/usr/bin/env python3
"""
Module that defines Fish, Bird, and the multiple-inherited FlyingFish class.
"""


class Fish:
    """Class representing a fish."""

    def swim(self):
        """Prints swimming message."""
        print("The fish is swimming")

    def habitat(self):
        """Prints fish habitat message."""
        print("The fish lives in water")


class Bird:
    """Class representing a bird."""

    def fly(self):
        """Prints flying message."""
        print("The bird is flying")

    def habitat(self):
        """Prints bird habitat message."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Class representing a flying fish, inheriting from both Fish and Bird."""

    def swim(self):
        """Prints specific flying fish swimming message."""
        print("The flying fish is swimming!")

    def fly(self):
        """Prints specific flying fish flying message."""
        print("The flying fish is soaring!")

    def habitat(self):
        """Prints specific flying fish habitat message."""
        print("The flying fish lives both in water and the sky!")
