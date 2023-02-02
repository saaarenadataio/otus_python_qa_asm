from src.Figure import Figure


class Square(Figure):
    name = "Square"

    def __init__(self, a):
        self.a = a

    @property
    def area(self):
        s = self.a ** 2
        return s

    @property
    def perimeter(self):
        p = 4 * self.a
        return p
