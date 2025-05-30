#!/usr/bin/env python3
"""
Module task_05_dragon
"""


class SwimMixin:
    """
    Mixin class for swimming
    """

    def swim(self):
        """
        Makes the creature swim
        """

        print("The creature swims!")


class FlyMixin:
    """
    Mixin class for flying
    """

    def fly(self):
        """
        Makes the creature fly
        """

        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    Creates a dragon
    """

    def roar(self):
        """
        Makes the dragon roar
        """

        print("The dragon roars!")

    def flame_throwing(self):
        """
        Makes the dragon throw flames
        """

        print("The dragon is throwing flames!")

    def sleep(self):
        """
        Makes the dragon sleep
        """

        print("The dragon is sleeping on its treasure!")

    def sing(self):
        """
        Makes the dragon sing
        """

        print("The dragon is singing Through the Fire and Flames!")
