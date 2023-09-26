#!/usr/bin/python3
"""
Func for num 3
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if an object is an instance of, or inherited from, the specified
    class.

    Args:
        obj: The object to check.
        a_class: The class to compare with.

    Returns:
        True if the object is an instance of, or inherited from,
        the specified class; otherwise, False.
    """
    return isinstance(obj, a_class)
