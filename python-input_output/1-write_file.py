#!/usr/bin/python3
"""
A function that writes a string to a text file (UTF8) and returns the
number of characters written
"""


def write_file(filename="", text=""):
    """
    Write text to a text file and return the number of characters written.

    Args:
        filename (str): The name of the file to be written.
        text (str): The text to be written to the file.

    Returns:
        int: The number of characters written to the file.

    Notes:
        This function opens the specified file in write mode
        ('w') and writes the provided text to it.
        If the file already exists, it will be overwritten.
        If the file does not exist, it will be created.
        The function returns the number of characters
        successfully written to the file.

    Example:
        >>> nb_characters = write_file("my_first_file.txt",
        "This School is so cool!\n")
        >>> print(nb_characters)
        24
    """
    try:
        with open(filename, mode='w', encoding='utf-8') as file:
            nb_characters = file.write(text)
        return nb_characters
    except Exception:
        return 0


if __name__ == "__main__":
    nb_characters = write_file("my_first_file.txt", "This School is so cool!")
    print(nb_characters)
