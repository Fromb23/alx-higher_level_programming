#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Get the number of rows and columns in the matrix
    rows = len(matrix)

    # Ensure there is at least one row before getting the number of columns
    columns = len(matrix[0]) if rows > 0 else 0

    # Create a new matrix with squared values
    new_matrix = [
        [matrix[i][j] ** 2 for j in range(columns)
        for i in range(rows)
    ]

    return new_matrix
