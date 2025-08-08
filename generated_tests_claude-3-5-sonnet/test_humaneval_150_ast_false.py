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
    assert x_or_y(2, "prime", "composite") == "prime"
    assert x_or_y(3, "prime", "composite") == "prime"
    assert x_or_y(5, "prime", "composite") == "prime"
    assert x_or_y(7, "prime", "composite") == "prime"
    assert x_or_y(11, "prime", "composite") == "prime"

def test_x_or_y_composite_numbers():
    assert x_or_y(4, "prime", "composite") == "composite"
    assert x_or_y(6, "prime", "composite") == "composite"
    assert x_or_y(8, "prime", "composite") == "composite"
    assert x_or_y(9, "prime", "composite") == "composite"
    assert x_or_y(10, "prime", "composite") == "composite"

def test_x_or_y_one():
    assert x_or_y(1, "prime", "composite") == "composite"

@pytest.mark.parametrize("n,x,y,expected", [
    (2, "A", "B", "A"),
    (4, "A", "B", "B"),
    (7, "A", "B", "A"),
    (1, "A", "B", "B"),
    (9, "A", "B", "B"),
])
def test_x_or_y_with_different_values(n, x, y, expected):
    assert x_or_y(n, x, y) == expected

@pytest.mark.parametrize("n,x,y,expected", [
    (13, True, False, True),
    (15, True, False, False),
    (17, True, False, True),
    (1, True, False, False),
])
def test_x_or_y_with_booleans(n, x, y, expected):
    assert x_or_y(n, x, y) == expected

@pytest.mark.parametrize("n,x,y,expected", [
    (23, 100, 200, 100),
    (24, 100, 200, 200),
    (1, 100, 200, 200),
])
def test_x_or_y_with_numbers(n, x, y, expected):
    assert x_or_y(n, x, y) == expected

def test_x_or_y_with_none():
    assert x_or_y(2, None, "value") == None
    assert x_or_y(4, "value", None) == None
    assert x_or_y(1, "value", None) == None

@pytest.mark.parametrize("n", [-1, 0, -5])
def test_x_or_y_with_negative_numbers(n):
    with pytest.raises(ValueError):
        x_or_y(n, "x", "y")

def test_x_or_y_with_invalid_types():
    with pytest.raises(TypeError):
        x_or_y("string", "x", "y")
    with pytest.raises(TypeError):
        x_or_y(None, "x", "y")
    with pytest.raises(TypeError):
        x_or_y([], "x", "y")