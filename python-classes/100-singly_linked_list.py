#!/usr/bin/python3
"""This module defines Node and SinglyLinkedList classes."""


class Node:
    """A class that defines a node of a singly linked list."""

    def __init__(self, data, next_node=None):
        """Initializes the Node instance.

        Args:
            data (int): The data of the node.
            next_node (Node, optional): The next node. Defaults to None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieves the data of the node."""
        return self.__data

    @data.setter
    def data(self, value):
        """Sets the data of the node with type validation."""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieves the next node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Sets the next node with type validation."""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """A class that defines a singly linked list."""

    def __init__(self):
        """Initializes an empty SinglyLinkedList instance."""
        self.__head = None

    def __str__(self):
        """Returns the string representation of the linked list."""
        result = []
        current = self.__head
        while current is not None:
            result.append(str(current.data))
            current = current.next_node
        return '\n'.join(result)

    def sorted_insert(self, value):
        """Inserts a new Node into the correct sorted position.

        Args:
            value (int): The data value for the new node.
        """
        new_node = Node(value)

        # If list is empty, make new_node the head
        if self.__head is None:
            self.__head = new_node
            return

        # If new_node should be inserted before the head
        if self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        # Traverse the list to find the insertion point
        current = self.__head
        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node

        # Insert new_node after the current node
        new_node.next_node = current.next_node
        current.next_node = new_node
