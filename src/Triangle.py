from src.Figure import Figure


class Triangle(Figure):
    name = "Triangle"

    def __init__(self, a, b, c):
        if (a > b + c) or (b > a + c) or (c > a + b):
            raise ValueError("Impossible to create triangle with such sides! - ", a, b, c)
        self.a = a
        self.b = b
        self.c = c

    @property
    def perimeter(self):
        p = (self.a + self.b + self.c)
        return p

    @property
    def area(self):
        s = ((self.perimeter * (self.perimeter - 2*self.a) * (self.perimeter - 2 * self.b) * (self.perimeter - 2 * self.c)) ** .5) / 4
        print(s)
        return s
