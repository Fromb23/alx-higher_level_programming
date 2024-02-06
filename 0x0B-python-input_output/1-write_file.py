#!/usr/bin/python3
"""Writes a string to a text file (UTF8) and returns th
number of characters written.
"""


def write_file(filename="", text=""):
    """Writes text to a file and returns the number
    of characters written.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        _written = file.write(text)
    return (_written)
