# Test cases for HumanEval/53
# Generated using Claude API



def add(x: int, y: int):
    """Add two numbers x and y
    >>> add(2, 3)
    5
    >>> add(5, 7)
    12
    """

    return x + y


# Generated test cases:
import pytest

def test_add_positive_numbers():
    assert add(2, 3) == 5
    assert add(5, 7) == 12
    assert add(100, 200) == 300

def test_add_negative_numbers():
    assert add(-2, -3) == -5
    assert add(-5, -7) == -12
    assert add(-10, -20) == -30

def test_add_zero():
    assert add(0, 0) == 0
    assert add(0, 5) == 5
    assert add(5, 0) == 5

def test_add_positive_and_negative():
    assert add(-5, 5) == 0
    assert add(10, -5) == 5
    assert add(-10, 5) == -5

@pytest.mark.parametrize("x, y, expected", [
    (2, 3, 5),
    (-2, -3, -5),
    (0, 0, 0),
    (1000, 1000, 2000),
    (-1000, 1000, 0),
    (5, -5, 0)
])
def test_add_parametrized(x, y, expected):
    assert add(x, y) == expected

def test_add_large_numbers():
    assert add(1000000, 2000000) == 3000000
    assert add(-1000000, -2000000) == -3000000

@pytest.mark.parametrize("x, y", [
    ("2", 3),
    (2, "3"),
    (None, 5),
    (5, None),
    ({}, [])
])
def test_add_invalid_types(x, y):
    with pytest.raises(TypeError):
        add(x, y)

def test_add_overflow():
    assert add(2**30, 2**30) == 2**31
    assert add(-2**30, -2**30) == -(2**31)