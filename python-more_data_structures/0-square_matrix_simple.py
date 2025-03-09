#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """
    Computes the square value of all integers of a matrix.
    Args:
        matrix: a 2 dimensional array
    Returns:
        A new matrix of same size with squared values
    """
    return [[x ** 2 for x in row] for row in matrix]
