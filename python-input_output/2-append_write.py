#!/usr/bin/python3
"""
A function that appends a string at the end of a text file (UTF8) and
returns the number of characters added
"""


def append_write(filename="", text=""):
    """
    Append the given text to the end of a text file (UTF-8) and
    return the number of characters added.

    If the file doesn’t exist, it will be created.

    :param filename: The name of the file to append to.
    :param text: The text to append to the file.
    :return: The number of characters added to the file.
    """
    try:
        with open(filename, 'a', encoding='utf-8') as file:
            file.write(text)
            return len(text)
    except Exception as e:
        # Handle any exceptions that might occur
        # (e.g., permission errors, disk full)
        print(f"An error occurred: {e}")
        return 0  # Return 0 to indicate no characters
        # were added due to the error

# Example usage:
if __name__ == "__main__":  
    nb_characters_added = append_write("file_append.txt", 
                                       "This School is so cool!\n")
    print(nb_characters_added)
