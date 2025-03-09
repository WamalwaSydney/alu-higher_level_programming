#!/usr/bin/python3
def max_integer(my_list=[]):
    """
    Finds the biggest integer of a list.
    Args:
        my_list: the list of integers
    Returns:
        The max integer in the list
        If the list is empty, returns None
    """
    if not my_list:
        return None
    
    max_value = my_list[0]
    for value in my_list:
        if value > max_value:
            max_value = value
    
    return max_value
