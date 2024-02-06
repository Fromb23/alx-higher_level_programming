#!/usr/bin/python3
import sys
import importlib
save_to_json_file, load_from_json_file = (
    importlib.import_module("5-save_to_json_file").save_to_json_file,
    importlib.import_module("6-load_from_json_file").load_from_json_file
)

"""
Add command line arguments to a JSON file list.

Load existing list from 'add_item.json', if present.
Append command line arguments to the list.
Save the updated list back to 'add_item.json'.
"""


def path_args():
    """
    Add command line arguments to a list stored in a JSON file.

    If the file 'add_item.json' exists, load its contents into a list.
    Otherwise, initialize an empty list.
    Append command line arguments to the list.
    Save the updated list to 'add_item.json'.
    """
    try:
        existing_list = load_from_json_file('add_item.json')
    except FileNotFoundError:
        existing_list = []

    existing_list.extend(sys.argv[1:])
    save_to_json_file(existing_list, 'add_item.json')
