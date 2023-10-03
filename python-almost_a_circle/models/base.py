#!/usr/bin/python3
"""
Module for the Base class.
"""
import json


class Base:
    """
    The `Base` class serves as the foundation for all other classes in
    this project.

    Attributes:
        __nb_objects (int): A private class attribute to keep track of the
        number of instances created.

        id (int): A public instance attribute representing the unique
        identifier of an instance.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a new instance of the `Base` class.

        Args:
            id (int, optional): An optional integer to set as the
            unique identifier.
            If not provided, a unique identifier will be
            automatically generated.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Convert a list of dictionaries to a JSON string.

        Args:
            list_dictionaries (list): A list of dictionaries.

        Returns:
            str: A JSON string representation of the list of dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Save a list of instances to a JSON file.

        Args:
            list_objs (list): A list of instances.

        Returns:
            None
        """
        lst = []
        if list_objs is not None and len(list_objs) > 0:
            for obj in list_objs:
                lst.append(obj.to_dictionary())
        with open(cls.__name__ + ".json", 'w') as f:
            f.write(Base.to_json_string(lst))

    @staticmethod
    def from_json_string(json_string):
        """
        Convert a JSON string to a list of dictionaries.

        Args:
            json_string (str): A JSON string representation.

        Returns:
            list: A list of dictionaries represented by the JSON string.
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)
