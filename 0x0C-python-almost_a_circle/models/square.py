#!/usr/bin/python3

from models.rectangle import Rectangle
"""
Square Module:
This module defines the Square class, which represents a square object.
"""


class Square(Rectangle):
    """
    Square Class:
    Represents a square object, which is a special case of a
    rectangle where all sides are equal in length.

    Attributes:
        size (int): The size of the square, which determines both width and height.
        x (int): The x-coordinate of the top-left corner of the square.
        y (int): The y-coordinate of the top-left corner of the square.
        id (int): The unique identifier of the square.

    Methods:
        __init__: Initializes a new square object.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a new square object with the given parameters.

        Args:
            size (int): The size of the square, which determines both width and height.
            x (int): The x-coordinate of the top-left corner of the square. Default is 0.
            y (int): The y-coordinate of the top-left corner of the square. Default is 0.
            id (int): The unique identifier of the square. Default is None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return a string representation of the square."""
        return "[square] (<{}>) <{}>/<{}> - <{}>".format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Get the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the square."""
        if not isinstance(value, int):
            raise TypeError("[TypeError] width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the attributes of the square."""
        if len(args) > 0:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return a dictionary representation of the square."""
        return {
                'id' : self.id,
                'size' : self.size,
                'x' : self.x,
                'y' : self.y
                }
