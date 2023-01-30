import pytest
from src import Square

@pytest.fixture()
def additional_square():
    add_square = Square.Square(10)
    return add_square
