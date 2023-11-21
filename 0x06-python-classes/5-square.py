#!/usr/bin/python3
""" A Squre module """


class Square:
    """
    This class represents a square.

    Attributes:
    __size: Private instance attribute representing the size of the square

    Methods:
    __init__: Initializes a Square object wwith an optional size.
    area: Public instance method that returns the current aquare area.
    my_print: Public instnace method thatt prints the sqayre to the stdout.
    """

    def __init__(self, size=0):
        """
        Initializes a Square object with an optional size.

        Parameters:
        size (int): Optional size  of the square. Defaults to 0.

        Raises:
        TypeError: If size is not an integer
        ValueError: If size is less than 0.
        """

        self.size = size

    @property
    def size(self):
        """
        Retrievex the size of the square.

        Returns:
        int: The size of the square.
        """

        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Parameters:
        value (int): The size to set.

        Raises:
        TypeError: If size is not an integer.
        VlaueError: If size is less than 0.
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
        int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square to the stdout using the character #.

        if size is 0, prints an empty line.
        """

        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
