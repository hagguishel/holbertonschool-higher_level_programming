#!/usr/bin/python3

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius * self.radius * math.pi

    def perimeter(self):
        return math.pi * self.radius * 2


class Rectangle(Shape):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return (self.height + self.width) * 2


def shape_info(obj):
    area = obj.area()

    perimeter = obj.perimeter()

    print(f"Area: {area}")
    print(f"Perimeter: {perimeter}")
