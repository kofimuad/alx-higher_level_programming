#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """Use of list comprehension"""
    [print("{}: {}".format(k, a_dictionary[k]))for k in sorted(a_dictionary)]
