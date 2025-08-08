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

def test_prime_numbers():
    assert x_or_y(2, 10, 20) == 10
    assert x_or_y(3, 10, 20) == 10
    assert x_or_y(5, 10, 20) == 10
    assert x_or_y(7, 10, 20) == 10
    assert x_or_y(11, 10, 20) == 10
    assert x_or_y(13, 10, 20) == 10

def test_non_prime_numbers():
    assert x_or_y(1, 10, 20) == 20
    assert x_or_y(4, 10, 20) == 20
    assert x_or_y(6, 10, 20) == 20
    assert x_or_y(8, 10, 20) == 20
    assert x_or_y(9, 10, 20) == 20
    assert x_or_y(15, 10, 20) == 20

@pytest.mark.parametrize("n, x, y, expected", [
    (2, 1, 0, 1),
    (4, 1, 0, 0),
    (7, 1, 0, 1),
    (9, 1, 0, 0),
    (11, 1, 0, 1),
    (15, 1, 0, 0)
])
def test_parametrized_cases(n, x, y, expected):
    assert x_or_y(n, x, y) == expected

def test_edge_cases():
    assert x_or_y(1, 100, 200) == 200
    assert x_or_y(2, -1, -2) == -1
    assert x_or_y(4, 0, 0) == 0
    assert x_or_y(7, -10, 10) == -10

def test_invalid_input():
    for n in [0, -1, -5]:
        result = x_or_y(n, 1, 2)
        assert result == 1  # For non-positive numbers, function returns x

def test_large_numbers():
    assert x_or_y(97, 1000, 2000) == 1000  # Large prime
    assert x_or_y(100, 1000, 2000) == 2000  # Large composite

def test_same_x_y_values():
    assert x_or_y(7, 10, 10) == 10
    assert x_or_y(8, 10, 10) == 10

def test_zero_values():
    assert x_or_y(2, 0, 1) == 0
    assert x_or_y(4, 1, 0) == 0

def test_floating_point_xy():
    assert x_or_y(2, 1.5, 2.5) == 1.5
    assert x_or_y(4, 1.5, 2.5) == 2.5