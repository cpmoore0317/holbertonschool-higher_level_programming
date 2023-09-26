#!/usr/bin/python3
"""
Class for num 7
"""


class BaseGeometry:
    """
    A base geometry class.
    """

    def area(self):
        """
        Raises an Exception with the message "area() is not implemented."

        Args:
            None

        Raises:
            Exception: Always raises an Exception with the specified message.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the value to ensure it is an integer greater than 0.

        Args:
            name (str): The name of the value being validated.
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
