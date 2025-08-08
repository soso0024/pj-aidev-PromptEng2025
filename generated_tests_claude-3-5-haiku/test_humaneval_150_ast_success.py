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
    assert x_or_y(7, 'x', 'y') == 'x'
    assert x_or_y(11, 'x', 'y') == 'x'
    assert x_or_y(13, 'x', 'y') == 'x'

def test_x_or_y_composite_number():
    assert x_or_y(4, 'x', 'y') == 'y'
    assert x_or_y(6, 'x', 'y') == 'y'
    assert x_or_y(9, 'x', 'y') == 'y'
    assert x_or_y(15, 'x', 'y') == 'y'

def test_x_or_y_special_cases():
    assert x_or_y(1, 'x', 'y') == 'y'
    assert x_or_y(2, 'x', 'y') == 'x'

@pytest.mark.parametrize("n,x,y,expected", [
    (7, 'prime', 'composite', 'prime'),
    (11, 'prime', 'composite', 'prime'),
    (4, 'prime', 'composite', 'composite'),
    (6, 'prime', 'composite', 'composite'),
    (1, 'prime', 'composite', 'composite'),
    (2, 'prime', 'composite', 'prime')
])
def test_x_or_y_parametrized(n, x, y, expected):
    assert x_or_y(n, x, y) == expected
