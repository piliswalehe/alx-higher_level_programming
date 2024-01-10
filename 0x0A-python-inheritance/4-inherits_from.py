#!/usr/bin/python3
"""
checks if object is an instance of a class inherited directly/indirectly
"""


def inherits_from(obj, a_class):
    """Compares obj classes
    Args:
        obj (unknown): object whose type is to be checked.
        a_class (str): class criteria to validate.
    Returns:
        True if the object is an instance of a class inherited,
        otherwise False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
