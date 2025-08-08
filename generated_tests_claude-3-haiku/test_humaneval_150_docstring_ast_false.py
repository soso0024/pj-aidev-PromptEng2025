# Test cases for HumanEval/150
# Generated using Claude API


def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """

    if n == 1:
        return y
    for i in range(2, n):
        if n % i == 0:
            return y
            break
    else:
        return x


# Generated test cases:
import pytest
from your_module import x_or_y

@pytest.mark.parametrize("n, x, y, expected", [
    (7, 34, 12, 34),
    (15, 8, 5, 5),
    (1, 100, 200, 200),
    (2, 10, 20, 10),
    (3, 50, 75, 50),
    (10, 8, 12, 12),
    (-5, 7, 11, 11),
    (0, 3, 6, 6),
    (1000, 42, 24, 42)
])
def test_x_or_y(n, x, y, expected):
    assert x_or_y(n, x, y) == expected

def test_x_or_y_raises_error():
    with pytest.raises(TypeError):
        x_or_y('a', 1, 2)