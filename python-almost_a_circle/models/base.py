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
