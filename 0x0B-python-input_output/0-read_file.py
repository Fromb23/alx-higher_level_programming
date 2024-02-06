#!/usr/bin/python3
"""A script to read and print the content of a file."""


def read_file(filename=""):
    """
    Read the content of a file and print it.

    Args:
        filename (str): The name of the file to be read.

    Returns:
        None
    """
    with open(filename, 'r') as file:
        content = file.read()
        print(content, end='')
