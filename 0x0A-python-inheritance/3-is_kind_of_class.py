#!/usr/bin/python3
"""
Module: Utility functions for class checks.
"""


def is_kind_of_class(obj, a_class):
    """
    Check if the object is an instance or subclass of a specific class.
    Returns True if yes, False otherwise.
    """

    if isinstance(obj, a_class):
        return True
    else:
        return False
