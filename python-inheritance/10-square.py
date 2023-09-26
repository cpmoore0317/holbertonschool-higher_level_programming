#!/usr/bin/python3
"""
This module contains one class: Square, that inherits from Rectangle
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class representing a square.
    """

    def __init__(self, size):
        """
        Initialize a Square instance.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than or equal to 0.
        """
        super().__init__(size, size)  # Call the parent class's constructor with the same size for both width and height

    def __str__(self):
        """
        Return a string representation of the Square instance.

        Returns:
            str: A string in the format "[Square] <size>/<size>".
        """
        return "[Square] {}/{}".format(self._Rectangle__width, self._Rectangle__height)  # Access private attributes of the base class

    # The area() method is inherited from Rectangle, so there's no need to override it here

    # You don't need to define integer_validator here as it's inherited from Rectangle
