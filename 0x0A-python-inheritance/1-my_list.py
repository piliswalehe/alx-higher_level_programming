#!/usr/bin/python3
"""
Contains definiton for the class MyList that inherits from list.
"""


class Mylist(list):
    """defines a new class called MyList that inherits from a list class
    """
    def print_sorted(self):
        """print elements in a list in order
        """
        sorted_list = sorted(self)
        print(sorted_list)
