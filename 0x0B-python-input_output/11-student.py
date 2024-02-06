#!/usr/bin/python3
"""
Defines a Student class with attributes first_name, last_name, and age.
"""


class Student:
    """
    Represents a student with attributes first name, last name, and age.
    """
    def __init__(self, first_name, last_name, age):
        """
        Initialize a Student object with provided first name,
        last name, and age.

        Parameters:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Convert the Student object to a JSON-compatible dictionary.

        If attrs is a list of strings, return a dictionary
        with only those attributes,
        otherwise return a dictionary with all attributes.

        Parameters:
        attrs (list of str, optional): Attributes to include in the dictionary.

        Returns:
        dict: A dictionary representing the attributes of the Student object.
        """
        if isinstance(attrs, list) and all(isinstance(attr, str) for attr in attrs):
                return {attr: getattr(self, attr) for attr in attrs if attr in self.__dict__}
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """
        Replace all attributes of the Student instance with
        the values from the provided dictionary.

        Parameters:
        json (dict): A dictionary containing attribute names and values.
        """
        for key, value in json.items():
            setattr(self, key, value)
