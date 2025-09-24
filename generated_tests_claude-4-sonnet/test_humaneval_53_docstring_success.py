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

def add(x: int, y: int):
    return x + y

def test_add_positive_numbers():
    assert add(2, 3) == 5
    assert add(5, 7) == 12
    assert add(1, 1) == 2

def test_add_negative_numbers():
    assert add(-2, -3) == -5
    assert add(-5, -7) == -12
    assert add(-1, -1) == -2

def test_add_mixed_numbers():
    assert add(-2, 3) == 1
    assert add(5, -7) == -2
    assert add(-10, 15) == 5

def test_add_with_zero():
    assert add(0, 0) == 0
    assert add(0, 5) == 5
    assert add(-3, 0) == -3
    assert add(0, -8) == -8

def test_add_large_numbers():
    assert add(1000000, 2000000) == 3000000
    assert add(-1000000, -2000000) == -3000000
    assert add(999999999, 1) == 1000000000

@pytest.mark.parametrize("x,y,expected", [
    (1, 2, 3),
    (0, 0, 0),
    (-1, 1, 0),
    (100, -50, 50),
    (-25, -25, -50),
    (42, 0, 42)
])
def test_add_parametrized(x, y, expected):
    assert add(x, y) == expected

def test_add_commutative_property():
    assert add(3, 7) == add(7, 3)
    assert add(-4, 9) == add(9, -4)
    assert add(0, 15) == add(15, 0)

def test_add_associative_property():
    a, b, c = 2, 3, 4
    assert add(add(a, b), c) == add(a, add(b, c))
    
    a, b, c = -1, 5, -3
    assert add(add(a, b), c) == add(a, add(b, c))
