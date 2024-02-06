#!/usr/bin/python3
"""Appends a string to a text file (UTF8) and returns
the number of characters appended.
"""


def append_write(filename="", text=""):
    """
    Appends text to a file and returns the
    number of characters appended.
    """
    with open(filename, 'a', encoding='utf-8') as file:
        _append = file.write(text)
    return _append
