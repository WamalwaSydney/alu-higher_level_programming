#!/usr/bin/python3
"""
Module for appending a string at the end of a text file.
"""


def append_write(filename="", text=""):
    """
    Append a string at the end of a text file and return characters added.

    Args:
        filename (str): The name of the file to append to.
        text (str): The text to append to the file.

    Returns:
        int: The number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
