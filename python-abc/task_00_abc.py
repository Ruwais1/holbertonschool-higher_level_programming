#!/usr/bin/env python3
"""
Module that defines an abstract Animal class and its subclasses.
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class representing an animal."""

    @abstractmethod
    def sound(self):
        """Abstract method to define the sound of the animal."""
        pass


class Dog(Animal):
    """Class representing a dog."""

    def sound(self):
        """Returns the sound of a dog."""
        return "Bark"


class Cat(Animal):
    """Class representing a cat."""

    def sound(self):
        """Returns the sound of a cat."""
        return "Meow"
