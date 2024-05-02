#!/usr/bin/python3

class Square:
    def __init__(self, size=0):
        """ Initialize a square. Size: Size of the square"""
        if not isinstance(size, int):
            raise TypeError("size must be an interger")
        else if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
