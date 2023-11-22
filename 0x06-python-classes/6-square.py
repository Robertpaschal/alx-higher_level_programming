#!/usr/bin/python3
""" A square module """


class Square:
    """
    This class represents a square.

    Attributes:
        __size: Private instance attribute representing the size of the square.
        __position: Private instance attribute representing \
                the position of the square.

    Methods:
        __init__: Initializes a Square object with optional size and position.
        area: Public instance method that returns the current square area.
        my_print: Public instance method that prints the square to stdout.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a Square object with optional size and position.

        Parameters:
            size (int): Optional size of the square. Defaults to 0.
            position (tuple): Optional position of the square.\
                    Defaults to (0, 0).

        Raises:
            TypeError: If size is not an integer \
                    or position is not a tuple of 2 positive integers.
            ValueError: If size is less than 0 or \
                    position values are not positive integers.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Retrieves the size of the square.

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
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        """
        Retrieves the position of the square.

        Returns:
            tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square.

        Parameters:
            value (tuple): The position to set.

        Raises:
            TypeError: If position is not a tuple of 2 positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple \
                        of 2 positive integers")

        self.__position = value

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square to stdout using the character #.

        If size is 0, prints an empty line.
        Position is used to adjust spacing by using space when position[1] > 0.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
