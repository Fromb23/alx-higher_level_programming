#!/usr/bin/python3
"""
Module: 5-square

This module defines a Square class with size verification,
an area method, and a method for printing the square.
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
    if size == 0:
        print()

    def position(self, value):
        """
        Set the position attribute.

        Parameters:
        - value (tuple): A tuple of two positive integers
        representing the position.

        Raises:
        - TypeError: If value is not a tuple of two positive integers.
        """
        if not isinstance(position, tuple) or len(position) != 2 or \
                not isinstance(position[0], int) or not \
                isinstance(position[1], int) \
                or position[0] <= 0 or position[1] <= 0:
            raise TypeError("position must be a \
                    tuple of two positive integers")

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new ClassName instance.

        Parameters:
        - size (int, optional): The size of the square's sides. Defaults to 0.
        - position (tuple, optional): A tuple of two integer
        representing the position. Defaults to (0, 0).
        """
        self.size = size
        self.position = position

    def my_print(self):
        """
        Prints the square using '#' characters.

        If size is equal to 0, print an empty line.
        """
        for i in range(self.position[1]):
            print()
        for i in range(self.size):
            print("_" * self.position[0] + "#" * self.size)
