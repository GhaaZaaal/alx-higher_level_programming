#!/usr/bin/python3
"""
My Module containing the div function
To divide every element in the matrix by the div parameter
returning a new matrix with every element in list in it equal to
the division of the the old element in list in the matrix by the div param
"""


def matrix_divided(matrix, div):
    """
    Doc
    """
    if (
        matrix is None
        or not isinstance(matrix, list)
        or not all(isinstance(row, list) for row in matrix)
    ):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
            )
    listInListLen = len(matrix[0])

    for largeList in matrix:
        if len(largeList) != listInListLen:
            raise TypeError("Each row of the matrix must have the same size")
        for item in largeList:
            if (
                item is None
                or not isinstance(item, (int, float))
                or item == float("inf")
            ):
                raise TypeError(
                    "matrix must be a matrix \
(list of lists) of integers/floats"
                )

    if div is None or not isinstance(div, (int, float)) or div == float('inf'):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [
        [round(element / div, 2) for element in row] for row in matrix
        ]
    return new_matrix
