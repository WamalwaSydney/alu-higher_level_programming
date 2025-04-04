#!/usr/bin/python3
"""Test cases for Base class"""
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle

class TestBase(unittest.TestCase):
    """Test cases for Base class"""
    
    def setUp(self):
        Base._Base__nb_objects = 0

    # ID Tests
    def test_auto_id(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)
        
    def test_auto_id_increment(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_specified_id(self):
        b = Base(89)
        self.assertEqual(b.id, 89)

    # JSON Tests
    def test_to_json_string_none(self):
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_empty(self):
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_exists(self):
        self.assertEqual(Base.to_json_string([{"id": 12}]), '[{"id": 12}]')

    def test_from_json_string_none(self):
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty(self):
        self.assertEqual(Base.from_json_string("[]"), [])

    def test_from_json_string_exists(self):
        self.assertEqual(Base.from_json_string('[{"id": 89}]'), [{"id": 89}])

    # Create Tests
    def test_create_rectangle(self):
        r_dict = {"id": 89, "width": 1, "height": 2, "x": 3, "y": 4}
        r = Rectangle.create(**r_dict)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 1)

    # File Tests
    def test_save_to_file_none(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json") as f:
            self.assertEqual(f.read(), "[]")

    def test_load_from_file_missing(self):
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        self.assertEqual(Rectangle.load_from_file(), [])
