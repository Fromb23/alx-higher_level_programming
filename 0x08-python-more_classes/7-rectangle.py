#!/usr/bin/python3

"""
This module defines a simple Rectangle class.

Examples:
    >>> Rectangle = __import__('0-rectangle').Rectangle

    >>> my_rectangle = Rectangle()
    >>> print(type(my_rectangle))
    <class '0-rectangle.Rectangle'>

    >>> print(my_rectangle.__dict__)
    {}
"""


class Rectangle:
    """
    Rectangle class represents a rectangle with width and height.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.

    Methods:
        width (property): Get the width of the rectangle.
        width (setter method): Set the width of the rectangle.
        height (property): Get the height of the rectangle.
        height (setter method): Set the height of the rectangle.
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initialize a Rectangle instance.

        Args:
            width (int): The width of the rectangle. Default is 0.
            height (int): The height of the rectangle. Default is 0.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Get the width of the rectangle.

        Returns:
            int: The width of the rectangle.

        >>> rectangle = Rectangle(width=5, height=10)
        >>> rectangle.width
        5
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.

        Args:
            value (int): The new width value.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.

        >>> rectangle = Rectangle()
        >>> rectangle.width = 7
        >>> rectangle.width
        7
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Get the height of the rectangle.

        Returns:
            int: The height of the rectangle.

        >>> rectangle = Rectangle(width=5, height=10)
        >>> rectangle.height
        10
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.

        Args:
            value (int): The new height value.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.

        >>> rectangle = Rectangle()
        >>> rectangle.height = 12
        >>> rectangle.height
        12
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculate and return the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculate and return the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Return a string representation of the rectangle.

        Returns:
            str: A string representation of the rectangle using '#' characters.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            rectangle_rows = [
                    str(self.print_symbol) * self.__width
                    for _ in range(self.__height)
                    ]
            return "\n".join(rectangle_rows)

    def __repr__(self):
        """
        Return a string representation of the rectangle suitable for debugging.

        Returns:
            str: A string representing the Rectangle
            instance with its width and height.
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        Destructor method for the Rectangle class.

        Prints a farewell message when an instance of the class is deleted.

        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
