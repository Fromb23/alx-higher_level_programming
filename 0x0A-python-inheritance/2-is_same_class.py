#!/usr/bin/python3
"""
This module defines a function for checking if
an object is an instance of a specific class.
"""


def is_same_class(obj, a_class):
    """
    Checks if the given object is an instance of the specified class.

    Args:
        obj: The object to be checked.
        a_class: The class to check against.

    Returns:
        bool: True if the object is an instance
            of the specified class, False otherwise.
    """
    if type(obj) is a_class:
        return True
    else:
        return False
