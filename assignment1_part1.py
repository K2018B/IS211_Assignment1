#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""IS211 Assignment Part 1"""

def listDivide(numbers, divide=2):
    """Dividing List

    Args:
        numbers(list): list of integers
        divide=2 (int): Arg to divide numbers by
    Returns:
        int: The number of elements divisible by the divisor
    Examles:
        >>> listDivide([1,3,7,9])
        0
        >>> listDivide([1,1,2,3,5,8,13], 1)
        7
    """
    divcount = 0
    for item in numbers:
        if item % divide is 0:
            divcount += 1
    return divcount

class ListDivideException(Exception):
    """Custom exception Class"""
    pass

def testListDivide():
    """A function to test ListDivide."""
    if listDivide([1, 2, 3, 4, 5]) != 2:
        raise ListDivideException
    elif listDivide([2, 4, 6, 8, 10]) != 5:
        raise ListDivideException
    elif listDivide([30, 54, 63, 98, 100], 10) != 2:
        raise ListDivideException
    elif listDivide([]) != 0:
        raise ListDivideException
    elif listDivide([1, 2, 3, 4, 5], 1) != 5:
        raise ListDivideException

if __name__ == "__main__":
    testListDivide()
