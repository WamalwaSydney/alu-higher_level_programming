#!/usr/bin/python3
"""
Module for Square class.
Inherits from Rectangle.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle

    Attributes:
        __size: private size of the square
    """

    def __init__(self, size):
        """
        Initialize Square with size

        Args:
            size: size of the square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Calculate the area of the square

        Returns:
            The area of the square
        """
        return self.__size ** 2
