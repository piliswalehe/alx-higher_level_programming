#!/usr/bin/python3
"""
module is for is_same_class
"""


def is_same_class(obj, a_class):
    """ if the object is exactly an instance of the specified class
    Args:
        obj (unknown): object whose type is to be checked.
        a_class (str): class criteria to validate.
    """

    if type(obj) == a_class:
        return True
    return False
