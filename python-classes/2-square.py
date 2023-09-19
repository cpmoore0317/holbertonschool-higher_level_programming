#!/usr/bin/python3
""" Defines a square. """


class Sqaure:
    """ Defining class Square. """

    def __init__(self, size=0):
        """ Initializing Square with a size. """
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
