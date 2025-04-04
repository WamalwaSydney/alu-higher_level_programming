#!/usr/bin/python3
"""Module to divide all elements of a matrix."""

def matrix_divided(matrix, div):
    """Divides all elements of a matrix by a divisor.
    
    Args:
        matrix (list of lists): Matrix of integers/floats.
        div (int/float): Divisor.
    
    Raises:
        TypeError: If matrix is invalid or div is not a number.
        ZeroDivisionError: If div is zero.
    
    Returns:
        list of lists: New matrix with elements divided by div.
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    row_len = len(matrix[0]) if matrix else 0
    for row in matrix:
        if len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")
        if not all(isinstance(e, (int, float)) for e in row):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(e / div, 2) for e in row] for row in matrix]
