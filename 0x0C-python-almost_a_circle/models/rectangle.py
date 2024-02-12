#!/usr/bin/python3
"""Define the Rectangle class."""

from models.base import Base


class Rectangle(Base):
    """
    Rectangle Class:
    Represents a rectangle object with width, height, position (x, y), and an identifier.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        x (int): The x-coordinate of the top-left corner of the rectangle.
        y (int): The y-coordinate of the top-left corner of the rectangle.
        id (int): The unique identifier of the rectangle.

    Methods:
        __init__: Initializes a new rectangle object.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a new rectangle object with the given parameters.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The x-coordinate of the top-left corner of the rectangle. Default is 0.
            y (int): The y-coordinate of the top-left corner of the rectangle. Default is 0.
            id (int): The unique identifier of the rectangle. Default is None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width
    @width.setter
    def width(self, value):
        """Set the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get the x-coordinate of the top-left corner of the rectangle."""
        return self.__x
    @x.setter
    def x(self, value):
        """Set the x-coordinate of the top-left corner of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get the y-coordinate of the top-left corner of the rectangle."""
        return self.__y
    @y.setter
    def y(self, value):
        """Set the y-coordinate of the top-left corner of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.__width * self__height

    def display(self):
        """Display the rectangle by printing '#' characters."""
        for _ in range(self.__x):
            print('#' * self.__y)

    def __str__(self):
        """Return a string representation of the rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """Update the attributes of the rectangle."""
        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.width = args[1]
        if len(args) > 2:
            self.height = args[2]
        if len(args) > 3:
            self.x = args[3]
        if len(args) > 4:
            self.y = args[4]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return a dictionary representation of the rectangle."""
        return {
                'id' : self.id,
                'width' : self.width,
                'height' : self.height,
                'x' : self.x,
                'y' : self.y
                }
