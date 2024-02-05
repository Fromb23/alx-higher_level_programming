#!/usr/bin/python3
def lookup(obj):
    obj_list = dir(obj)
    """
    Returns a list of attributes and methods of the given object.

    Args:
        obj: The object for which attributes and methods will be retrieved.

    Returns:
        list: A list of strings representing the attributes and
        methods of the object.
    """

    return obj_list
