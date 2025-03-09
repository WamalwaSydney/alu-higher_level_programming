#!/usr/bin/python3
def uniq_add(my_list=[]):
    """
    Adds all unique integers in a list.
    Args:
        my_list: list of integers
    Returns:
        Sum of unique integers
    """
    return sum(set(my_list))
