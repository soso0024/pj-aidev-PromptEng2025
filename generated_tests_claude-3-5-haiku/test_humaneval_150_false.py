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
    for i in range(2, int(abs(n)**0.5) + 1):
        if n % i == 0:
            return y
    return x

def test_x_or_y_prime_number():
    assert x_or_y(7, 10, 20) == 10
    assert x_or_y(11, 15, 25) == 15
    assert x_or_y(13, 30, 40) == 30

def test_x_or_y_composite_number():
    assert x_or_y(4, 10, 20) == 20
    assert x_or_y(6, 15, 25) == 25
    assert x_or_y(9, 30, 40) == 40

def test_x_or_y_special_cases():
    assert x_or_y(1, 10, 20) == 20
    assert x_or_y(2, 15, 25) == 15

@pytest.mark.parametrize("n,x,y,expected", [
    (7, 10, 20, 10),
    (11, 15, 25, 15),
    (4, 10, 20, 20),
    (1, 10, 20, 20),
    (2, 15, 25, 15),
    (9, 30, 40, 40)
])
def test_x_or_y_parametrized(n, x, y, expected):
    assert x_or_y(n, x, y) == expected

def test_x_or_y_large_numbers():
    assert x_or_y(97, 100, 200) == 100
    assert x_or_y(100, 50, 75) == 75

def test_x_or_y_negative_inputs():
    assert x_or_y(-7, 10, 20) == 20
    assert x_or_y(7, -10, 20) == 20

def test_x_or_y_zero_input():
    assert x_or_y(0, 10, 20) == 20