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

def test_x_or_y_prime_number():
    assert x_or_y(2, 'x', 'y') == 'x'
    assert x_or_y(3, 'x', 'y') == 'x'
    assert x_or_y(5, 'x', 'y') == 'x'
    assert x_or_y(7, 'x', 'y') == 'x'
    assert x_or_y(11, 'x', 'y') == 'x'

def test_x_or_y_composite_number():
    assert x_or_y(4, 'x', 'y') == 'y'
    assert x_or_y(6, 'x', 'y') == 'y'
    assert x_or_y(8, 'x', 'y') == 'y'
    assert x_or_y(9, 'x', 'y') == 'y'
    assert x_or_y(10, 'x', 'y') == 'y'

def test_x_or_y_edge_cases():
    assert x_or_y(1, 'x', 'y') == 'y'
    assert x_or_y(0, 'x', 'y') == 'y'
    assert x_or_y(-1, 'x', 'y') == 'y'

@pytest.mark.parametrize("n,x,y,expected", [
    (2, 'prime', 'composite', 'prime'),
    (3, 'prime', 'composite', 'prime'),
    (4, 'prime', 'composite', 'composite'),
    (5, 'prime', 'composite', 'prime'),
    (6, 'prime', 'composite', 'composite'),
    (7, 'prime', 'composite', 'prime'),
    (8, 'prime', 'composite', 'composite'),
    (9, 'prime', 'composite', 'composite'),
    (11, 'prime', 'composite', 'prime'),
    (1, 'prime', 'composite', 'composite'),
    (0, 'prime', 'composite', 'composite')
])
def test_x_or_y_parametrized(n, x, y, expected):
    assert x_or_y(n, x, y) == expected