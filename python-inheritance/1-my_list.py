#!/usr/bin/python3
"""
Module for MyList class.
Inherits from list and adds print_sorted method.
"""


class MyList(list):
    """
    Class that inherits from list

    Methods:
        print_sorted: prints the list in ascending order
    """

    def print_sorted(self):
        """
        Prints the list in ascending order
        """
        print(sorted(self))
