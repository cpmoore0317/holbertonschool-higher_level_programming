#!/usr/bin/python3
"""
A function that writes an Object to a text file,
using a JSON representation
"""

def save_to_json_file(my_obj, filename):
    """
    Serialize an object to its JSON representation and save it to a text file.

    :param my_obj: The object to be serialized to JSON.
    :param filename: The name of the file where the JSON data will be saved.
    """
    import json

    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)