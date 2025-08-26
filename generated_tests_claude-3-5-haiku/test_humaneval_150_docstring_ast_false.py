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

def test_x_or_y_prime_numbers():
    assert x_or_y(7, 34, 12) == 34
    assert x_or_y(11, 100, 200) == 100
    assert x_or_y(13, 50, 60) == 50

def test_x_or_y_non_prime_numbers():
    assert x_or_y(15, 8, 5) == 5
    assert x_or_y(24, 100, 200) == 200
    assert x_or_y(9, 50, 60) == 60

def test_x_or_y_edge_cases():
    assert x_or_y(1, 10, 20) == 20
    assert x_or_y(2, 30, 40) == 30
    assert x_or_y(0, 50, 60) == 60

@pytest.mark.parametrize("n,x,y,expected", [
    (7, 34, 12, 34),
    (11, 100, 200, 100),
    (15, 8, 5, 5),
    (24, 100, 200, 200),
    (1, 10, 20, 20),
    (2, 30, 40, 30),
    (0, 50, 60, 60)
])
def test_x_or_y_parametrized(n, x, y, expected):
    assert x_or_y(n, x, y) == expected