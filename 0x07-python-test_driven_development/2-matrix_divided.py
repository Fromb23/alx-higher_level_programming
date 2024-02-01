#!/usr/bin/python3

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a divisor.

    Parameters:
    - matrix (list of lists): The input matrix (list of lists).
    - div (float or int): The divisor.

    Returns:
    list of lists: A new matrix with elements
                    rounded to 2 decimal places after division.

    Raises:
    TypeError: If the matrix is not a list of lists
    containing only integers or floats.
    TypeError: If each row of the matrix does not have the same size.
    TypeError: If div is not a number (float or int).
    ZeroDivisionError: If division is zero.
    """
    for row in matrix:
        if not all(isinstance(element, (int, float)) for element in row):
            raise TypeError("matrix must be a matrix "
                            "(list of lists) of integers/floats")

    first_row_len = len(matrix[0])

    for row in matrix:
        if len(row) != first_row_len:
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (float, int)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = [
            [round(element / div, 2) for element in row]
            for row in matrix
            ]

    return new_matrix
