#!/usr/bin/python3
"""
This module defines a custom list class, MyList,
that extends the built-in list class.
"""


class MyList(list):
    """
    MyList is a custom list class that extends the built-in list class.

    Methods:
        print_sorted(self): Prints the elements of the list in sorted order.
    """
    def print_sorted(self):
        """
        Prints the elements of the list in sorted order.
        """
        print(sorted(self))
