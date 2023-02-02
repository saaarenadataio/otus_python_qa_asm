class Figure:
    name = "Figure"

    def add_area(self, b):
        if not isinstance(b, Figure):
            raise ValueError(b, "is not Figure!")
        return self.area + b.area
