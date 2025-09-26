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
from math import sqrt

@pytest.mark.parametrize("n, x, y, expected", [
    (7, 34, 12, 34),
    (15, 8, 5, 5),
    (1, 100, 200, 200),
    (2, 10, 20, 10),
    (3, 50, 60, 50),
    (4, 70, 80, 80),
    (0, 90, 100, 100),
    (-5, 110, 120, 120),
    (1, 130, 140, 140),
    (2, 150, 160, 10)
])
def test_x_or_y(n, x, y, expected):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    def x_or_y(n, x, y):
        if is_prime(n):
            return x
        else:
            return y

    assert x_or_y(n, x, y) == expected