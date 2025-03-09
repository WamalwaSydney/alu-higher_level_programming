#!/usr/bin/python3
def no_c(my_string):
    """
    Removes all characters c and C from a string.
    Args:
        my_string: the input string
    Returns:
        The new string without c and C
    """
    new_string = ""
    for char in my_string:
        if char != 'c' and char != 'C':
            new_string += char
    return new_string
