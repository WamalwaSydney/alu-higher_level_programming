#!/usr/bin/python3
"""Module to print a name."""

def say_my_name(first_name, last_name=""):
    """Prints the formatted name.
    
    Args:
        first_name (str): First name.
        last_name (str, optional): Last name. Defaults to "".
    
    Raises:
        TypeError: If names are not strings.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
