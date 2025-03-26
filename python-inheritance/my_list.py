#!/usr/bin/python3
class MyList(list):
    """A subclass of list with an additional method to print sorted list"""
    def print_sorted(self):
        print(sorted(self))
