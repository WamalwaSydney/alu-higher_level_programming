#!/usr/bin/python3
"""Test cases for Square class"""
import unittest
import os
from models.square import Square
from models.base import Base

class TestSquare(unittest.TestCase):
    """Test cases for Square class"""
    
    def setUp(self):
        self.s = Square(5)

    # Init Tests
    def test_square_creation(self):
        self.assertEqual(self.s.size, 5)
        self.assertEqual(self.s.width, 5)

    def test_full_initialization(self):
        s = Square(1, 2, 3, 4)
        self.assertEqual(s.id, 4)

    # Validation Tests
    def test_size_validation(self):
        with self.assertRaises(TypeError):
            Square("5")
        with self.assertRaises(ValueError):
            Square(-5)
        with self.assertRaises(ValueError):
            Square(0)

    # Method Tests
    def test_str(self):
        self.assertEqual(str(self.s), f"[Square] ({self.s.id}) 0/0 - 5")

    def test_update_args(self):
        self.s.update(89, 10, 2, 3)
        self.assertEqual(self.s.id, 89)
        self.assertEqual(self.s.size, 10)

    def test_to_dictionary(self):
        d = self.s.to_dictionary()
        self.assertEqual(d["size"], 5)
        self.assertEqual(d["x"], 0)
