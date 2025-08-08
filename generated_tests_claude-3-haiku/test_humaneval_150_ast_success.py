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

def x_or_y(n, x, y):
    if n <= 0:
        raise ValueError
    if n == 1:
        return y
    for i in range(2, n):
        if n % i == 0:
            return y
    else:
        return x

def test_x_or_y_n_is_1():
    assert x_or_y(1, 'x', 'y') == 'y'

def test_x_or_y_n_is_divisible():
    assert x_or_y(6, 'x', 'y') == 'y'

def test_x_or_y_n_is_prime():
    assert x_or_y(7, 'x', 'y') == 'x'

@pytest.mark.parametrize("n, x, y, expected", [
    (1, 'x', 'y', 'y'),
    (2, 'x', 'y', 'x'),
    (3, 'x', 'y', 'x'),
    (4, 'x', 'y', 'y'),
    (5, 'x', 'y', 'x'),
    (6, 'x', 'y', 'y'),
    (7, 'x', 'y', 'x'),
    (8, 'x', 'y', 'y'),
    (9, 'x', 'y', 'y'),
    (10, 'x', 'y', 'y')
])
def test_x_or_y_parametrized(n, x, y, expected):
    assert x_or_y(n, x, y) == expected

def test_x_or_y_zero_n():
    with pytest.raises(ValueError):
        x_or_y(0, 'x', 'y')

def test_x_or_y_negative_n():
    with pytest.raises(ValueError):
        x_or_y(-1, 'x', 'y')