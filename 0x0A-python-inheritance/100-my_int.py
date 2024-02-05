#!/usr/bin/python3
class MyInt(int):
    """
    MyInt class inherits from int with inverted equality operators.

    Methods:
        __eq__(self, other): Inverts the == operator.
        __ne__(self, other): Inverts the != operator.
    """
    def __eq__(self, other):
        """
        Inverts the == operator.

        Args:
            other: The object to compare against.

        Returns:
            bool: True if not equal, False if equal.
        """
        if isinstance(other, MyInt):
            return not super().__eq__(other)
        else:
            return False

    def __ne__(self, other):
        """
        Inverts the != operator.

        Args:
            other: The object to compare against.

        Returns:
            bool: True if not equal, False if equal.
        """
        if isinstance(other, MyInt):
            return not super().__ne__(other)
        else:
            return False
