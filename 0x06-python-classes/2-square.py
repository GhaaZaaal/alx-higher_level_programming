#!/usr/bin/python3
"""Square module."""


class Square:
    """
    This is a class named Square and have a size attribute
    """

    def __init__(self, size=0):
        """
        Initializing The Attributes

        Args:
            1- size => The Size of Any Side of The Square
                Errors:
                    1- If size is not an integer
                    2- If size is less than zero
        """
        try:
            if not isinstance(size, int):
                raise TypeError("size must be an integer")
            if size < 0:
                raise ValueError("size must be >= 0")
        except (TypeError, ValueError) as err:
            print(err)

        self._Square__size = size
