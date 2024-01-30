#!/usr/bin/python3

def add_integer(a, b=98):
    """
    Adds two integers or floats and returns the result.

    Parameters:
    - a (int or float): The first number.
    - b (int or float, optional): The second number. Default is 98.

    Returns:
    int: The sum of the two numbers, converted to an integer.

    Raises:
    TypeError: If either 'a' or 'b' is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return a + b
