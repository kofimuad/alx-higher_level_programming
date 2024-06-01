#!/usr/bin/python3
"""
A function that adds two integers
"""


def add_integer(a, b=98):
    """returns a + b"""
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return (int(a) + int(b))
    else:
        raise TypeError("{:} must be an integer"
                        .format('b' if isinstance(a, (int, float)) else 'a'))
