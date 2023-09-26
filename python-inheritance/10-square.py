#!/usr/bin/python3
"""
Class for num 10
"""
class Square(Rectangle):
    """
    A class representing a square, inheriting from Rectangle.
    """

    def __init__(self, size):
        """
        Initializes a Square instance with a given size.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than or equal to 0.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """
        Returns a string representation of the Square.

        Args:
            None

        Returns:
            str: A string representation of the Square.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
