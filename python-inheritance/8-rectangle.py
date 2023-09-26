#!/usr/bin/python3
"""
This module contains one class: Rectangle, that inherits from BaseGeometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Contains __init__ method """
    def __init__(self, width, height):
        """
        Initialization
        """
        super().integer_validator("width", width).integer_validator("height", height)
        self.__width = width
        self.__height = height
