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

    def update(self, *args, **kwargs):
        """
        Update the attributes of the square with the provided arguments.

        Args:
            *args: Positional arguments to update the square attributes in
            the following order:
                1st argument: id attribute
                2nd argument: size attribute
                3rd argument: x attribute
                4th argument: y attribute
            **kwargs: Keyword arguments to update the square attributes
            by name.
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """
        Return a string representation of the square.

        Returns:
            str: A string in the format "[Square] (<id>) <x>/<y> - <size>"
        """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)
