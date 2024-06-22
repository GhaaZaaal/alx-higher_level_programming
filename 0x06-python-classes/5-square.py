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
        """
        self._Square__size = size

    @property
    def size(self):
        """
        Getter For Size Attribute
        """
        return self._Square__size

    @size.setter
    def size(self, value):
        """
        Setter For Size To Value

        Args:
            1- value => The Size Given of Any Side of The Square
                Errors:
                    1- If size is not an integer
                    2- If size is less than zero
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self._Square__size = value

    def area(self):
        """
        Method to Calculate The Area of The Square
        """
        return self._Square__size**2

    def my_print(self):
        """
        Method To Print A Cute Square of "#"
        """
        if self._Square__size == 0:
            print()
        for i in range(self._Square__size):
            for x in range(self._Square__size):
                print("#", end="")
            print()
