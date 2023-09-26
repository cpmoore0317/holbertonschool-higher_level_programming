#!/usr/bin/python3
"""
This module contains one function: inherits_from
"""


def inherits_from(obj, a_class):
    """
    Check if an object is an instance of a class that inherited
    (directly or indirectly) from the specified class.

    Args:
        obj: The object to check.
        a_class: The class to check against.

    Returns:
        True if obj is an instance of a class that inherited
        from a_class, otherwise False.
    """
    if type(obj) is a_class:
        return False
    return issubclass(type(obj), a_class)
