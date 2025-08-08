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
    if n <= 1:
        return y
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return y
    return x

def test_x_or_y_prime_numbers():
    assert x_or_y(2, 34, 12) == 34
    assert x_or_y(3, 8, 5) == 8
    assert x_or_y(5, 100, 200) == 100
    assert x_or_y(7, 34, 12) == 34
    assert x_or_y(11, 50, 60) == 50

def test_x_or_y_non_prime_numbers():
    assert x_or_y(1, 10, 20) == 20
    assert x_or_y(4, 15, 25) == 25
    assert x_or_y(6, 30, 40) == 40
    assert x_or_y(9, 50, 60) == 60
    assert x_or_y(15, 8, 5) == 5

def test_x_or_y_edge_cases():
    assert x_or_y(0, 1, 2) == 2
    assert x_or_y(-7, 10, 20) == 20

@pytest.mark.parametrize("n,x,y,expected", [
    (2, 34, 12, 34),
    (3, 8, 5, 8),
    (1, 10, 20, 20),
    (4, 15, 25, 25),
    (7, 100, 200, 100),
    (11, 50, 60, 50),
    (15, 8, 5, 5)
])
def test_x_or_y_parametrized(n, x, y, expected):
    assert x_or_y(n, x, y) == expected