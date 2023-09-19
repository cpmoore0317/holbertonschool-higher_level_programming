#!/usr/bin/python3

def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a divisor and round the result to 2 decimal places.

    Args:
        matrix (list of lists): The matrix to be divided, containing integers or floats.
        div (int or float): The divisor.

    Returns:
        list of lists: A new matrix with elements rounded to 2 decimal places after division.

    Raises:
        TypeError: If the matrix is not a list of lists of integers/floats,
                   or if each row of the matrix does not have the same size,
                   or if the divisor is not a number (integer or float).
        ZeroDivisionError: If the divisor is equal to 0.

    Example:
        >>> matrix = [
        ...     [1, 2, 3],
        ...     [4, 5, 6]
        ... ]
        >>> matrix_divided(matrix, 3)
        [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    # Check if all rows have the same size
    if len(set(len(row) for row in matrix)) != 1:
        raise TypeError("Each row of the matrix must have the same size")
    
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    return [[round(element / div, 2) for element in row] for row in matrix]
