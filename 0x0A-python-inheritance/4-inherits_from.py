#!/usr/bin/python3
"""
Module: Utility functions for class inheritance checks.
"""


def inherits_from(obj, a_class):
    """
    Check if the object inherits from a specific class.
    Returns True if yes, False otherwise.
    """
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    else:
        return False
