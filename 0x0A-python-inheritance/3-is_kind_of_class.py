#!/usr/bin/python3
"""
checks the kind of class of an obj
"""


def is_kind_of_class(obj, a_class):
    """ returns True if the object is an instance of
    or if the object is an instance of a class inherited,
    otherwise False.
    """

    return isinstance(obj, a_class)
