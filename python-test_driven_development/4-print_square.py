#!/usr/bin/python3
"""Module to print a square."""

def print_square(size):
    """Prints a square of # characters.
    
    Args:
        size (int): Size length of the square.
    
    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is negative.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
