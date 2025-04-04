#!/usr/bin/python3
"""Module to find the max integer in a list."""

def max_integer(list=[]):
    """Finds and returns the max integer in a list of integers.
    
    Args:
        list (list): List of integers.
    
    Returns:
        int or None: Max integer in list, or None if list is empty.
    """
    if len(list) == 0:
        return None
    result = list[0]
    for num in list[1:]:
        if num > result:
            result = num
    return result
