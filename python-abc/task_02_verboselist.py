#!/usr/bin/env python3
"""
Module task_02_verboselist
"""


class VerboseList(list):
    """
    This class extends the Python list class
    """

    def append(self, item):
        """
        This method appends an item to the list
        """

        print("Added [{}] to the list".format(item))
        super().append(item)

    def extend(self, item):
        """
        This method extends an item to the list
        """

        print("Extended the list with [{}] items.".format(len(item)))
        super().extend(item)

    def remove(self, item):
        """
        This method removes an item to the list
        """

        if item not in self:
            raise ValueError("This item doesn't exist in the list")
        print("Removed [{}] from the list".format(item))
        super().remove(item)

    def pop(self, item=-1):
        """
        This method pops an item to the list
        """

        print("Popped [{}] from the list.".format(self[item]))
        return super().pop(item)
