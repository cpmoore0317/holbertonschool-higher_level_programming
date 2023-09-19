#!/usr/bin/python3
""" Writing a class based on 2-square.py. """


class Square:
    """
    This class represents a square.

    __size (int): The size of the square.

    __init__(self, size=0): Initializes a new Square instance with the given size.
    area(self): Calculates and returns the area of the square.
    """

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        def area(self):
            return self.__size ** 2
