#!/usr/bin/python3
"""
Read file function
"""


def read_file(filename=""):
    """
    Read and print the contents of a text file.

    Args:
        filename (str): The name of the file to be read.

    Returns:
        None

    Notes:
        This function reads the contents of a text file and prints them to the standard output (stdout).
        If the file does not exist, it silently handles the `FileNotFoundError` without raising an exception.

    Example:
        >>> read_file("my_file.txt")
        This is the content of my_file.txt.
    """
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            print(file.read(), end="")
    except FileNotFoundError:
        pass

if __name__ == "__main__":
    read_file("my_file_0.txt")