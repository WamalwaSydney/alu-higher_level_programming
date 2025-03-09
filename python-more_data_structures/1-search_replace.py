#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """
    Replaces all occurrences of an element by another in a new list.
    Args:
        my_list: the initial list
        search: the element to replace
        replace: the new element
    Returns:
        A new list with replacements
    """
    return [replace if item == search else item for item in my_list]
