#!/usr/bin/python3

import json
import os
"""Define the Base class."""


class Base:
    """Base class for other classes."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a Base instance.

        Args:
            id (int): The identifier for the instance.
            If None, a new identifier will be generated.

        """
        if id is not None:
            self.id = id
        else:
            Base. __nb_objects += 1
            self.id = Base. __nb_objects

    def to_json_string(list_dictionaries):
        """Convert a list of dictionaries to a JSON string.

        Args:
            list_dictionaries (list): List of dictionaries to be converted.

        Returns:
            str: JSON representation of the list of dictionaries.
        """
        if not list_dictionaries:
            return  "[]"
        else:
            dictionaries = [obj.to_dictionary() for obj in list_dictionaries]
            return json.dumps(dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save a list of objects to a JSON file.

        Args:
            cls: The class.
            list_objs (list): List of objects to be saved to the file.
        """
        if list_objs is None:
            list_objs = []
        new_file = cls.__name__ + ".json"
        json_string = Base.to_json_string(list_objs)
        with open(new_file, 'w') as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """Load a list of objects from a JSON string.

        Args:
            json_string (str): JSON string representing a list of dictionaries.

        Returns:
            list: List of objects loaded from the JSON string.
        """
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Create a new instance using a dictionary of attributes.

        Args:
            cls: The class.
            **dictionary: Dictionary of attributes to initialize the instance with.

        Returns:
            Base: A new instance of the class initialized with the provided attributes.
        """
        dummy_instance = cls(1, 1)
        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """Load instances from a JSON file.

        Args:
            cls: The class.

        Returns:
            list: A list of instances loaded from the JSON file.
        """
        filename = cls.__name__ + ".json"
        if not os.path.exists(filename):
            return []

        with open(filename, 'r') as file:
            file_contents = file.read()

        list_of_dicts = Base.from_json_string(file_contents)

        instances = []
        for item in list_of_dicts:
            instance = cls.create(**item)
            instances.append(instance)

        return instances
