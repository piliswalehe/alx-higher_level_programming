#!/usr/bin/python3
"""
Module that adds two integers
"""


def add_integer(a, b=98):
    """adds two integers
        Args:
            a: the first integer or float
            b: the second integer or float

        Raises:
            TypeError: if a, b are not integers
        Return:
            Sum of two integers
    """
    if not isinstance (a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance (b, (int, float)):
        raise TypeError("b must be an integer")
    
    a = int(a)
    b = int(b)

    return a + b
