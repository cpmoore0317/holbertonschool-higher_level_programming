#!/usr/bin/python3
"""
A  a class Student that defines a student
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

    def to_json(self):
        """
        Retrieve a dictionary representation of a Student instance.

        :return: A dictionary with the student's attributes.
        """
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age
        }