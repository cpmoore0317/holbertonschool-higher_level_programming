#!/usr/bin/python3
"""
Task 5
"""

def print_square(size):
    """
    Print a square of a specified size with the character #.

    Args:
        size (int): The size of the square.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.

    Example:
        >>> print_square(4)
        ####
        ####
        ####
        ####
        >>> print_square(10)
        ##########
        ##########
        ##########
        ##########
        ##########
        ##########
        ##########
        ##########
        ##########
        ##########
        >>> print_square(0)
        >>> print_square(1)
        #
        >>> print_square(-1)
        Traceback (most recent call last):
            ...
        ValueError: size must be >= 0
    """
    if not isinstance(size, int) or (isinstance(size, float) and size < 0):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
