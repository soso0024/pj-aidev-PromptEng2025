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

def test_x_or_y_basic():
    assert x_or_y(1, 10, 20) == 20
    assert x_or_y(2, 10, 20) == 10
    assert x_or_y(3, 10, 20) == 10
    assert x_or_y(4, 10, 20) == 20

@pytest.mark.parametrize("n, x, y, expected", [
    (1, 5, 3, 3),
    (2, 5, 3, 5),
    (3, 5, 3, 5),
    (4, 5, 3, 3),
    (5, 5, 3, 5),
    (6, 5, 3, 3),
    (7, 5, 3, 5),
    (8, 5, 3, 3),
    (9, 5, 3, 3),
    (11, 5, 3, 5),
])
def test_x_or_y_parametrized(n, x, y, expected):
    assert x_or_y(n, x, y) == expected

def test_x_or_y_large_numbers():
    assert x_or_y(97, 100, 200) == 100  # prime
    assert x_or_y(100, 100, 200) == 200  # composite

def test_x_or_y_zero_values():
    assert x_or_y(3, 0, 0) == 0
    assert x_or_y(4, 0, 1) == 1

def test_x_or_y_negative_numbers():
    assert x_or_y(3, -1, -2) == -1
    assert x_or_y(4, -1, -2) == -2

@pytest.mark.parametrize("n, x, y", [
    (1.5, 5, 3),
    ("1", 5, 3),
])
def test_x_or_y_invalid_n(n, x, y):
    with pytest.raises((TypeError, ValueError)):
        x_or_y(n, x, y)

def test_x_or_y_invalid_xy():
    with pytest.raises(TypeError):
        x_or_y(3, "5", 3)
    with pytest.raises(TypeError):
        x_or_y(3, 5, "3")
    with pytest.raises(TypeError):
        x_or_y(3, None, 3)
    with pytest.raises(TypeError):
        x_or_y(3, 5, None)

def test_x_or_y_zero_and_negative_n():
    with pytest.raises(ValueError):
        x_or_y(0, 5, 3)
    with pytest.raises(ValueError):
        x_or_y(-1, 5, 3)