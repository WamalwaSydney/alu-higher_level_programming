#!/usr/bin/python3
"""
Module for loading an object from a JSON file.
"""
import json


def load_from_json_file(filename):
    """
    Create an Object from a JSON file.

    Args:
        filename (str): The name of the file to load from.

    Returns:
        object: The Python object represented by the JSON file.
    """
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
