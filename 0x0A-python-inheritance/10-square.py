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

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            str: A string representation of the area.
        """
        _area = self.__width * self.__height
        print("[Rectangle] {}/{}".format(self.__width, self.__height))
        return str(_area)


class Square(Rectangle):
    """
    Square class that inherits from Rectangle.

    Attributes:
        __size (int): Private size of the square.
    """
    def __init__(self, size):
        """
        Initializes a Square instance with size.

        Args:
            size (int): Size of the square.
        """
        self.__size
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
