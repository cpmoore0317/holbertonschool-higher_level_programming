#!/usr/bin/python3
"""
Module for the Base class.
"""


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
