#!/usr/bin/python3
"""Unit tests for Rectangle class"""
import unittest
import os
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """Test cases for Rectangle class"""

    def setUp(self):
        """Reset __nb_objects before each test"""
        Base._Base__nb_objects = 0

    def test_rectangle_creation(self):
        """Test Rectangle creation"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r1.id, 1)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.width, 2)
        self.assertEqual(r2.height, 10)
        self.assertEqual(r2.id, 2)

        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)

    def test_type_validation(self):
        """Test type validation"""
        with self.assertRaises(TypeError) as e:
            Rectangle("10", 2)
        self.assertEqual(str(e.exception), "width must be an integer")

        with self.assertRaises(TypeError) as e:
            Rectangle(10, "2")
        self.assertEqual(str(e.exception), "height must be an integer")

        with self.assertRaises(TypeError) as e:
            Rectangle(10, 2, "0", 0)
        self.assertEqual(str(e.exception), "x must be an integer")

        with self.assertRaises(TypeError) as e:
            Rectangle(10, 2, 0, "0")
        self.assertEqual(str(e.exception), "y must be an integer")

    def test_value_validation(self):
        """Test value validation"""
        with self.assertRaises(ValueError) as e:
            Rectangle(-10, 2)
        self.assertEqual(str(e.exception), "width must be > 0")

        with self.assertRaises(ValueError) as e:
            Rectangle(10, -2)
        self.assertEqual(str(e.exception), "height must be > 0")

        with self.assertRaises(ValueError) as e:
            Rectangle(0, 2)
        self.assertEqual(str(e.exception), "width must be > 0")

        with self.assertRaises(ValueError) as e:
            Rectangle(10, 0)
        self.assertEqual(str(e.exception), "height must be > 0")

        with self.assertRaises(ValueError) as e:
            Rectangle(10, 2, -1, 0)
        self.assertEqual(str(e.exception), "x must be >= 0")

        with self.assertRaises(ValueError) as e:
            Rectangle(10, 2, 0, -1)
        self.assertEqual(str(e.exception), "y must be >= 0")

    def test_area(self):
        """Test area calculation"""
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)

        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)

    def test_display(self):
        """Test display method"""
        r = Rectangle(2, 2)
        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), "##\n##\n")

    def test_str(self):
        """Test __str__ method"""
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r1), "[Rectangle] (12) 2/1 - 4/6")

        r2 = Rectangle(5, 5, 1)
        self.assertEqual(str(r2), "[Rectangle] (1) 1/0 - 5/5")

    def test_update_args(self):
        """Test update method with args"""
        r = Rectangle(10, 10, 10, 10)
        r.update(89)
        self.assertEqual(r.id, 89)
        r.update(89, 2)
        self.assertEqual(r.width, 2)
        r.update(89, 2, 3)
        self.assertEqual(r.height, 3)
        r.update(89, 2, 3, 4)
        self.assertEqual(r.x, 4)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(r.y, 5)

    def test_update_kwargs(self):
        """Test update method with kwargs"""
        r = Rectangle(10, 10, 10, 10)
        r.update(id=89)
        self.assertEqual(r.id, 89)
        r.update(width=2)
        self.assertEqual(r.width, 2)
        r.update(height=3)
        self.assertEqual(r.height, 3)
        r.update(x=4)
        self.assertEqual(r.x, 4)
        r.update(y=5)
        self.assertEqual(r.y, 5)

    def test_to_dictionary(self):
        """Test to_dictionary method"""
        r = Rectangle(10, 2, 1, 9)
        r_dict = r.to_dictionary()
        expected = {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}
        self.assertEqual(r_dict, expected)
        self.assertIsInstance(r_dict, dict)


if __name__ == '__main__':
    unittest.main()
