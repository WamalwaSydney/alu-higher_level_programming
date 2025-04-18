#!/usr/bin/python3
"""
Module for Rectangle class.
Inherits from BaseGeometry.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle class that inherits from BaseGeometry

    Attributes:
        __width: private width of the rectangle
        __height: private height of the rectangle
    """

    def __init__(self, width, height):
        """
        Initialize Rectangle with width and height

        Args:
            width: width of the rectangle
            height: height of the rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
