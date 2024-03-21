#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda inMat: list(map(lambda e: e**2, inMat)), matrix))
