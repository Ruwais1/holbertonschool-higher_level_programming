#!/usr/bin/env python3
"""
Module that defines the CountedIterator class to keep track of iterations.
"""


class CountedIterator:
    """An iterator that counts the number of items successfully fetched."""

    def __init__(self, iterable):
        """Initializes the iterator object and the counter."""
        self.__iterator = iter(iterable)
        self.__count = 0

    def get_count(self):
        """Returns the current number of items that have been iterated."""
        return self.__count

    def __next__(self):
        """Fetches the next item and increments the counter."""
        try:
            item = next(self.__iterator)
            self.__count += 1
            return item
        except StopIteration:
            raise StopIteration

    def __iter__(self):
        """Returns the iterator object itself."""
        return self
