#!/usr/bin/python3
"""
Module for inherits_from function.
Checks if object is an instance of a class that inherited from a class.
"""


def inherits_from(obj, a_class):
    """
    Checks if an object is an instance of a class that inherited from a class.

    Args:
        obj: The object to check
        a_class: The class to compare against

    Returns:
        True if object is an instance of a class that inherited from the class,
        otherwise False
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
