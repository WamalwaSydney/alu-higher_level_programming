#!/usr/bin/python3
"""Unit tests for Square class"""
import unittest
import os
from models.square import Square
from models.base import Base


class TestSquare(unittest.TestCase):
    """Test cases for Square class"""

    def setUp(self):
        """Reset __nb_objects before each test"""
        Base._Base__nb_objects = 0

    def test_square_creation(self):
        """Test Square creation"""
        s1 = Square(5)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)
        self.assertEqual(s1.id, 1)

        s2 = Square(2, 2)
        self.assertEqual(s2.size, 2)
        self.assertEqual(s2.x, 2)
        self.assertEqual(s2.id, 2)

        s3 = Square(3, 1, 3)
        self.assertEqual(s3.size, 3)
        self.assertEqual(s3.x, 1)
        self.assertEqual(s3.y, 3)
        self.assertEqual(s3.id, 3)

        s4 = Square(1, 2, 3, 4)
        self.assertEqual(s4.id, 4)

    def test_type_validation(self):
        """Test type validation"""
        with self.assertRaises(TypeError) as e:
            Square("5")
        self.assertEqual(str(e.exception), "width must be an integer")

        with self.assertRaises(TypeError) as e:
            Square(5, "2")
        self.assertEqual(str(e.exception), "x must be an integer")

        with self.assertRaises(TypeError) as e:
            Square(5, 2, "3")
        self.assertEqual(str(e.exception), "y must be an integer")

    def test_value_validation(self):
        """Test value validation"""
        with self.assertRaises(ValueError) as e:
            Square(-5)
        self.assertEqual(str(e.exception), "width must be > 0")

        with self.assertRaises(ValueError) as e:
            Square(0)
        self.assertEqual(str(e.exception), "width must be > 0")

        with self.assertRaises(ValueError) as e:
            Square(5, -2)
        self.assertEqual(str(e.exception), "x must be >= 0")

        with self.assertRaises(ValueError) as e:
            Square(5, 2, -3)
        self.assertEqual(str(e.exception), "y must be >= 0")

    def test_str(self):
        """Test __str__ method"""
        s1 = Square(4, 2, 1, 12)
        self.assertEqual(str(s1), "[Square] (12) 2/1 - 4")

        s2 = Square(5, 1)
        self.assertEqual(str(s2), "[Square] (1) 1/0 - 5")

    def test_size_property(self):
        """Test size property"""
        s = Square(5)
        self.assertEqual(s.size, 5)
        s.size = 10
        self.assertEqual(s.size, 10)
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)

        with self.assertRaises(TypeError) as e:
            s.size = "9"
        self.assertEqual(str(e.exception), "width must be an integer")

    def test_update_args(self):
        """Test update method with args"""
        s = Square(5)
        s.update(89)
        self.assertEqual(s.id, 89)
        s.update(89, 2)
        self.assertEqual(s.size, 2)
        s.update(89, 2, 3)
        self.assertEqual(s.x, 3)
        s.update(89, 2, 3, 4)
        self.assertEqual(s.y, 4)

    def test_update_kwargs(self):
        """Test update method with kwargs"""
        s = Square(5)
        s.update(id=89)
        self.assertEqual(s.id, 89)
        s.update(size=2)
        self.assertEqual(s.size, 2)
        s.update(x=3)
        self.assertEqual(s.x, 3)
        s.update(y=4)
        self.assertEqual(s.y, 4)

    def test_to_dictionary(self):
        """Test to_dictionary method"""
        s = Square(10, 2, 1)
        s_dict = s.to_dictionary()
        expected = {'id': 1, 'x': 2, 'size': 10, 'y': 1}
        self.assertEqual(s_dict, expected)
        self.assertIsInstance(s_dict, dict)


if __name__ == '__main__':
    unittest.main()
