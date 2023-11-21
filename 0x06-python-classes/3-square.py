#!/usr/bin/python3
""" A Square module """


class Square:
    """
    This class represents a sqaure.

    Attributes:
    __size: Private instance attribute representing the sie of the square.

    Methods:
    __init__: Initializes a Sqaure object with an optional size.
    area: Public instance method that returns the current square area
    """

    def __init__(self, size=0):
        """
        Initialisez a Sqaure oblect eith an optional size

        Parameters:
        size (int): Optional size of the squae. Defaults to 0.

        Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be  >= 0")

        self.__size = size

    def area(self):
        """
        Calcualtes and returns the area of the square.

        Returns:
        init: The area of the square.
        """

        return self.__size ** 2
