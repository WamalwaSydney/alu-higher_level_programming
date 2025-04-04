#!/usr/bin/python3
"""Test cases for Rectangle class"""
import unittest
import os
import io
import sys
from models.rectangle import Rectangle
from models.base import Base

class TestRectangle(unittest.TestCase):
    """Test cases for Rectangle class"""
    
    def setUp(self):
        self.r = Rectangle(10, 20)

    # Init Tests
    def test_rectangle_creation(self):
        self.assertEqual(self.r.width, 10)
        self.assertEqual(self.r.height, 20)

    def test_full_initialization(self):
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r.id, 5)

    # Validation Tests
    def test_width_validation(self):
        with self.assertRaises(TypeError):
            Rectangle("10", 20)
        with self.assertRaises(ValueError):
            Rectangle(0, 20)
        with self.assertRaises(ValueError):
            Rectangle(-10, 20)

    # Method Tests
    def test_area(self):
        self.assertEqual(self.r.area(), 200)

    def test_str(self):
        self.assertEqual(str(self.r), f"[Rectangle] ({self.r.id}) 0/0 - 10/20")

    def test_display(self):
        r = Rectangle(2, 2)
        expected = "##\n##\n"
        with io.StringIO() as buf, redirect_stdout(buf):
            r.display()
            self.assertEqual(buf.getvalue(), expected)

    def test_update_args(self):
        self.r.update(89, 5, 6, 2, 3)
        self.assertEqual(self.r.id, 89)
        self.assertEqual(self.r.width, 5)

    def test_to_dictionary(self):
        d = self.r.to_dictionary()
        self.assertEqual(d["width"], 10)
        self.assertEqual(d["height"], 20)

def redirect_stdout(stream):
    """Redirect stdout to stream"""
    sys.stdout = stream
    return stream
