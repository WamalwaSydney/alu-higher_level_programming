#!/usr/bin/python3
"""Test cases for Square class"""
import unittest
import os
from models.square import Square
from models.base import Base

class TestSquare(unittest.TestCase):
    def test_init(self):
        s = Square(5)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.width, 5)

    def test_size_validation(self):
        with self.assertRaises(ValueError):
            Square(-5)
        with self.assertRaises(TypeError):
            Square("5")

    def test_str(self):
        s = Square(5, 2, 3, 4)
        self.assertEqual(str(s), "[Square] (4) 2/3 - 5")

    def test_update_args(self):
        s = Square(1, 1, 1, 1)
        s.update(2, 3, 4, 5)
        self.assertEqual(s.id, 2)
        self.assertEqual(s.size, 3)

    def test_to_dictionary(self):
        s = Square(5, 2, 3, 4)
        self.assertEqual(s.to_dictionary()['size'], 5)
