#!/usr/bin/python3
"""
This script provides a function to convert a JSON
formatted string to a Python object.
"""


import json


def from_json_string(my_str):
    """
    Convert a JSON formatted string to a Python object.

    Args:
        my_str (str): The JSON formatted string to be converted.

    Returns:
        object: The Python object converted from the JSON string.
    """
    return json.loads(my_str)
