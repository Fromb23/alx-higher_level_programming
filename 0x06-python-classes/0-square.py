#!/usr/bin/python3
"""
This module defines a Square class that represents a square
and provides methods for calculating its area.
"""


class Square:
    """
    A class representing a square.

    Attributes:
    - length (int): The length of the square's sides.
    """
    def __init__(self, length=None):
        """
        Initializes a new Square instance.

        Parameters:
        - length (int, optional): The length of the
        square's sides. Defaults to None.
        """
        self.length = length

    def area(self):
        """
        Calculates the area of the square.

        Returns:
        - int: The area of the square.

        Raises:
        - ValueError: If the length is not provided
        or is not a positive number.
        """
        return self.length * self.length
