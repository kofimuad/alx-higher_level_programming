#!/usr/bin/python3
# 1-rectangle.py
"""Defines a rectangle class"""


class Rectangle:
    """Represents a rectangle"""

    def __init__(self, width=0, height=0):
        """Initializes a new rectangle.
        Args:
            width(int): the width of the new rectangle
            height(int): the height of the new rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get width of the rectangle"""
        return self.__width # the "__" makes it private

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an int')
        if value < 0:
            raise ValueError('width must be >= 0')

        self.__width = value

    @property
    def height(self):
        """Gets the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('value must be >= 0')
        self.__height = value
