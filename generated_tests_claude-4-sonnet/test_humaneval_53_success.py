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
    assert add(10, 20) == 30
    assert add(1, 1) == 2

def test_add_negative_numbers():
    assert add(-2, -3) == -5
    assert add(-10, -20) == -30
    assert add(-1, -1) == -2

def test_add_mixed_positive_negative():
    assert add(5, -3) == 2
    assert add(-5, 3) == -2
    assert add(10, -10) == 0
    assert add(-7, 12) == 5

def test_add_with_zero():
    assert add(0, 0) == 0
    assert add(5, 0) == 5
    assert add(0, 5) == 5
    assert add(-5, 0) == -5
    assert add(0, -5) == -5

def test_add_large_numbers():
    assert add(1000000, 2000000) == 3000000
    assert add(-1000000, -2000000) == -3000000
    assert add(999999999, 1) == 1000000000

@pytest.mark.parametrize("x,y,expected", [
    (1, 2, 3),
    (0, 0, 0),
    (-1, 1, 0),
    (100, -50, 50),
    (-100, -200, -300),
    (42, 0, 42),
    (0, -42, -42)
])
def test_add_parametrized(x, y, expected):
    assert add(x, y) == expected

def test_add_commutative_property():
    assert add(3, 7) == add(7, 3)
    assert add(-5, 8) == add(8, -5)
    assert add(0, 15) == add(15, 0)

def test_add_missing_arguments():
    with pytest.raises(TypeError):
        add(5)
    
    with pytest.raises(TypeError):
        add()

def test_add_too_many_arguments():
    with pytest.raises(TypeError):
        add(1, 2, 3)