#!/usr/bin/python3
"""
A function that returns an object (Python data structure)
represented by a JSON string
"""


def from_json_string(my_str):
    """
    Deserialize a JSON-formatted string and
    return the corresponding Python data structure.

    :param my_str: A JSON-formatted string.
    :return: A Python data structure representing the deserialized object.
    """
    import json

    return json.loads(my_str)
