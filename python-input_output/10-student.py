#!/usr/bin/python3
"""
A class Student that defines a student by: (based on 9-student.py)
"""


class Student:
    """
    A class that defines a student with first_name, last_name, and age attributes.

    Public instance attributes:
    - first_name
    - last_name
    - age

    Methods:
    - to_json: Retrieve a dictionary representation of a Student instance.

    :param first_name: The first name of the student.
    :param last_name: The last name of the student.
    :param age: The age of the student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialize a Student instance with first_name, last_name, and age.

        :param first_name: The first name of the student.
        :param last_name: The last name of the student.
        :param age: The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieve a dictionary representation of a Student instance.

        :param attrs: A list of attribute names to be included in the dictionary.
                      If None, all attributes are included.
        :return: A dictionary with the specified or all student's attributes.
        """
        if attrs is None:
            return self.__dict__
        else:
            return {key: value for key, value in self.__dict__.items() if key in attrs}