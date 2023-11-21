#!/usr/bin/python3
""" A square module """


class Square:
    """
    This class represents a square.

    Attributes:
        __size: Private instance attribute representing the size of the square.

    Methods:
        __init__: Initializes a Square object with size.
        size: Property and setter method for retrieving and setting the size of the square.
        area: Public instance method that returns the current square area.
        __eq__: Magic method for equality comparison.
        __ne__: Magic method for inequality comparison.
        __lt__: Magic method for less than comparison.
        __le__: Magic method for less than or equal to comparison.
        __gt__: Magic method for greater than comparison.
        __ge__: Magic method for greater than or equal to comparison.
    """

    def __init__(self, size=0):
        """
        Initializes a Square object with size.

        Parameters:
            size (float or int): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not a number (float or integer).
            ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
            float or int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Parameters:
            value (float or int): The size to set.

        Raises:
            TypeError: If size is not a number (float or integer).
            ValueError: If size is less than 0.
        """
        if not isinstance(value, (float, int)):
            raise TypeError("size must be a number (float or integer)")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            float or int: The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        Magic method for equality comparison.

        Parameters:
            other (Square): The square to compare.

        Returns:
            bool: True if equal, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() == other.area()
        return False

    def __ne__(self, other):
        """
        Magic method for inequality comparison.

        Parameters:
            other (Square): The square to compare.

        Returns:
            bool: True if not equal, False otherwise.
        """
        return not self.__eq__(other)

    def __lt__(self, other):
        """
        Magic method for less than comparison.

        Parameters:
            other (Square): The square to compare.

        Returns:
            bool: True if less than, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() < other.area()
        return NotImplemented

    def __le__(self, other):
        """
        Magic method for less than or equal to comparison.

        Parameters:
            other (Square): The square to compare.

        Returns:
            bool: True if less than or equal to, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() <= other.area()
        return NotImplemented

    def __gt__(self, other):
        """
        Magic method for greater than comparison.

        Parameters:
            other (Square): The square to compare.

        Returns:
            bool: True if greater than, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() > other.area()
        return NotImplemented

    def __ge__(self, other):
        """
        Magic method for greater than or equal to comparison.

        Parameters:
            other (Square): The square to compare.

        Returns:
            bool: True if greater than or equal to, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() >= other.area()
        return NotImplemented
