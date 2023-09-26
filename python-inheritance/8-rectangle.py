#!/usr/bin/python3
"""
This module contains one class: Rectangle, that inherits from BaseGeometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class representing a rectangle.
    """

    def __init__(self, width, height):
        """
        Initialize a Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            TypeError: If either width or height is not an integer.
            ValueError: If either width or height is less than or equal to 0.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """
        Return a string representation of the Rectangle instance.

        Returns:
            str: A string in the format "[Rectangle] <width>/<height>".
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
