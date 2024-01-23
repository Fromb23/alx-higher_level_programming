#!/usr/bin/python3
"""
Module: 1-square

This module defines a Square class with a private size attribute.
"""


class Square:
    """
    A class representing a square.

    Attributes:
    - __size (int): The size of the square's sides (private).
    """
    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Parameters:
        - size (int, optional): The size of the square's sides. Defaults to 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
