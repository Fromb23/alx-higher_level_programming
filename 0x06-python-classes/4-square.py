#!/usr/bin/python3
"""
Module: 4-square

This module defines a Square class with size verification and
an area method, using property and setter.
"""


class Square:
    """
    A class representing a square.

    Attributes:
    - _size (int): The size of the square's sides (private).
    """
    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Parameters:
        - size (int, optional): The size of the square's sides. Defaults to 0.
        """
        self._size = size

    @property
    def size(self):
        """
        Getter method for the size attribute.

        Returns:
        - int: The size of the square's sides.
        """
        return self._size

    @size.setter
    def size(self, value):
        """
        Setter method for the size attribute.

        Parameters:
        - value (int): The new size for the square's sides.

        Raises:
        - TypeError: If value is not an integer.
        - ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
        - int: The area of the square.
        """
        return self._size * self._size
