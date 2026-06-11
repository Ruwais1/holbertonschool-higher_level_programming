#!/usr/bin/python3
"""
Unittest for max_integer([..]) module.
This module defines test cases to evaluate the `max_integer` function.
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Defines suite of unit tests for the max_integer function."""

    def test_ordered_list(self):
        """Test with a standard ordered list of integers."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test with an unordered list of integers."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """Test with the maximum value at the start of the list."""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_empty_list(self):
        """Test with an empty list which should return None."""
        self.assertIsNone(max_integer([]))

    def test_one_element_list(self):
        """Test with a list containing only a single element."""
        self.assertEqual(max_integer([7]), 7)

    def test_all_negative_numbers(self):
        """Test with a list of completely negative integers."""
        self.assertEqual(max_integer([-1, -5, -2, -10]), -1)

    def test_mixed_negative_positive(self):
        """Test with a mixture of negative and positive integers."""
        self.assertEqual(max_integer([-10, 5, -2, 3]), 5)


if __name__ == '__main__':
    unittest.main()
