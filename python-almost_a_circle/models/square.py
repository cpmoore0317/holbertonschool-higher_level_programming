#!/usr/bin/python3
"""
Module for the Square class.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    The `Square` class represents a square and inherits from
    the `Rectangle` class.

    Attributes:
        id (int): An identifier for the square.
        size (int): The size of the square.
        x (int): The x-coordinate of the square's position.
        y (int): The y-coordinate of the square's position.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a new instance of the `Square` class.

        Args:
            size (int): The size of the square.
            x (int, optional): The x-coordinate of the square's
            position (default is 0).
            y (int, optional): The y-coordinate of the square's
            position (default is 0).
            id (int, optional): An optional identifier for the
            square (default is None).
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Get the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.width

    @size.setter
    def size(self, size):
        """
        Set the size of the square.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If `size` is not an integer.
            ValueError: If `size` is less than or equal to 0.
        """
        self.width = size
        self.height = size

    def __str__(self):
        """
        Return a string representation of the square.

        Returns:
            str: A string in the format "[Square] (<id>) <x>/<y> - <size>"
        """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)
