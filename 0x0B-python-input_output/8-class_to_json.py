#!/usr/bin/python3
"""
This script defines a function to convert a class
instance to a JSON-compatible dictionary.
"""


def class_to_json(obj):
    """
    Convert a class instance to a JSON-compatible dictionary.

    Parameters:
    obj: An instance of a class.

    Returns:
    A dictionary representing the attributes of the class instance.
    """
    return obj.__dict__
