#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """A combination of liscomp, map and lambda"""
    return ([list(map(lambda x: x * x, row))for row in matrix])
