#!/usr/bin/python3
"""
Module that defines the class Student with filtered JSON retrieval.
"""


class Student:
    """Class that defines a student."""

    def __init__(self, first_name, last_name, age):
        """Initializes a new Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.
        If attrs is a list of strings, only specific attributes are retrieved.
        """
        if type(attrs) is list and all(type(i) is str for i in attrs):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__
