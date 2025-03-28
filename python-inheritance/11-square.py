#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    def __init__(self, size):
        self.integer_validator("size", size)
        self._Rectangle__width = size
        self._Rectangle__height = size
    def area(self):
        return self._Rectangle__width * self._Rectangle__height
    def __str__(self):
        return "[Square] {}/{}".format(self._Rectangle__width, self._Rectangle__height)
