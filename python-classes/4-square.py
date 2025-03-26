#!/usr/bin/python3
"""Module 4-square
This module defines a Square class with a private size attribute and its getter and setter.
"""

class Square:
    """A class that defines a square with a controlled size attribute."""
    def __init__(self, size=0):
        """Initialize a new Square.
        Args:
            size (int): The size of the square.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation.
        Args:
            value (int): The new size of the square.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current square area."""
        return self.__size * self.__size

    @property
    def dict_(self):
        """Return the dictionary of attributes."""
        return self.__dict__
