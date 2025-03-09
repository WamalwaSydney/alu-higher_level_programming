#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """
    Replaces an element of a list at a specific position.
    Args:
        my_list: the list
        idx: the index
        element: the new element
    Returns:
        The modified list or the original list if idx is negative or out of range
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    my_list[idx] = element
    return my_list
