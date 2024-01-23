#!/usr/bin/python3
"""
Module: 0-square

This module defines a simple Square class.
"""


class Square:
    """
    A class representing a square.

    Attributes:
    - _size (int): The size of the square's sides.
    """
    def __init__(self, size):
        """
        Initializes a new Square instance.

        Parameters:
        - size (int): The size of the square's sides.
        """
        self.__size = size
