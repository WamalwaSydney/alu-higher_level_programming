#!/usr/bin/python3
class BaseGeometry:
    """BaseGeometry class with a method that raises an exception"""
    def area(self):
        raise Exception("area() is not implemented")
