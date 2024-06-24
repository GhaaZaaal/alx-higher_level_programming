#!/usr/bin/python3
"""Square module."""


class Square:
    """
    This is a class named Square and have a size attribute
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializing The Attributes

        Args:
            1- size => The Size of Any Side of The Square
        """
        self._Square__size = size
        if not isinstance(position, tuple) or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif isinstance(position, tuple):
            for num in position:
                if not isinstance(num, int) or num < 0:
                    raise TypeError(
                        "position must be a tuple of 2 \
positive integers"
                    )
        self._Square__position = position

    @property
    def position(self):
        """
        Getter For Position Attribute
        """
        return self._Square__position

    @position.setter
    def position(self, value):
        """
        Setter For Position To Value

        Args:
            1- value => The Position Given of Any Side of The Square
                Errors:
                    1- If Position is not an integer
                    2- If Position is less than zero
        """

        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif isinstance(value, tuple):
            for num in value:
                if not isinstance(num, int) or num <= 0:
                    raise TypeError(
                        "position must be a tuple of 2 \
                                    positive integers"
                    )
        else:
            self._Square__position = value

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
        if self._Square__position:
            rowSize = self._Square__size + self._Square__position[0]
            # print("Setting position to:", self._Square__position)
        else:
            rowSize = self._Square__size

        if self._Square__size == 0:
            print()

        for i in range(self._Square__size + self._Square__position[1]):
            if (i + 1) >= self._Square__position[1]:
                print("", end="\n")
                continue
            for x in range(rowSize):
                if self._Square__position:
                    if (x + 1) <= self._Square__position[0]:
                        print(" ", end="")
                    else:
                        print("#", end="")
                else:
                    print("#", end="")

            print()
