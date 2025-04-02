#!/usr/bin/python3
"""
Module for is_kind_of_class function.
Checks if object is an instance of, or inherited from, a class.
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if an object is an instance of, or inherited from, a class.

    Args:
        obj: The object to check
        a_class: The class to compare against

    Returns:
        True if object is an instance of or inherited from the class,
        otherwise False
    """
    return isinstance(obj, a_class)
