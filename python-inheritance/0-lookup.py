#!/usr/bin/python3
"""
Module for lookup function.
Returns attributes and methods of an object.
"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.

    Args:
        obj: The object to inspect

    Returns:
        A list of attributes and methods
    """
    return dir(obj)
