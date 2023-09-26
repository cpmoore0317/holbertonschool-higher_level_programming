#!/usr/bin/python3
"""
A function that creates an Object from a “JSON file”
"""


def load_from_json_file(filename):
    """
    Deserialize a JSON file and return the corresponding Python data structure.

    :param filename: The name of the JSON file to be loaded.
    :return: A Python data structure representing the deserialized object.
    """
    import json

    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)