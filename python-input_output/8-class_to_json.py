#!/usr/bin/python3
"""
A function that returns the dictionary description with simple
data structure (list, dictionary, string, integer and boolean)
for JSON serialization of an object
"""


def class_to_json(obj):
    """
    Serialize an object's attributes to a dictionary with simple data structures
    suitable for JSON serialization.

    :param obj: An instance of a class with serializable attributes.
    :return: A dictionary representing the serialized object.
    """
    # Initialize an empty dictionary to store the serialized attributes.
    serialized_obj = {}

    # Get a list of all attributes of the object.
    attributes = dir(obj)

    # Iterate over the attributes.
    for attr_name in attributes:
        # Exclude special methods and attributes that start with '__'.
        if not callable(getattr(obj, attr_name)) and not attr_name.startswith("__"):
            # Get the attribute value and its type.
            attr_value = getattr(obj, attr_name)
            attr_type = type(attr_value)

            # Check if the attribute value is of a serializable type.
            if attr_type in (list, dict, str, int, bool):
                # Add the attribute to the serialized dictionary.
                serialized_obj[attr_name] = attr_value

    return serialized_obj