#!/usr/bin/python3

def uniq_add(my_list=[]):
    uniq_element = set(my_list)  # use set to get unique elements
    sum = 0
    for element in uniq_element:
        sum += element
    return (sum)
