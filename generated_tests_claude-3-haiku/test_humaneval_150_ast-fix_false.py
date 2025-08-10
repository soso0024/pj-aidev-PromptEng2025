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
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            assert x_or_y(n, x, y) == expected
    else:
        assert x_or_y(n, x, y) == expected

@pytest.mark.parametrize("n, x, y, expected", [
    (1, 10, 20, 20),
    (2, 10, 20, 10),
    (3, 10, 20, 10),
    (4, 10, 20, 20),
    (6, 10, 20, 20),
    (7, 10, 20, 10),
    (0, 10, 20, ValueError),
    (-1, 10, 20, ValueError),
    (1.5, 10, 20, TypeError),
    (2, "a", 20, TypeError),
    (2, 10, "b", TypeError)
])
def test_x_or_y_parametrized(n, x, y, expected):
    test_x_or_y(n, x, y, expected)

def x_or_y(n, x, y):
    if n == 1:
        return y
    for i in range(2, n):
        if n % i == 0:
            return y
            break
    else:
        return x