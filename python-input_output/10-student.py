#!/usr/bin/python3
"""
Module for the Student class with a filtered to_json method.
"""


class Student:
    """
    Class that defines a student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialize a new Student.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieve a dictionary representation of a Student instance.

        Args:
            attrs (list, optional): A list of attribute names to retrieve.
                If None, all attributes are retrieved.

        Returns:
            dict: The dictionary representation.
        """
        if attrs is None:
            return self.__dict__

        return {attr: getattr(self, attr)
                for attr in attrs if hasattr(self, attr)}
