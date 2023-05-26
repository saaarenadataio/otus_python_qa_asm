from src.Figure import Figure


class Rectangle(Figure):
    name = "Rectangle"

    def __init__(self, a, b):
        self.a = a
        self.b = b

    @property
    def area(self):
        s = self.a * self.b
        return s

    @property
    def perimeter(self):
        p = 2 * (self.a + self.b)
        return p
