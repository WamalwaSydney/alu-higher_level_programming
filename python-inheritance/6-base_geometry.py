#!/usr/bin/python3
"""
Module for BaseGeometry class.
Includes area method that raises an exception.
"""


class BaseGeometry:
    """
    BaseGeometry class with area method

    Methods:
        area: raises an Exception
    """

    def area(self):
        """
        Area method that raises an Exception

        Raises:
            Exception: with message "area() is not implemented"
        """
        raise Exception("area() is not implemented")
