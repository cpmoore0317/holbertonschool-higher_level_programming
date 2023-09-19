#!/usr/bin/python3
"""
Task 5
"""


def text_indentation(text):
    """
    Print a text with 2 new lines after each '.', '?', and ':' characters.

    Args:
        text (str): The input text to be processed.

    Raises:
        TypeError: If the input 'text' is not a string.

    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""
    in_whitespace = False

    for char in text:
        if char in ['.', '?', ':']:
            result += char + '\n\n'
            in_whitespace = True
        else:
            if char.isspace():
                if in_whitespace:
                    continue
                else:
                    result += ' '
                    in_whitespace = True
            else:
                result += char
                in_whitespace = False

    lines = result.split('\n')
    for line in lines:
        if line.strip():
            print(line)
