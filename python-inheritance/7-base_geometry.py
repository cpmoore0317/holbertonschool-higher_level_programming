#!/usr/bin/python3
"""
This module contains one class: BaseGeometry
"""


class BaseGeometry:
    """
    A class representing basic geometry operations.
    """

    def area(self):
        """
        Calculate the area.

        Raises:
            Exception: Always raises an Exception with the message "area() is not implemented."
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate that a value is an integer and greater than 0.

        Args:
            name (str): The name of the value being validated.
            value (int): The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
