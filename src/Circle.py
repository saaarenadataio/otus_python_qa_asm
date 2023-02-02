from src.Figure import Figure
from math import pi


class Circle(Figure):
    name = "Circle"

    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        s = pi * self.radius ** 2
        return s

    @property
    def perimeter(self):
        p = 2 * pi * self.radius
        return p
