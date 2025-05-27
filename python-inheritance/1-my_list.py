#!/usr/bin/python3
"""
Module for MyList class.
Defines MyList, a subclass of list with a method
to display its elements in ascending order.
"""


class MyList(list):
    """List subclass with a print_sorted method."""

    def print_sorted(self):
        """
        Display the list elements in ascending order.
        """
        print(sorted(self))
