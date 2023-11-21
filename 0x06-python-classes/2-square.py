#!/usr/bin/python3
""" A square mode"""


class Square:
    """
    This class represents a square.

    Attributes:
    __size: Private instance attribute representing the size of the sqaure

    Methods:
    __init__: Initializes a Square object with an optional size
    """

    def __init__(self, size=0):
        """

        Initializes a Square object with an optional size.

        Parameters:
        size (int): Optional size of the square. Defaults to 0

        Raises:
        TypeError: If size is not an integer
        ValueError: If size is less than 0
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
