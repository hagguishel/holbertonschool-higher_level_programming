#!/usr/bin/env python3
"""
Module task_04_flyingfish
"""


class Fish:
    """
    This class creates a fish
    """

    def swim(self):
        """
        Makes the fish swim
        """

        print("The fish is swimming")

    def habitat(self):
        """
        Prints the habitat of the fish
        """

        print("The fish lives in water")


class Bird:
    """
    This class creates a bird
    """

    def fly(self):
        """
        Makes the bird fly
        """

        print("The bird is flying")

    def habitat(self):
        """
        Prints the habitat of the bird
        """

        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    This class creates a flying fish
    """

    def fly(self):
        """
        Makes the flying fish fly
        """

        print("The flying fish is soaring!")

    def swim(self):
        """
        Makes the flying fish swim
        """

        print("The flying fish is swimming!")

    def habitat(self):
        """
        Prints the habitat of the flying fish
        """

        print("The flying fish lives both in water and the sky!")
