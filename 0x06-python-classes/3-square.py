#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """Presnts a square"""

    def __init__(self, size=0):
        """
        square is initialized

        Arg:
            size: the size of a square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an int")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """returns current area of square"""
        return (self.__size**2)
