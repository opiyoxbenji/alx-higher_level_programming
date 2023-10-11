#!/usr/bin/python3
"""Returns the number of characters"""


def append_write(filename="", text=""):
    """Appends a string to the end of a text file (UTF8)"""

    with open(filename, 'a', encoding='utf-8') as file:
        num_characters_added = file.write(text)

    return num_characters_added
