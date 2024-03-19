#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for in_matrix in matrix:
        if len(in_matrix) == 0:
            print()
        for i in range(0, len(in_matrix)):
            print(
                "{:d}".format(in_matrix),
                end="\n" if i is len(in_matrix) - 1 else " ")
