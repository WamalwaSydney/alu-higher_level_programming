#!/usr/bin/python3
"""
Module for generating Pascal's Triangle.
"""


def pascal_triangle(n):
    """
    Return a list of lists of integers representing the Pascal's triangle of n.

    Args:
        n (int): The number of rows.

    Returns:
        list: A list of lists of integers.
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1]  # First element is always 1
        if triangle:
            prev_row = triangle[-1]
            # Calculate middle elements using previous row
            for j in range(len(prev_row) - 1):
                row.append(prev_row[j] + prev_row[j + 1])
            # Last element is always 1 if row has more than one element
            if i > 0:
                row.append(1)
        triangle.append(row)

    return triangle
