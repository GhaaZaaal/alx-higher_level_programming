#!/usr/bin/python3
"""
My Module containing the add function
To add two integers
with type int
"""


def add_integer(a, b=98):
    """
    My function that makes an easy addition of a and b
    """
    if a is None or not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if b is None or not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
