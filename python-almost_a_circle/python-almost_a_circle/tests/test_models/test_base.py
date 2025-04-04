#!/usr/bin/python3
"""Unit tests for Base class"""
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Test cases for Base class"""

    def setUp(self):
        """Reset __nb_objects before each test"""
        Base._Base__nb_objects = 0

    def test_id_assignment(self):
        """Test automatic ID assignment"""
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base()
        self.assertEqual(b3.id, 3)

    def test_specified_id(self):
        """Test specified ID assignment"""
        b = Base(89)
        self.assertEqual(b.id, 89)

    def test_to_json_string(self):
        """Test to_json_string method"""
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string([{'id': 12}]), '[{"id": 12}]')

    def test_from_json_string(self):
        """Test from_json_string method"""
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string("[]"), [])
        self.assertEqual(Base.from_json_string('[{"id": 89}]'), [{'id': 89}])

    def test_save_to_file(self):
        """Test save_to_file method"""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")
        os.remove("Rectangle.json")

        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")
        os.remove("Rectangle.json")

        r = Rectangle(1, 2)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) > 0)
        os.remove("Rectangle.json")

    def test_create(self):
        """Test create method"""
        r_dict = {'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4}
        r = Rectangle.create(**r_dict)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

    def test_load_from_file(self):
        """Test load_from_file method"""
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        self.assertEqual(Rectangle.load_from_file(), [])

        r = Rectangle(1, 2)
        Rectangle.save_to_file([r])
        loaded = Rectangle.load_from_file()
        self.assertEqual(len(loaded), 1)
        self.assertEqual(loaded[0].width, 1)
        self.assertEqual(loaded[0].height, 2)
        os.remove("Rectangle.json")


if __name__ == '__main__':
    unittest.main()
