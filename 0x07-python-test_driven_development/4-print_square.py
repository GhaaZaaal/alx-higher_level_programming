#!/usr/bin/python3
"""Square module."""


def print_square(size):
    """Doc"""
    if not isinstance(size, (int, float)):
        raise TypeError("size must be an integer")
    elif isinstance(size, float):
        if size < 0:
            raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    for i in range(int(size)):
        for x in range(int(size)):
            print("#", end="")
        print()
