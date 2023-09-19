#!/usr/bin/python3
""" Writing a class based on 2-square.py. """


class Square:
    """ Defining and empty class named square. """

    def __init__(self, size=0):

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        def area(self)

            return self.__size ** 2
