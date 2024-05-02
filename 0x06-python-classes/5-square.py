#!/usr/bin/python3
"""Initializes a class Square"""


class Square:
    """Represents a square"""

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
    """Gets the current size of square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        Starts the square

        Args:
            value(int): the size of the square
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """returns area of square"""
        return (self.__size**2)

    def my_print(self):
        """Prints a square to stdout"""
        for i in range(0, self.__size):
            print("#", end="")
            for j in range(self.__size):
                print("")
        if self.__size  == 0:
            print("")

