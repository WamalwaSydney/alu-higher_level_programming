#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """
    Replaces or adds key/value in a dictionary.
    Args:
        a_dictionary: the dictionary
        key: the key to add or update
        value: the value to associate with the key
    Returns:
        Updated dictionary
    """
    a_dictionary[key] = value
    return a_dictionary
