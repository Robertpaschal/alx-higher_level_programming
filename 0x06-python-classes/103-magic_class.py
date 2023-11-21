#!/usr/bin/python3
""" A byte module """


import math

class MagicClass:
    """
    This class represents a MagicClass that performs operations based on a radius.

    Attributes:
        __radius: Private instance attribute representing the radius of the MagicClass.

    Methods:
        __init__: Initializes a MagicClass object with a radius.
        area: Calculates and returns the area of the circle.
        circumference: Calculates and returns the circumference of the circle.
    """

    def __init__(self, radius=0):
        """
        Initializes a MagicClass object with a radius.

        Parameters:
            radius (float or int): The radius of the MagicClass. Defaults to 0.

        Raises:
            TypeError: If radius is not a number (float or integer).
            ValueError: If radius is less than 0.
        """
        self.radius = radius

    @property
    def radius(self):
        """
        Retrieves the radius of the MagicClass.

        Returns:
            float or int: The radius of the MagicClass.
        """
        return self.__radius

    @radius.setter
    def radius(self, value):
        """
        Sets the radius of the MagicClass.

        Parameters:
            value (float or int): The radius to set.

        Raises:
            TypeError: If radius is not a number (float or integer).
            ValueError: If radius is less than 0.
        """
        if not isinstance(value, (float, int)):
            raise TypeError('radius must be a number')

        if value < 0:
            raise ValueError('radius must be >= 0')

        self.__radius = value

    def area(self):
        """
        Calculates and returns the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return math.pi * self.__radius**2

    def circumference(self):
        """
        Calculates and returns the circumference of the circle.

        Returns:
            float: The circumference of the circle.
        """
        return 2 * math.pi * self.__radius
