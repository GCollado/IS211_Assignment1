# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
The program takes a list of numbers, divide the list elements and returns the
number of elements that are divisible by the divide variable. Test function the
handling of dividing several list and throw a custom exception if error occurs.
"""


def listDivide(numbers, divide=2):
    # Returns total number df divisible elements
    divisible = [number for number in numbers if number%divide == 0]
    return len(divisible)


class ListDivideException(Exception):
    # Custom exception class
    pass


def testListDivide():
    try:
        listDivide([1,2,3,4,5])
        listDivide([2,4,6,8,10])
        listDivide([30,54,63,98,100], divide=10)
        listDivide([])
        listDivide([1,2,3,4,5],1)
    except Exception:
        raise ListDivideException
