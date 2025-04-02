#!/usr/bin/python3
"""
Module for Rectangle class.
Inherits from BaseGeometry with implemented area and __str__ methods.
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

    def area(self):
        """
        Calculate the area of the rectangle

        Returns:
            The area of the rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        String representation of Rectangle

        Returns:
            String in the format [Rectangle] <width>/<height>
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
