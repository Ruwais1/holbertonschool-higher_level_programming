#!/usr/bin/env python3
"""
Module that defines VerboseList, a custom list that prints notifications
when items are modified.
"""


class VerboseList(list):
    """A custom list that prints messages when elements are added or removed."""

    def append(self, item):
        """Adds an item to the list and prints a notification."""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, iterable):
        """Extends the list with an iterable and prints a notification."""
        initial_length = len(self)
        super().extend(iterable)
        added_items = len(self) - initial_length
        print("Extended the list with [{}] items.".format(added_items))

    def remove(self, item):
        """Removes an item from the list and prints a notification."""
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Pops an item from the list at a given index and prints a notification."""
        item = self[index]
        print("Popped [{}] from the list.".format(item))
        return super().pop(index)
