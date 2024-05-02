#!/usr/bin/python3
"""Implementing a class Square"""


class Square:
    """Represents a square"""
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """Gets the current size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        Initializes a square

        Args:
            value(int): placeholder for the size of the square
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of square"""
        return (self.__size**2)
