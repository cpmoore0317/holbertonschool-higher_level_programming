#!/usr/bin/python3
"""
Func for num 4
"""
def inherits_from(obj, a_class):
    """
    Checks if an object is an instance of a class that inherited (directly or indirectly) from the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare with.

    Returns:
        True if the object is an instance of a class that inherited from the specified class; otherwise, False.
    """
    return issubclass(type(obj), a_class)
