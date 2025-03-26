#!/usr/bin/python3
"""Module 1-square
This module defines a Square class with a private size attribute.
"""

class Square:
    """A class that defines a square with a private size attribute."""
    def __init__(self, size):
        """Initialize a new Square.
        Args:
            size (int): The size of the square.
        """
        self.__size = size

    @property
    def dict_(self):
        """Return the dictionary of attributes."""
        return self.__dict__
