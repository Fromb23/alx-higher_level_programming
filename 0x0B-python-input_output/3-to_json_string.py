#!/usr/bin/python3
"""
This script provides a function to convert a Python
object to a JSON formatted string.
"""


import json


def to_json_string(my_obj):
    """
    Convert Python object to JSON string.

    Args:
        my_obj: Python object to be converted.

    Returns:
        str: JSON formatted string.
    """
    return json.dumps(my_obj)
