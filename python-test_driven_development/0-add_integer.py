#!/usr/bin/python3
"""Module to add two integers."""

def add_integer(a, b=98):
    """Adds two integers or floats.
    
    Args:
        a (int/float): First number.
        b (int/float, optional): Second number. Defaults to 98.
    
    Raises:
        TypeError: If a or b is not an integer or float.
    
    Returns:
        int: Sum of a and b after casting to integers.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
