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

def test_x_or_y(n, x, y, expected):
    if isinstance(n, int) and n >= 1:
        if isinstance(expected, type) and issubclass(expected, Exception):
            with pytest.raises(expected):
                x_or_y(n, x, y)
        else:
            assert x_or_y(n, x, y) == expected
    else:
        with pytest.raises(TypeError):
            x_or_y(n, x, y)

@pytest.mark.parametrize("n, x, y, expected", [
    (1, 'a', 'b', 'b'),
    (2, 'a', 'b', 'a'),
    (3, 'a', 'b', 'a'),
    (4, 'a', 'b', 'b'),
    (6, 'a', 'b', 'b'),
    (7, 'a', 'b', 'a'),
    (0, 'a', 'b', TypeError),
    (-1, 'a', 'b', TypeError),
    (1.5, 'a', 'b', TypeError),
    ('a', 'x', 'y', TypeError),
    ([], 'x', 'y', TypeError),
    ({}, 'x', 'y', TypeError),
])
def test_x_or_y(n, x, y, expected):
    test_x_or_y(n, x, y, expected)