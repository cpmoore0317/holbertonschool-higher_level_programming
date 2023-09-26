#!/usr/bin/python3
"""
A script that adds all arguments to a Python list,
and then save them to a file
"""

import sys
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

def add_args_to_list_and_save(args):
    """
    Add command line arguments to a Python list and save it to a JSON file.

    :param args: A list of command line arguments.
    """
    # Load the existing list from the file or create an empty list if the file doesn't exist.
    try:
        existing_list = load_from_json_file('add_item.json')
    except FileNotFoundError:
        existing_list = []

    # Add the new arguments to the existing list.
    existing_list.extend(args)

    # Save the updated list to a JSON file.
    save_to_json_file(existing_list, 'add_item.json')

if __name__ == "__main__":
    # Extract command line arguments excluding the script name.
    arguments = sys.argv[1:]

    # Add the arguments to the list and save it to the file.
    add_args_to_list_and_save(arguments)