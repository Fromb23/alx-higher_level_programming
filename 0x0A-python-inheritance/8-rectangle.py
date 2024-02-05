#!/usr/bin/python3
"""
Class: BaseGeometry - Represents the base geometry class.
"""


class BaseGeometry:
    """
    Placeholder for the base geometry class.

    Methods:
        area(self) - Raises an exception indicating
        that area() is not implemented.
    """
    def area(self):
        """
        Raises an exception indicating that area() is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the value for being an integer and greater than 0.

        Args:
            name (str): The name of the value.
            value: The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    Rectangle class that inherits from BaseGeometry.

    Attributes:
        __width (int): Private width of the rectangle.
        __height (int): Private height of the rectangle.
    """

    def __init__(self, width, height):
        """
        Initializes a Rectangle instance with width and height.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
