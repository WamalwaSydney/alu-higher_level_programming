#!/usr/bin/python3
"""Unittest for max_integer([..])."""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function."""

    def test_max_at_end(self):
        """Test with max at the end."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_at_beginning(self):
        """Test with max at the beginning."""
        self.assertEqual(max_integer([4, 1, 2, 3]), 4)

    def test_max_in_middle(self):
        """Test with max in the middle."""
        self.assertEqual(max_integer([1, 4, 2, 3]), 4)

    def test_one_negative(self):
        """Test with one negative number."""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_only_negatives(self):
        """Test with only negative numbers."""
        self.assertEqual(max_integer([-10, -5, -3, -7]), -3)

    def test_one_element(self):
        """Test with list of one element."""
        self.assertEqual(max_integer([5]), 5)

    def test_empty_list(self):
        """Test with empty list."""
        self.assertIsNone(max_integer([]))
