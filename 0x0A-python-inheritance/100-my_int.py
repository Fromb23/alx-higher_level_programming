#!/usr/bin/python3
"""
Module: my_int

Description:
    MyInt class inherits from int with inverted equality operators.
"""


class MyInt(int):
    def __eq__(self, other):
        """Inverts the == operator."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Inverts the != operator."""
        return super().__eq__(other)
