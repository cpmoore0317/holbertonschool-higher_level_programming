#!/usr/bin/python3
"""
Square for 11
"""
class Square(Rectangle):
    """
    A class representing a square, which is a special case of a rectangle.

    Attributes:
        __size (int): The size of the square.

    Methods:
        __init__(self, size): Initializes a Square instance with a given size.
        area(self): Calculates and returns the area of the square.
        __str__(self): Returns a string representation of the Square.
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

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def __str__(self):
        """
        Returns a string representation of the Square.

        Returns:
            str: A string in the format "[Square] <size>/<size>".
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
