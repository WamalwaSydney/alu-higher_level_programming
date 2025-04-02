#!/usr/bin/python3
"""
Module for is_same_class function.
Checks if object is exactly an instance of specified class.
"""


def is_same_class(obj, a_class):
    """
    Checks if an object is exactly an instance of the specified class.

    Args:
        obj: The object to check
        a_class: The class to compare against

    Returns:
        True if object is exactly an instance of the specified class,
        otherwise False
    """
    return type(obj) is a_class
