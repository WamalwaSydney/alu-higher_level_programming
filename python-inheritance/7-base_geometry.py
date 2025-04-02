#!/usr/bin/python3
"""
Module for BaseGeometry class.
Includes area method and integer validator.
"""


class BaseGeometry:
    """
    BaseGeometry class with area method and integer validator

    Methods:
        area: raises an Exception
        integer_validator: validates that a value is a positive integer
    """

    def area(self):
        """
        Area method that raises an Exception

        Raises:
            Exception: with message "area() is not implemented"
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that value is a positive integer

        Args:
            name: name of the value (always a string)
            value: value to validate

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than or equal to 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
