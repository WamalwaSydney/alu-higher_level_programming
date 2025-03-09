#!/usr/bin/python3
def element_at(my_list, idx):
    """
    Retrieves an element from a list like in C.
    Args:
        my_list: the list
        idx: the index
    Returns:
        The element at index idx or None if idx is negative or out of range
    """
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]
