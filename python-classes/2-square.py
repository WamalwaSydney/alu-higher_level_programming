#!/usr/bin/python3
"""Module 2-square
This module defines a Square class with a private size attribute and validation.
"""

class Square:
    """A class that defines a square with size validation."""
    def __init__(self, size=0):
        """Initialize a new Square.
        Args:
            size (int): The size of the square. Must be >= 0.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def dict_(self):
        """Return the dictionary of attributes."""
        return self.__dict__
