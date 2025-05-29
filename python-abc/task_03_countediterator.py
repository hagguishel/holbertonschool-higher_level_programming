#!/usr/bin/env python3
"""
Module task_03_countediterator
"""
from abc import ABC, abstractmethod


class CountedIterator:
    """
    This class extends the built-in iterator obtained from the iter function
    """

    def __init__(self, iterator):
        """
        This method initializes two attributes : iterator and counter
        """

        self.iterator = iter(iterator)
        self.counter = 0

    def get_count(self):
        """
        Returns the current value of the counter
        """

        return self.counter

    def __next__(self):
        """
        This method increments a counter each time an item is fetched
        """

        item = next(self.iterator)
        self.counter += 1
        return item
