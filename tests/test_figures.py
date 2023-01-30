from src import Circle, Square, Triangle, Rectangle

def test_triangle(additional_square):
    triangle = Triangle.Triangle(3,4,5)
    assert triangle.name == "Triangle", "Wrong Triangle name"
    assert triangle.area == 6, "Wrong Triangle area calculation"
    assert triangle.perimeter == 12, "Wrong Triangle perimeter calculation"
    assert triangle.add_area(additional_square) == 106, "Wrong area addition to Triangle"


def test_rectangle(additional_square):
    rectangle = Rectangle.Rectangle(3,4)
    assert rectangle.name == "Rectangle", "Wrong Rectangle name"
    assert rectangle.area == 12, "Wrong Rectangle area calculation"
    assert rectangle.perimeter == 14, "Wrong Rectangle perimeter calculation"
    assert rectangle.add_area(additional_square) == 112, "Wrong area addition to Rectangle"


def test_square(additional_square):
    square = Square.Square(5)
    assert square.name == "Square", "Wrong Square name"
    assert square.area == 25, "Wrong Square area calculation"
    assert square.perimeter == 20, "Wrong Square perimeter calculation"
    assert square.add_area(additional_square) == 125, "Wrong area addition to Square"


def test_circle(additional_square):
    circle = Circle.Circle(5)
    assert circle.name == "Circle", "Wrong circle name"
    assert circle.area == 78.53981633974483, "Wrong Circle area calculation"
    assert circle.perimeter == 31.41592653589793, "Wrong Circle perimeter calculation"
    assert circle.add_area(additional_square) == 178.53981633974485, "Wrong area addition to Circle"
