#!/usr/bin/python3
"""
Definition of a function lookup
"""


def lookup(obj):
    """ Returns a list of attributes and methods of an given object
     Args:
        obj (any): object whose attributes and methods are to be returned
    """
    return (dir(obj))
