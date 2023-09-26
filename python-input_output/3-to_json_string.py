#!/usr/bin/python3
"""
A function that returns the JSON representation of an object (string)
"""


def to_json_string(my_obj):
    """
    Serialize an object to its JSON representation (string).

    :param my_obj: The object to be serialized to JSON.
    :return: A JSON-formatted string representing the object.
    """
    import json

    return json.dumps(my_obj)
