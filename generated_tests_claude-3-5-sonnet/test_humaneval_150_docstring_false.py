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
    assert x_or_y(2, 10, 20) == 10
    assert x_or_y(3, 10, 20) == 10
    assert x_or_y(5, 10, 20) == 10
    assert x_or_y(7, 10, 20) == 10
    assert x_or_y(11, 10, 20) == 10
    assert x_or_y(23, 10, 20) == 10

def test_x_or_y_non_prime_numbers():
    assert x_or_y(1, 10, 20) == 20
    assert x_or_y(4, 10, 20) == 20
    assert x_or_y(6, 10, 20) == 20
    assert x_or_y(8, 10, 20) == 20
    assert x_or_y(9, 10, 20) == 20
    assert x_or_y(15, 10, 20) == 20

@pytest.mark.parametrize("n, x, y, expected", [
    (7, 34, 12, 34),
    (15, 8, 5, 5),
    (2, 100, 200, 100),
    (4, 100, 200, 200),
    (1, 100, 200, 200),
    (97, 100, 200, 100),
])
def test_x_or_y_parametrized(n, x, y, expected):
    assert x_or_y(n, x, y) == expected

def test_x_or_y_zero_values():
    assert x_or_y(2, 0, 0) == 0
    assert x_or_y(4, 0, 0) == 0

def test_x_or_y_negative_values():
    assert x_or_y(2, -1, -2) == -1
    assert x_or_y(4, -1, -2) == -2
    assert x_or_y(7, -10, -20) == -10

def test_x_or_y_large_numbers():
    assert x_or_y(97, 1000000, 2000000) == 1000000
    assert x_or_y(100, 1000000, 2000000) == 2000000

@pytest.mark.parametrize("n", [-1, 0, -5, -10])
def test_x_or_y_invalid_input(n):
    with pytest.raises(ValueError):
        x_or_y(n, 10, 20)

def test_x_or_y_float_input():
    with pytest.raises(TypeError):
        x_or_y(2.5, 10, 20)
    with pytest.raises(TypeError):
        x_or_y(2, 10.5, 20)
    with pytest.raises(TypeError):
        x_or_y(2, 10, 20.5)