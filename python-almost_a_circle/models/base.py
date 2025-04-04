#!/usr/bin/python3
"""Base model class"""
import json
import os

class Base:
    """Base class for all models"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        return json.dumps(list_dictionaries) if list_dictionaries else "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        filename = f"{cls.__name__}.json"
        data = [obj.to_dictionary() for obj in list_objs] if list_objs else []
        with open(filename, "w") as f:
            f.write(cls.to_json_string(data))

    @staticmethod
    def from_json_string(json_string):
        return json.loads(json_string) if json_string else []

    @classmethod
    def create(cls, **dictionary):
        dummy = cls(1, 1) if cls.__name__ == "Rectangle" else cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        filename = f"{cls.__name__}.json"
        if not os.path.exists(filename):
            return []
        with open(filename, "r") as f:
            return [cls.create(**d) for d in cls.from_json_string(f.read())]
